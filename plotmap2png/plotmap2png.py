#!/usr/bin/env python

# Donated to the public domain 2019 by Sam Trenholme

# This requires python3 and the "pypng" module
# This code has been tested with Python 3.6.8

# This code takes the output of "totestraRG32.py" when run in standalone
# mode and generates a PNG file of the generated world, which is put in the
# file out.png
import sys,re, png

world = []
for line in sys.stdin:
    pngline = ()
    if(len(line) >= 145):
        mapline = line[0:144]
        for pixel in mapline:
            if(pixel == '+'): # Plains
                pngline += (32,128,32)
                pngline += (32,128,32)
            elif(pixel == 'n'): # Hills
                pngline += (128,128,32)
                pngline += (128,128,32)
            elif(pixel == 'A'): # Mountains
                pngline += (0,0,0)
                pngline += (0,0,0)
            else: # Water
                pngline += (0,0,128)
                pngline += (0,0,128)
        world.append(pngline)
        world.append(pngline)

outfile = open('out.png', 'wb')
outpng = png.Writer(288,len(world))
outpng.write(outfile, world)
print("out.png written")
