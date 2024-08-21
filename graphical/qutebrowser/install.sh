#!/bin/bash
mkdir -p "$HOME/.config/qutebrowser"
ln -s "$(pwd)/config.py" "$HOME/.config/qutebrowser/config.py"
