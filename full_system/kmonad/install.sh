#!/bin/bash
set -o errexit
set -o nounset

this_dir="$(dirname ${BASH_SOURCE[0]})"
curl -fSL -o "$HOME/.local/bin/kmonad" "kmonad_url"
systemctl --user enable --now "$this_dir/kmonad.service"
