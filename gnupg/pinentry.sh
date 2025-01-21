#!/bin/sh
case "${PINENTRY_USER_DATA-}" in
*USE_TTY=1*)
  exec /usr/bin/pinentry-curses "$@"
  ;;
esac
exec /usr/bin/pinentry-gtk "$@"
