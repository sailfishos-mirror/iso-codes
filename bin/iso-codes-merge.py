#!/usr/bin/env python

import sys
import os
import logging
import tempfile
import urllib
import subprocess

lang2Name = {'af': 'Afrikaans',
 'am': 'Amharic',
 'ar': 'Arabic',
 'ast': 'Asturian',
 'az': 'Azerbaijani',
 'be': 'Belarusian',
 'be@latin': 'Belarusian (Latin script)',
 'bg': 'Bulgarian',
 'bn': 'Bengali',
 'bn_IN': 'Bengali (India)',
 'bs': 'Bosnian',
 'ca': 'Catalan',
 'crh': 'Crimean Tatar (Crimean Turkish)',
 'cs': 'Czech',
 'da': 'Danish',
 'de': 'German',
 'el': 'Greek',
 'en_GB': 'English (British)',
 'en_ZA': 'English (South African)',
 'eo': 'Esperanto',
 'es': 'Spanish',
 'et': 'Estonian',
 'eu': 'Basque',
 'fa': 'Persian',
 'fi': 'Finnish',
 'fr': 'French',
 'ga': 'Irish',
 'gl': 'Galician',
 'gu': 'Gujarati',
 'he': 'Hebrew',
 'hi': 'Hindi',
 'hr': 'Croatian',
 'hu': 'Hungarian',
 'hy': 'Armenian',
 'ia': 'Interlingua',
 'id': 'Indonesian',
 'is': 'Icelandic',
 'it': 'Italian',
 'ja': 'Japanese',
 'ka': 'Georgian',
 'kk': 'Kazakh',
 'kn': 'Kannada',
 'ko': 'Korean',
 'ku': 'Kurdish',
 'ky': 'Kirghiz',
 'lg': 'Luganda',
 'lo': 'Lao',
 'lt': 'Lithuanian',
 'lv': 'Latvian',
 'mk': 'Macedonian',
 'ml': 'Malayalam',
 'mn': 'Mongolian',
 'mr': 'Marathi',
 'ms': 'Malay',
 'mt': 'Maltese',
 'nb': 'Norwegian Bokmaal',
 'nds': 'Low German',
 'ne': 'Nepali',
 'nl': 'Dutch',
 'nn': 'Norwegian Nynorsk',
 'pa': 'Punjabi',
 'pl': 'Polish',
 'ps': 'Pashto',
 'pt': 'Portuguese',
 'pt_BR': 'Brazilian Portuguese',
 'ro': 'Romanian',
 'ru': 'Russian',
 'rw': 'Kinyarwanda',
 'sk': 'Slovak',
 'sl': 'Slovenian',
 'sq': 'Albanian',
 'sr': 'Serbian',
 'sv': 'Swedish',
 'sw': 'Swahili',
 'ta': 'Tamil',
 'te': 'Telugu',
 'tg': 'Tajik',
 'th': 'Thai',
 'tr': 'Turkish',
 'uk': 'Ukrainian',
 'vi': 'Vietnamese',
 'wa': 'Walloon',
 'zh_CN': 'Chinese (simplified)',
 'zh_HK': 'Chinese (Hong Kong)',
 'zh_TW': 'Chinese (traditional)'}

class Isocodes(object):

    def __init__(self, home=None):
        self.home = home or "."
        self.tmpfiles = []

    def _getUrl(self, domain, lang):
        return "http://translationproject.org/latest/%s/%s.po" % (domain, lang)

    def _msgfmt(self, fname):
        logging.info(fname)
        if not os.path.exists(fname):
            logging.info('Not Exist')
        else:
            subprocess.check_call(['msgfmt', '-v', fname])

    def _msgcanonicalformat(self, fname, domain):
        logging.info(fname)
        potfile = os.path.join(self.home, domain, domain+".pot")
        subprocess.check_call(['msgmerge', '--previous', '-o', fname, fname, potfile])
        subprocess.check_call(['msgattrib', '--no-obsolete', '-o', fname, fname])
        subprocess.check_call(['sed', '-i', '-e', 's/^"Project-Id-Version: iso.*/"Project-Id-Version: ' + domain + '\\\\n"/', fname])

    def _getOldFname(self, domain, lang):
        return os.path.join(self.home, domain, lang+".po")

    def merge(self, domain, lang):
        url = self._getUrl(domain, lang)
        logging.info(url)
        oldfname = self._getOldFname(domain, lang)
        newfname = self._downloadFile(url)
        self._msgcanonicalformat(newfname, domain)
        self._diff(oldfname, newfname)
        self._msgfmt(oldfname)
        self._msgfmt(newfname)

        res = raw_input('merge this (Y/n): ')
        if res == '' or res == 'y' or res == 'Y':
            self._doMerge(domain, lang, oldfname, newfname)

    def _doMerge(self, domain, lang, oldfname, newfname):
        logging.info("_doMerge: %s, %s" % (oldfname, newfname))
        os.rename(newfname, oldfname)
        subprocess.check_call(['git', 'add', oldfname])
        translator = self._findLastTranslator(oldfname)
        changelogFname = self._updateChangeLog(domain, lang, translator)
        subprocess.check_call(['git', 'add', changelogFname])
        subprocess.check_call(['git', 'diff', 'HEAD'])
        res = raw_input('commit this (Y/n): ')
        if res == '' or res == 'y' or res == 'Y':
            commitMessage = '%s: %s by %s from TP' % (domain, lang2Name[lang], translator)
            subprocess.check_call(['git', 'commit', '-m', commitMessage])

    def _downloadFile(self, url):
        fd, ofname = tempfile.mkstemp(dir=self.home)
        ofile = os.fdopen(fd, 'wb')
        ofile.write(urllib.urlopen(url).read())
        ofile.close()
        self.tmpfiles.append(ofname)
        return ofname

    def _diff(self, fname1, fname2):
        subprocess.call(['diff', '-u', fname1, fname2])

    def __del__(self):
        for fname in self.tmpfiles:
            logging.info(fname)
            if os.path.exists(fname):
                os.unlink(fname)

    def _findLastTranslator(self, fname):
        prefix ='"Last-Translator: '
        for line in file(fname):
            if line.startswith(prefix):
                line = line[len(prefix):]
                return line[:line.index('<')].strip()
        return None

    def _updateChangeLog(self, domain, lang, translator):
        changelogFname = os.path.join(self.home, 'ChangeLog')
        lines = file(changelogFname).readlines()
        section, rest = self._findFirstSection(lines)
        before, middle, after = self._findDomainLines(section, domain)
        self._updateChangeLog2(middle, domain, lang, translator)
        file(changelogFname, 'w').writelines(before + middle + after + rest)
        return changelogFname

    def _updateChangeLog2(self, lines, domain, lang, translator):
        if not lines:
            line = '  [ ISO %s translations ]\n' % domain[4:].replace('_', '-')
            lines[:] = [line, '\n']

        line = '  * %s by %s (TP)\n' % (lang2Name[lang], translator)
        lines[-1:-1] = [line]

    def _findFirstSection(self, lines):
        for i in range(1, len(lines)):
            if lines[i].startswith('iso-codes'):
                return lines[:i], lines[i:]

    def _findDomainLines(self, lines, domain):
        keyword = '[ ISO %s translations ]' % domain[4:].replace('_', '-')

        i1 = None
        i2 = None
        for i in range(len(lines)):
            line = lines[i]
            if keyword in line:
                i1 = i
                break

        if i1 is not None:
            for i in range(i1, len(lines)):
                line = lines[i]
                if not line.strip():
                    i2 = i
                    break

        if i1 is None:
            return lines[:-1], [], lines[-1:]
        else:
            return lines[:i1], lines[i1:i2+1], lines[i2+1:]

def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: %s <domain> <lang>\n' % os.path.basename(sys.argv[0]))
        sys.exit(2)
    isocodes = Isocodes()
    isocodes.merge(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
