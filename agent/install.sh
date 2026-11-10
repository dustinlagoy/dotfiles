#!/bin/bash
mkdir -p "$HOME/.pi/agent"
../link.sh "$(pwd)/pi/models.json" "$HOME/.pi/agent/models.json"
../link.sh "$(pwd)/pi/settings.json" "$HOME/.pi/agent/settings.json"
../link.sh "$(pwd)/pi/keybindings.json" "$HOME/.pi/agent/keybindings.json"

mkdir -p "$HOME/.config/crush"
../link.sh "$(pwd)/crush/crush.json" "$HOME/.config/crush/crush.json"
../link.sh "$(pwd)/crush/long.md" "$HOME/.config/crush/long.md"

mkdir -p "$HOME/.claude"
../link.sh "$(pwd)/claude/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
../link.sh "$(pwd)/claude/settings.json" "$HOME/.claude/settings.json"
# Write ~/.claude.json with hasCompletedOnboarding so that a container with
# CLAUDE_CODE_OAUTH_TOKEN exported starts without the first-run wizard (theme
# / auth prompts). See https://github.com/anthropics/claude-code/issues/8938.
../link.sh "$(pwd)/claude/claude.json" "$HOME/.claude.json"
../link.sh "$(pwd)/claude/curl.sh" "$HOME/.local/bin/curl.sh"
../link.sh "/bin/bash" "$HOME/.local/bin/du"
if command -v uv
then
    uv tool install trafilatura
fi
exit 0
