import PIL
from PIL import Image, ImageDraw
import math

xposition = 0
yposition = 0

output = ""

with open("../git.txt", encoding="utf-8") as file:
    #data = file.read()
    data_lines = file.readlines()

    image = Image.new("RGBA", (128,math.ceil(math.ceil(len(data_lines) / 10) / 16) * 8), color=(0,0,0,0))
    draw = ImageDraw.Draw(image)

    line_i = 0
    ranges = [[]]
    while line_i < len(data_lines):
        char_line = data_lines[line_i].strip("\n")
        if char_line.startswith("0x"):
            thischarcode = int(char_line, 16)
        else:
            thischarcode = ord(char_line)

        if line_i >= 1: # this isn't the first character, so...
            if thischarcode != ranges[-1][-1] + 1:
                # which basically means "if thischarcode != the last character of the last range plus one"
                ranges.append([]) # add a new range

        ranges[-1].append(thischarcode) # add this character codepoint to the last range
        
        line_i += 1
        for y in range(8):
            for x in range(8):
                char = data_lines[line_i][x]
                if char == "0":
                    image.putpixel(((xposition*8) + x,(yposition*8) + y),(255,255,255,255))
                else:
                    image.putpixel(((xposition*8) + x,(yposition*8) + y),(0,0,0,0))
            line_i += 1
        line_i += 1
        xposition += 1
        if xposition > 15:
            xposition = 0
            yposition += 1

output = '<?xml version="1.0" encoding="UTF-8"?>\n<font_metadata>\n    <display_name>english/…</display_name>\n    <width>8</width>\n    <height>8</height>\n    <white_teeth>1</white_teeth>\n    <chars>\n'
i=0
while i < len(ranges):
    output = output + ('        <range start="0x%02X" end="0x%02X"/>\n'%(ranges[i][0],ranges[i][len(ranges[i])-1]))
    i=i+1
output = output + '    </chars>\n    <special>\n        <range start="0x00" end="0x1F" advance="6"/>\n    </special>\n    <fallback>buttons_8x8</fallback>\n</font_metadata>'
 
image.save("../font.png")
with open("../font.fontmeta", "w", encoding="utf-8") as file:
    file.write(output + "\n")
