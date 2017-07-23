# -*- coding: utf-8 -*-

import KofiPy as kofi
from os import listdir
from os.path import isfile, join
import imghdr

def list_images():
    mypath = "/home/cem/Desktop/kofipics/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyims = []
    for f in onlyfiles:
        if imghdr.what(mypath + f) in ["jpeg", "bmp", "png"]:
            onlyims.append(mypath + f)
    return onlyims

def main():
    with open("targets.txt", "w") as targets:
        for f in list_images():
            print>>targets , f



if __name__ == "__main__":
    main()
