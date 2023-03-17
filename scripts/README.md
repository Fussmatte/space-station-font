# Space Station font scripts
Here are some scripts for generating from (and to) `font.png` and `font.fontmeta` (*vfont*).
* `vfont_to_ttf.py` — **Requires FontForge and Pillow/PIL.** (The former can be installed on Ubuntu/Debian-based distros with `python3-fontforge`.)
Generate a TTF from *vfont*. Relies on the files existing in the parent directory. Also accepts arguments for custom font generation, see script comments for details.
* `vfont_to_git.py` — Generate `git.txt` (a human-readable text-based bitmap font format) from *vfont*.
* `git_to_vfont.py` — Generate *vfont* from `git.txt`.
* `sort_git.py` — Sort `git.txt` by Unicode codepoint, which can then be re-generated into *vfont*.
