#-----------------------------------------------------------------------

=head1 NAME

Locale::Country - ISO codes for country identification (ISO 3166)

=head1 SYNOPSIS

    use Locale::Country;
    
    $country = code2country('jp');               # $country gets 'Japan'
    $code    = country2code('Norway');           # $code gets 'no'
    
    @codes   = all_country_codes();
    @names   = all_country_names();
    
    # add "uk" as a pseudo country code for United Kingdom
    Locale::Country::_alias_code('uk' => 'gb');

=cut

#-----------------------------------------------------------------------

package Locale::Country;
use strict;
require 5.002;

#-----------------------------------------------------------------------

=head1 DESCRIPTION

The C<Locale::Country> module provides access to the ISO
codes for identifying countries, as defined in ISO 3166.
You can either access the codes via the L<conversion routines>
(described below), or with the two functions which return lists
of all country codes or all country names.

There are three different code sets you can use for identifying
countries:

=over 4

=item B<alpha-2>

Two letter codes, such as 'tv' for Tuvalu.
This code set is identified with the symbol C<LOCALE_CODE_ALPHA_2>.

=item B<alpha-3>

Three letter codes, such as 'brb' for Barbados.
This code set is identified with the symbol C<LOCALE_CODE_ALPHA_3>.

=item B<numeric>

Numeric codes, such as 064 for Bhutan.
This code set is identified with the symbol C<LOCALE_CODE_NUMERIC>.

=back

All of the routines take an optional additional argument
which specifies the code set to use.
If not specified, it defaults to the two-letter codes.
This is partly for backwards compatibility (previous versions
of this module only supported the alpha-2 codes), and
partly because they are the most widely used codes.

The alpha-2 and alpha-3 codes are not case-dependent,
so you can use 'BO', 'Bo', 'bO' or 'bo' for Bolivia.
When a code is returned by one of the functions in
this module, it will always be lower-case.

=cut

#-----------------------------------------------------------------------

require Exporter;
use Carp;
use Locale::Constants;


#-----------------------------------------------------------------------
#	Public Global Variables
#-----------------------------------------------------------------------
use vars qw($VERSION @ISA @EXPORT @EXPORT_OK);
$VERSION   = sprintf("%d.%02d", q$Revision$ =~ /(\d+)\.(\d+)/);
@ISA       = qw(Exporter);
@EXPORT    = qw(code2country country2code
                all_country_codes all_country_names
		country_code2code
		LOCALE_CODE_ALPHA_2 LOCALE_CODE_ALPHA_3 LOCALE_CODE_NUMERIC);

#-----------------------------------------------------------------------
#	Private Global Variables
#-----------------------------------------------------------------------
my $CODES     = [];
my $COUNTRIES = [];


#=======================================================================

=head1 CONVERSION ROUTINES

There are three conversion routines: C<code2country()>, C<country2code()>,
and C<country_code2code()>.

=over 8

=item code2country( CODE, [ CODESET ] )

This function takes a country code and returns a string
which contains the name of the country identified.
If the code is not a valid country code, as defined by ISO 3166,
then C<undef> will be returned:

    $country = code2country('fi');

=item country2code( STRING, [ CODESET ] )

This function takes a country name and returns the corresponding
country code, if such exists.
If the argument could not be identified as a country name,
then C<undef> will be returned:

    $code = country2code('Norway', LOCALE_CODE_ALPHA_3);
    # $code will now be 'nor'

The case of the country name is not important.
See the section L<KNOWN BUGS AND LIMITATIONS> below.

=item country_code2code( CODE, CODESET, CODESET )

This function takes a country code from one code set,
and returns the corresponding code from another code set.

    $alpha2 = country_code2code('fin',
		 LOCALE_CODE_ALPHA_3 => LOCALE_CODE_ALPHA_2);
    # $alpha2 will now be 'fi'

If the code passed is not a valid country code in
the first code set, or if there isn't a code for the
corresponding country in the second code set,
then C<undef> will be returned.

=back

=cut

#=======================================================================
sub code2country
{
    my $code = shift;
    my $codeset = @_ > 0 ? shift : LOCALE_CODE_DEFAULT;


    return undef unless defined $code;

    #-------------------------------------------------------------------
    # Make sure the code is in the right form before we use it
    # to look up the corresponding country.
    # We have to sprintf because the codes are given as 3-digits,
    # with leading 0's. Eg 052 for Barbados.
    #-------------------------------------------------------------------
    if ($codeset == LOCALE_CODE_NUMERIC)
    {
	return undef if ($code =~ /\D/);
	$code = sprintf("%.3d", $code);
    }
    else
    {
	$code = lc($code);
    }

    if (exists $CODES->[$codeset]->{$code})
    {
        return $CODES->[$codeset]->{$code};
    }
    else
    {
        #---------------------------------------------------------------
        # no such country code!
        #---------------------------------------------------------------
        return undef;
    }
}

sub country2code
{
    my $country = shift;
    my $codeset = @_ > 0 ? shift : LOCALE_CODE_DEFAULT;


    return undef unless defined $country;
    $country = lc($country);
    if (exists $COUNTRIES->[$codeset]->{$country})
    {
        return $COUNTRIES->[$codeset]->{$country};
    }
    else
    {
        #---------------------------------------------------------------
        # no such country!
        #---------------------------------------------------------------
        return undef;
    }
}

sub country_code2code
{
    (@_ == 3) or croak "country_code2code() takes 3 arguments!";

    my $code = shift;
    my $inset = shift;
    my $outset = shift;
    my $outcode = shift;
    my $country;


    return undef if $inset == $outset;
    $country = code2country($code, $inset);
    return undef if not defined $country;
    $outcode = country2code($country, $outset);
    return $outcode;
}

#=======================================================================

=head1 QUERY ROUTINES

There are two function which can be used to obtain a list of all codes,
or all country names:

=over 8

=item C<all_country_codes( [ CODESET ] )>

Returns a list of all two-letter country codes.
The codes are guaranteed to be all lower-case,
and not in any particular order.

=item C<all_country_names( [ CODESET ] )>

Returns a list of all country names for which there is a corresponding
country code in the specified code set.
The names are capitalised, and not returned in any particular order.

Not all countries have alpha-3 and numeric codes -
some just have an alpha-2 code,
so you'll get a different number of countries
depending on which code set you specify.

=back

=cut

#=======================================================================
sub all_country_codes
{
    my $codeset = @_ > 0 ? shift : LOCALE_CODE_DEFAULT;

    return keys %{ $CODES->[$codeset] };
}

sub all_country_names
{
    my $codeset = @_ > 0 ? shift : LOCALE_CODE_DEFAULT;

    return values %{ $CODES->[$codeset] };
}

#-----------------------------------------------------------------------

=head1 CODE ALIASING

This module supports a semi-private routine for specifying two letter
code aliases.

    Locale::Country::_alias_code( ALIAS => CODE [, CODESET ] )

This feature was added as a mechanism for handling
a "uk" code. The ISO standard says that the two-letter code for
"United Kingdom" is "gb", whereas domain names are all .uk.

By default the module does not understand "uk", since it is implementing
an ISO standard. If you would like 'uk' to work as the two-letter
code for United Kingdom, use the following:

    use Locale::Country;
    
    Locale::Country::_alias_code('uk' => 'gb');

With this code, both "uk" and "gb" are valid codes for United Kingdom,
with the reverse lookup returning "uk" rather than the usual "gb".

=cut

#-----------------------------------------------------------------------

sub _alias_code
{
    my $alias = shift;
    my $real  = shift;
    my $codeset = @_ > 0 ? shift : LOCALE_CODE_DEFAULT;

    my $country;


    if (not exists $CODES->[$codeset]->{$real})
    {
        carp "attempt to alias \"$alias\" to unknown country code \"$real\"\n";
        return undef;
    }
    $country = $CODES->[$codeset]->{$real};
    $CODES->[$codeset]->{$alias} = $country;
    $COUNTRIES->[$codeset]->{"\L$country"} = $alias;

    return $alias;
}

#-----------------------------------------------------------------------

=head1 EXAMPLES

The following example illustrates use of the C<code2country()> function.
The user is prompted for a country code, and then told the corresponding
country name:

    $| = 1;   # turn off buffering
    
    print "Enter country code: ";
    chop($code = <STDIN>);
    $country = code2country($code, LOCALE_CODE_ALPHA_2);
    if (defined $country)
    {
        print "$code = $country\n";
    }
    else
    {
        print "'$code' is not a valid country code!\n";
    }

=head1 DOMAIN NAMES

Most top-level domain names are based on these codes,
but there are certain codes which aren't.
If you are using this module to identify country from hostname,
your best bet is to preprocess the country code.

For example, B<edu>, B<com>, B<gov> and friends would map to B<us>;
B<uk> would map to B<gb>. Any others?

=head1 KNOWN BUGS AND LIMITATIONS

=over 4

=item *

When using C<country2code()>, the country name must currently appear
exactly as it does in the source of the module. For example,

    country2code('United States')

will return B<us>, as expected. But the following will all return C<undef>:

    country2code('United States of America')
    country2code('Great Britain')
    country2code('U.S.A.')

If there's need for it, a future version could have variants
for country names.

=item *

In the current implementation, all data is read in when the
module is loaded, and then held in memory.
A lazy implementation would be more memory friendly.

=back

=head1 SEE ALSO

=over 4

=item Locale::Language

ISO two letter codes for identification of language (ISO 639).

=item Locale::Currency

ISO three letter codes for identification of currencies
and funds (ISO 4217).

=item ISO 3166

The ISO standard which defines these codes.

=item http://www.din.de/gremien/nas/nabd/iso3166ma/

Official home page for ISO 3166

=item http://www.egt.ie/standards/iso3166/iso3166-1-en.html

Another useful, but not official, home page.

=item http://www.cia.gov/cia/publications/factbook/docs/app-f.html

An appendix in the CIA world fact book which lists country codes
as defined by ISO 3166, FIPS 10-4, and internet domain names.

=back


=head1 AUTHOR

Neil Bowers E<lt>neilb@cre.canon.co.ukE<gt>

=head1 COPYRIGHT

Copyright (c) 1997-2001 Canon Research Centre Europe (CRE).

This module is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

=cut

#-----------------------------------------------------------------------

#=======================================================================
# initialisation code - stuff the DATA into the ALPHA2 hash
#=======================================================================
{
    my ($alpha2, $alpha3, $numeric);
    my $country;

    open(DATA, "/usr/share/iso-codes/iso-codes-2.tab") || 
      die "iso-codes data file not present";

    while (<DATA>)
    {
        next unless /\S/;
        chop;
        ($alpha2, $alpha3, $numeric, $country) = split(/\t/, $_, 4);

        $CODES->[LOCALE_CODE_ALPHA_2]->{$alpha2} = $country;
        $COUNTRIES->[LOCALE_CODE_ALPHA_2]->{"\L$country"} = $alpha2;

	if ($alpha3)
	{
            $CODES->[LOCALE_CODE_ALPHA_3]->{$alpha3} = $country;
            $COUNTRIES->[LOCALE_CODE_ALPHA_3]->{"\L$country"} = $alpha3;
	}

	if ($numeric)
	{
            $CODES->[LOCALE_CODE_NUMERIC]->{$numeric} = $country;
            $COUNTRIES->[LOCALE_CODE_NUMERIC]->{"\L$country"} = $numeric;
	}
	close(DATA);

    }
}

1;

