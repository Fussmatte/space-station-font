import PIL
from PIL import Image

xposition = 0
yposition = 0

output = ""

image = Image.open('font.png' ).convert('RGBA')

with open("font.txt", encoding="utf-8") as file:
    data = file.read()
    data = data[:-1] # no newline
    for i in range(len(data)):
        output += data[i] + "\n"
        for y in range(8):
            for x in range(8):
                pixel = image.getpixel(((xposition * 8) + x,(yposition * 8) + y))
                if pixel == (255,255,255,255):
                    output += "0"
                else:
                    output += "-"
            output += "\n"
        xposition += 1
        if xposition > 15:
            xposition = 0
            yposition += 1
        output += "\n"

with open("git.txt", "w", encoding="utf-8") as file:
    file.write(output[:-1])