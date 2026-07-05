# TODO

Fonts are the product; nothing here changes a curve. These are non-urgent improvements for a later pass.

- [ ] Add a reproducible build: export static and variable TTFs from the `.vfj` sources (FontLab command-line or a `fontmake`/`gftools` path), so releases don't depend on a manual FontLab export.
- [ ] Publish font binaries as a GitHub Release (attach the two variable TTFs) instead of only committing them.
- [ ] Add a rendered specimen image (or an HTML type tester) to the README so the design is visible without installing the fonts.
- [ ] Run `fontbakery` in CI for full font-quality checks, not just a fontTools parse.
- [ ] Consider shipping static instances (Regular/Medium/Bold/Black) for tools that don't read variation axes.
- [ ] Move the `.vfc` FontLab cache files out of git history entirely (currently untracked; kept only for local convenience).
- [ ] Document the exact axis defaults and named instances so users know what "Regular" maps to.
