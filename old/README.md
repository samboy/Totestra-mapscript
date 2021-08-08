# Totestra

Totestra is a program that makes random maps for Civilization IV. It
is based on Cephalo's excellent PerfectWorld2 map script, and uses
plate tectonics, meteor, and weather modeling to create a remarkably
realistic earth-like planet. It is an update to PerfectWorld that adds
more parameters that can be set inside Civ IV to the map generator, as
well as fixing some long standing bugs with Cephalo's map generator. One
goal of Totestra is 100% compatibility with PerfectWorld2; given the right
parameters, Totestra will make the exact same map that PerfectWorld2 did.

## Install

To install the script, copy Totestra.py to the PublicMaps directory,
which should be at /Users/yourname/Documents/My Games/Sid Meier's
Civilization 4 Complete/PublicMaps or somewhere similar.

## Using in stand-alone mode

It’s possible to use this map script to make maps without using
Civilization IV; this script now has a standalone mode for making maps
on the command line.  This is useful for people who want to see Perfect
World generated maps without starting Civilization IV, or for people
who want to automate making a large number of maps (useful for finding
seeds which make for really nice worlds).

To run it stand alone, be sure to be at a command line, have Python2
installed, then type in something like: `python2 Totestra.py 5`

This will generate the random map with the seed "5".  Note that, when run
standalone, the map generator will generate a plot map then exit. The map
is all of the default options, which can not be changed (in particular,
in the stand alone mode, we only generate 144x96 huge medium patience
world maps)

A tool for converting the unusual ASCII format generated by TotestraRG32
in to a PNG file is included in the directory `plotmap2png/`; this tool
requires Python 3 and the `pypng` library to run.  

Note that the information about the number of desert, flood plain, and
tundra squares near the end of the program’s output assume the map has
an arid climate.

## RadioGatún[32]

It’s also possible to run it either in stand-alone mode or in CivIV
using RadioGatún[32] instead of the Mersenne Twister as a random number
generator.  In stand-alone mode, put the letter `T` before the seed, e.g.
`python2 Totestra.py T285`.  To use RadioGatún[32] inside of CivIV, edit
Totestra.py to have the `UseRG32 = False` line say `UseRG32 = True`.

## More information

https://forums.civfanatics.com/threads/totestra-a-new-perfectworld2-fork.461262/