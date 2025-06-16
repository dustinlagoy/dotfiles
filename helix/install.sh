#!/bin/bash
mkdir -p "$HOME/.config/helix"
ln -s "$(pwd)/config.toml" "$HOME/.config/helix/config.toml"
ln -s "$(pwd)/languages.toml" "$HOME/.config/helix/languages.toml"
ln -s "$(pwd)/efm.yaml" "$HOME/.config/helix/efm.yaml"
ln -s "$(pwd)/themes" "$HOME/.config/helix/themes"
