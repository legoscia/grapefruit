AC_INIT([Grapefruit], [0.1], [], [grapefruit])
AM_INIT_AUTOMAKE([foreign dist-bzip2 dist-zip])

AC_CHECK_PROG(has_fontforge, fontforge, yes, no)
AS_IF([test x$has_fontforge != xyes],
      [AC_MSG_WARN([Fontforge not found; you will not be able to rebuild the font])])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
