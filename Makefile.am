EXTRA_DIST=README.org Grapefruit.sfd generate.py
MAINTAINERCLEANFILES=Grapefruit.ttf

dist_font_DATA=Grapefruit.ttf

# install font in user's font directory...
# is there a nice way to install the font system-wide?
fontdir=$(HOME)/.fonts

.sfd.ttf:
	fontforge $(srcdir)/generate.py $< $@
