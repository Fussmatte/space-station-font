import PIL
import re
from PIL import Image

xposition = 0
yposition = 0

output = ""

image = Image.open('../font.png' ).convert('RGBA')

with open("../font.fontmeta", encoding="utf-8") as file:
    fontmeta = file.read()
    ranges = re.findall(r'<range start="(0[xX][0-9a-fA-F]+)" end="(0[xX][0-9a-fA-F]+)"\/>',fontmeta)
    print(ranges)

    i = 0
    data = ""
    while i < len(ranges):
        for j in range(int(ranges[i][0],0),int(ranges[i][-1],0)+1):
            data = data + chr(j)
        i=i+1

    for i in range(len(data)):
        output += data[i] + "\n"
        for y in range(8):
            for x in range(8):
                pixel = image.getpixel(((xposition * 8) + x,(yposition * 8) + y))
                if pixel[3] != 0: #If alpha > 0
                    output += "0"
                else:
                    output += "-"
            output += "\n"
        xposition += 1
        if xposition > 15:
            xposition = 0
            yposition += 1
        output += "\n"

with open("../git.txt", "w", encoding="utf-8") as file:
    file.write(output[:-1])