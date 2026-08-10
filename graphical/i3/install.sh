#!/bin/bash
mkdir -p "$HOME/.config/i3"
../../link.sh "$(pwd)/config" "$HOME/.config/i3/config"
../../link.sh "$(pwd)/i3status_config" "$HOME/.config/i3status/config"
