# space-station-font
A Unicode font, in PNG and TTF format, based on the Commodore 64/VVVVVV font. Intended for use in Ved and versions of VVVVVV with Unicode support.

The `font.fontmeta` file, which contains the list of characters and other properties, must accompany the PNG file in the graphics data directory for VVVVVV in order to properly display the font.

The `git.txt` file contains bitmap data for the font in plaintext, in case you need that.

Once upon a time the TTF version was intended for [Ved](https://tolp.nl/ved), which now instead uses the same format as VVVVVV. The TTF version is still used by the program's homepage. Feel free to use it as a general-purpose C64-style font! It's licensed under the SIL Open Font License v1.1. See [LICENSE](LICENSE) for details.

Check out the [included Python scripts](/scripts) for converting stuff. (Make sure the png and fontmeta are in the parent directory from the scripts.)
