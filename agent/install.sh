#!/bin/bash
mkdir -p "$HOME/.config/crush"
../link.sh "$(pwd)/crush.json" "$HOME/.config/crush/crush.json"
../link.sh "$(pwd)/long.md" "$HOME/.config/crush/long.md"

mkdir -p "$HOME/.claude"
../link.sh "$(pwd)/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
../link.sh "$(pwd)/settings.json" "$HOME/.claude/settings.json"
# Write ~/.claude.json with hasCompletedOnboarding so that a container with
# CLAUDE_CODE_OAUTH_TOKEN exported starts without the first-run wizard (theme
# / auth prompts). See https://github.com/anthropics/claude-code/issues/8938.
../link.sh "$(pwd)/claude.json" "$HOME/.claude.json"
../link.sh "$(pwd)/curl.sh" "$HOME/.local/bin/curl.sh"
../link.sh "/bin/bash" "$HOME/.local/bin/du"
