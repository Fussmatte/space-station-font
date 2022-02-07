# Space Station font scripts
Here are some scripts for generating from (and to) `font.png` and `font.txt` (*txtpng*).
* `txtpng_to_ttf.py` — **Requires `fontforge` and `PIL`.** Generate a TTF from *txtpng*. Relies on the files existing in the parent directory. Also accepts arguments for custom font generation, see script comments for details.
* `txtpng_to_git.py` — Generate `git.txt` (a human-readable text-based bitmap font format) from *txtpng*.
* `git_to_txtpng.py` — Generate *txtpng* from `git.txt`.