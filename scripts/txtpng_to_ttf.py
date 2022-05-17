from __future__ import print_function
import sys
import fontforge
from PIL import Image
#from textwrap import wrap

# Original code by benob (https://github.com/benob/png_font_to_ttf)
# Modified for Space Station by Reese Rivers (https://github.com/Fussmatte/space-station-font)
# Thanks to Dav999 for writing the charsetraw split code!

# For the font.png make sure the transparency is FIRST in the png's palette!
# This should be visible in Aseprite at least

fontName        = "SpaceStation"
fontFullName    = "Space Station"
fontVersion     = "3.4"

output          = "../space-station.ttf"
imagefilename   = "../font.png"
width           = 8
height          = 8
charsetfilename = "../font.txt"

# optional: provide own font info
# fontforge -script pngtxt_to_ttf.py <output.ttf> <font.png> <font.txt> <width> <height> <fontName> <fontFullName> <fontVer>
if len(sys.argv) == 9:
    output          = sys.argv[1]
    imagefilename   = sys.argv[2]
    charsetfilename = sys.argv[3]
    width           = int(sys.argv[4])
    height          = int(sys.argv[5])
    fontName        = sys.argv[6]
    fontFullName    = sys.argv[7]
    fontVer         = sys.argv[8]
else:
    print("No font info provided, exporting for Space Station")

image = Image.open(imagefilename)
charsetfile = open(charsetfilename,"r")
charsetraw = charsetfile.read()
#charset = wrap(charsetraw,image.width // width,break_on_hyphens=False)

charset = [""]
col = 0
for c in charsetraw:
    charset[-1] += c
    col += 1
    if col >= image.width // width:
        charset.append("")
        col = 0

factor = 10 # size factor so that coords are in range [16, 65536]

font = fontforge.font() 
font.ascent = height * factor
font.descent = 0 * factor
font.encoding = 'UnicodeFull' # required encoding to access private range

pixels = image.load()

for j in range(image.height // height):
    print(f'{j:04}' + '/' + str(len(charset)-1),end=' ') # current row
    for i in range(image.width // width):
      offset = i + j * (image.width // width)
      for q in range(len(charset[j])):
          if i==0: print(charset[j][q],end='')    # current character
          char = font.createChar(ord(charset[j][q]))
          char.width = width * factor
          pen = char.glyphPen()
          for y in range(height):
              for x in range(width):
                  pixel = pixels[q * width + x, j * height + y]
                  if pixel != 0: # if pixel is not transparent
                      pen.moveTo((x * factor, (height - y) * factor)) # draw a pixel
                      pen.lineTo(((x + 1) * factor, (height - y) * factor))
                      pen.lineTo(((x + 1) * factor, (height - y - 1) * factor))
                      pen.lineTo((x * factor, (height - y - 1) * factor))
                      pen.closePath()
      if i==(image.width // width)-1: print() 

# export to font 
font.fontname   = fontName
font.fullname   = fontFullName
font.version    = fontVersion
font.familyname = font.fullname
with open("../LICENSE", "r") as file:
    font.copyright = file.read()

font.generate(output, flags=('opentype'))
