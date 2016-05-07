from sys import argv
import re

script, inputName, outputName = argv

with open(inputName, "r") as myfile:
    oText = ''
    for line in myfile:
        oText = oText + "\n" + " ".join([w.upper() if w == "i" else w for w in line.split()])

oFile = open(outputName, "w")
oFile.write(oText)
