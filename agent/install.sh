#!/bin/bash
mkdir -p "$HOME/.local/share/crush"
../link.sh "$(pwd)/crush.json" "$HOME/.config/crush/crush.json"
../link.sh "$(pwd)/long.md" "$HOME/.config/crush/long.md"
