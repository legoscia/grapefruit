#!/usr/bin/env fontforge
# -*- coding: utf-8 -*-
# This is a Python script, meant to be invoked through Fontforge.

import fontforge
import sys

if len(sys.argv) != 3:
    print "Usage:",sys.argv[0],"SFDFILE TTFFILE"
    print "Generate a TTF file from a SFD file through Fontforge."
    exit(1)

sfd_file = sys.argv[1]
ttf_file = sys.argv[2]
font = fontforge.open(sfd_file)
print sfd_file,"→",ttf_file
font.generate(ttf_file)
