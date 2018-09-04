# How to release a new version of iso-codes

Make sure you have all the latest updates in your working copy.

```
$ git pull
```

Update the version number in configure.ac, also update the ChangeLog
with the current release number, your name, and the date.
Commit the changes.

```
$ git commit -am "Prepare next release"
```

Update all automatically generated files (configure, Makefiles, etc.)
and commit.

```
$ ./bootstrap
$ git commit -am "Update automatically generated files"
```

Create the Makefiles.

```
$ ./configure
```

Update all .po files (including the automatic update of the
sr@latin locale) and commit.

```
$ make update-po
$ git commit -am "Refresh .po files"
```

Create a tag for the next release.
Please respect the following release numbering scheme, which
adheres to semantic versioning:

- Major version: use this for data organisation changes (like the
  switch to JSON, or incompatible changes in the JSON files like the
  removal of a field)
- Minor version: use this when one of the ISO lists is updated,
  for compatible changes to the JSON files, like the addition of
  a field, or for translation updates.

```
$ git tag -sm "Release MAJOR.MINOR" iso-codes-MAJOR.MINOR
```

Use the Makefile target "release" for creating checked tarballs.

```
$ make release
```

Use the Makefile target "sign-release" to sign the tarballs.

```
$ make sign-release
```

Upload the tarballs and your signatures to Salsa. Also push the
changes to the git repository.

```
$ git push
$ git push --tags
```
