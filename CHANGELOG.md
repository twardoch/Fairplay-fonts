# Changelog

All notable changes to Fairplay are recorded here. Version numbers follow the git `vX.Y.Z` tags on this repository; the fonts themselves carry their own internal version (currently 2.000).

## [Unreleased]

### Added
- README rewritten to describe what Fairplay changes versus Playfair Display: the semi-condensed display cut, the `opsz`/`wght`/`wdth` axes, and Cyrillic coverage.
- `docs/assets/icon.png` project icon.
- Continuous integration: a GitHub Actions job that parses every shipped variable font with fontTools and checks its `name`, `fvar`, and glyph tables on each push.
- `CHANGELOG.md` and `TODO.md`.

### Changed
- `.gitignore` de-duplicated; the `*.vfc` FontLab cache rule is now stated once.

## [1.0.0] — 2025-09-24
- First tagged release of the repository, packaging the Fairplay variable fonts (upright and italic, font version 2.000) with FontLab `.vfj` sources and the InDesign/PDF test documents.

## Earlier history
Fairplay began in 2014 as a fork of Playfair Display (repository tags `v1.004` through `1.202`, mirroring upstream). Work between 2015 and 2020 reshaped the design into the semi-condensed display family and reworked the Cyrillic letterforms (for example the adjustments to `ю`, `тцщгдл`, and related glyphs across all masters).
