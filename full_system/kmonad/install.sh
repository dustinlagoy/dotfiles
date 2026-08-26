#!/bin/bash
set -o errexit
set -o nounset
VERSION="0.4.5"

this_dir="$(dirname ${BASH_SOURCE[0]})"
curl -fSL -o "$HOME/.local/bin/kmonad" "https://github.com/kmonad/kmonad/releases/download/$VERSION/kmonad"
systemctl --user enable --now "$this_dir/kmonad.service"
