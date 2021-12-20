# space-station-font
A Unicode font, in PNG and TTF format, based on the Commodore 64/VVVVVV font. Intended for use in Ved and versions of VVVVVV with Unicode support.

**⚠ NOTICE:** *The TTF and <code>git.txt</code> versions of the font may be out-of-date compared to the png version, so use the latter if possible.*

The PNG file can be used with versions of VVVVVV with Unicode support. It can also be used with Pixel Font Converter! by YellowAfterlife (https://yal.cc/r/20/pixelfont/) in conjunction with the JSON file, which contains character map data and other font information. Note that the letters are in white.

The <code>font.txt</code> file, which contains the character map, must accompany the PNG file in the graphics data directory for VVVVVV in order to properly display the font.

The <code>git.txt</code> file contains bitmap data for the font in plaintext, in case you need that. The included Python scripts will convert a paired PNG and <code>font.txt</code> to <code>git.txt</code> and vice versa. (Make sure the files and scripts are all in one directory, named the same as in the repo).

The TTF file is intended for Ved, but feel free to use it for whatever!
