EXTRA_DIST=README.org Grapefruit.sfd generate.py
MAINTAINERCLEANFILES=Grapefruit.ttf

dist_font_DATA=Grapefruit.ttf

# this defaults to /usr/local/share/fonts
fontdir=$(datarootdir)/fonts

.sfd.ttf:
	fontforge $(srcdir)/generate.py $< $@
