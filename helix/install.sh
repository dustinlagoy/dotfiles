#!/bin/bash
mkdir -p "$HOME/.config/helix"
../link.sh "$(pwd)/config.toml" "$HOME/.config/helix/config.toml"
../link.sh "$(pwd)/languages.toml" "$HOME/.config/helix/languages.toml"
../link.sh "$(pwd)/efm.yaml" "$HOME/.config/helix/efm.yaml"
../link.sh "$(pwd)/themes" "$HOME/.config/helix/themes"
