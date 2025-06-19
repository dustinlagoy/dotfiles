#!/bin/bash
target=$1
link=$2
if [ -L $link ]
then
  current=$(readlink -e $link)
  if [[ $current == $target ]]
  then
    # echo "link $link already exists and has correct target"
    exit 0
  fi
  echo "ERROR link $link already exists but points to $current"
  exit 1
fi
if [ -a $link ]
then
  echo "ERROR cannot overwrite existing file $link"
  exit 1
fi
ln -s "$target" "$link"
