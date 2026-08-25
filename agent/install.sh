#!/bin/bash
mkdir -p "$HOME/.config/crush"
../link.sh "$(pwd)/crush.json" "$HOME/.config/crush/crush.json"
../link.sh "$(pwd)/long.md" "$HOME/.config/crush/long.md"

mkdir -p "$HOME/.claude"
../link.sh "$(pwd)/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
../link.sh "$(pwd)/settings.json" "$HOME/.claude/settings.json"
../link.sh "$(pwd)/claude.json" "$HOME/.claude.json"
