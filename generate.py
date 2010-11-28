#!/usr/bin/env fontforge
# -*- coding: utf-8 -*-
#
# Copyright © 2010, Magnus Henoch <magnus.henoch@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
