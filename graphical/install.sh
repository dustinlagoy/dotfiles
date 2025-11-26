#!/bin/bash
# Get list of directories
directories=$(ls -d */)
for directory in $directories
do
    # Run the install for each
    (cd $directory; ./install.sh) || echo "error running install.sh in $directory"
done
mkdir -p $HOME/.config/dunst
../link.sh "$(pwd)/dunstrc" "$HOME/.config/dunst/dunstrc"
