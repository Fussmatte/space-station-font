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
    while line_i < len(data_lines):
        output += data_lines[line_i].strip("\n")
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
 
image.save("../font.png")
with open("../font.txt", "w", encoding="utf-8") as file:
    file.write(output + "\n")