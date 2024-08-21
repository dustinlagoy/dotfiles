# # This is here so configs done via the GUI are still loaded.
# # Remove it to not load settings done via the GUI.
config.load_autoconfig(True)

# # Number of commands to save in the command history. 0: no history / -1:
# # unlimited
# # Type: Int
c.completion.cmd_history_max_items = 1000

# # Which method of blocking ads should be used.  Support for Adblock Plus
# # (ABP) syntax blocklists using Brave's Rust library requires the
# # `adblock` Python package to be installed, which is an optional
# # dependency of qutebrowser. It is required when either `adblock` or
# # `both` are selected.
# # Type: String
# # Valid values:
# #   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
# #   - adblock: Use Brave's ABP-style adblocker
# #   - hosts: Use hosts blocking
# #   - both: Use both hosts blocking and Brave's ABP-style adblocker
# c.content.blocking.method = 'auto'
c.content.blocking.method = "both"

# # Which cookies to accept. With QtWebEngine, this setting also controls
# # other features with tracking capabilities similar to those of cookies;
# # including IndexedDB, DOM storage, filesystem API, service workers, and
# # AppCache. Note that with QtWebKit, only `all` and `never` are
# # supported as per-domain values. Setting `no-3rdparty` or `no-
# # unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# # `all`. If this setting is used with URL patterns, the pattern gets
# # applied to the origin/first party URL of the page making the request,
# # not the request URL.
# # Type: String
# # Valid values:
# #   - all: Accept all cookies.
# #   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
# #   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
# #   - never: Don't accept cookies at all.
# c.content.cookies.accept = 'all'
c.content.cookies.accept = "all"

# # Store cookies.
# # Type: Bool
# c.content.cookies.store = True
c.content.cookies.store = True

# with config.pattern('*://google.com/') as p:
#     p.content.cookies.accept = 'no-3rdparty'
# with config.pattern('*://facebook.com/') as p:
#     p.content.cookies.accept = 'all'
# with config.pattern('*://discourse.julialang.org/') as p:
#     p.content.cookies.accept = 'no-3rdparty'

with config.pattern("*://google.com/") as p:
    p.content.media.audio_video_capture = True
    p.content.desktop_capture = True
with config.pattern("*://facebook.com/") as p:
    p.content.media.audio_video_capture = True
    p.content.desktop_capture = True

# # Duration (in milliseconds) to wait before removing finished downloads.
# # If set to -1, downloads are never removed.
# # Type: Int
c.downloads.remove_finished = 60000

# # Characters used for hint strings.
# # Type: UniqueCharString
# c.hints.chars = 'asdfghjkl'
c.hints.chars = "arstdhneio"

# # Languages to use for spell checking. You can check for available
# # languages and install dictionaries using scripts/dictcli.py. Run the
# # script with -h/--help for instructions.
# # Type: List of String
# # Valid values:
# #   - af-ZA: Afrikaans (South Africa)
# #   - bg-BG: Bulgarian (Bulgaria)
# #   - ca-ES: Catalan (Spain)
# #   - cs-CZ: Czech (Czech Republic)
# #   - da-DK: Danish (Denmark)
# #   - de-DE: German (Germany)
# #   - el-GR: Greek (Greece)
# #   - en-AU: English (Australia)
# #   - en-CA: English (Canada)
# #   - en-GB: English (United Kingdom)
# #   - en-US: English (United States)
# #   - es-ES: Spanish (Spain)
# #   - et-EE: Estonian (Estonia)
# #   - fa-IR: Farsi (Iran)
# #   - fo-FO: Faroese (Faroe Islands)
# #   - fr-FR: French (France)
# #   - he-IL: Hebrew (Israel)
# #   - hi-IN: Hindi (India)
# #   - hr-HR: Croatian (Croatia)
# #   - hu-HU: Hungarian (Hungary)
# #   - id-ID: Indonesian (Indonesia)
# #   - it-IT: Italian (Italy)
# #   - ko: Korean
# #   - lt-LT: Lithuanian (Lithuania)
# #   - lv-LV: Latvian (Latvia)
# #   - nb-NO: Norwegian (Norway)
# #   - nl-NL: Dutch (Netherlands)
# #   - pl-PL: Polish (Poland)
# #   - pt-BR: Portuguese (Brazil)
# #   - pt-PT: Portuguese (Portugal)
# #   - ro-RO: Romanian (Romania)
# #   - ru-RU: Russian (Russia)
# #   - sh: Serbo-Croatian
# #   - sk-SK: Slovak (Slovakia)
# #   - sl-SI: Slovenian (Slovenia)
# #   - sq: Albanian
# #   - sr: Serbian
# #   - sv-SE: Swedish (Sweden)
# #   - ta-IN: Tamil (India)
# #   - tg-TG: Tajik (Tajikistan)
# #   - tr-TR: Turkish (Turkey)
# #   - uk-UA: Ukrainian (Ukraine)
# #   - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = []
c.spellcheck.languages = ["en-US", "fr-FR"]

# # When to show the tab bar.
# # Type: String
# # Valid values:
# #   - always: Always show the tab bar.
# #   - never: Always hide the tab bar.
# #   - multiple: Hide the tab bar if only one tab is open.
# #   - switching: Show the tab bar when switching tabs.
c.tabs.show = "multiple"

# # Duration (in milliseconds) to show the tab bar before hiding it when
# # tabs.show is set to 'switching'.
# # Type: Int
# c.tabs.show_switching_delay = 800

# # Open a new window for every tab.
# # Type: Bool
c.tabs.tabs_are_windows = True

# # Default zoom level.
# # Type: Perc
# c.zoom.default = '100%'
# c.zoom.default = '125%'
c.zoom.default = "100%"

# # Bindings for normal mode
config.bind("J", "scroll-page 0 0.5")
config.bind("K", "scroll-page 0 -0.5")
config.bind("<Ctrl-Shift-d>", "tab-close -o")
config.bind("<Ctrl-d>", "tab-close")
config.bind("j", "scroll down")
config.bind("k", "scroll up")

# # Bindings for caret mode
config.bind("J", "scroll down", mode="caret")
config.bind("K", "scroll up", mode="caret")
config.bind("j", "move-to-next-line", mode="caret")
config.bind("k", "move-to-prev-line", mode="caret")

for mode in ["normal", "insert"]:
    config.bind(
        "<Ctrl-l>",
        "spawn --userscript qute-pass --mode gopass --prefix=websites --dmenu-invocation wmenu",
        mode=mode,
    )
    config.bind(
        "<Ctrl-u>",
        "spawn --userscript qute-pass --mode gopass --prefix=websites --dmenu-invocation wmenu --username-only",
        mode=mode,
    )
    config.bind(
        "<Ctrl-p>",
        "spawn --userscript qute-pass --mode gopass --prefix=websites --dmenu-invocation wmenu --password-only",
        mode=mode,
    )
    config.bind(
        "<Ctrl-o>",
        "spawn --userscript qute-pass --mode gopass --prefix=websites --dmenu-invocation wmenu --otp-only",
        mode=mode,
    )

# Start flavours
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Harmonic16 Dark scheme by Jannik Siebert (https://github.com/janniks)

base00 = "#0b1c2c"
base01 = "#223b54"
base02 = "#405c79"
base03 = "#627e99"
base04 = "#aabcce"
base05 = "#cbd6e2"
base06 = "#e5ebf1"
base07 = "#f7f9fb"
base08 = "#bf8b56"
base09 = "#bfbf56"
base0A = "#8bbf56"
base0B = "#56bf8b"
base0C = "#568bbf"
base0D = "#8b56bf"
base0E = "#bf568b"
base0F = "#bf5656"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base01

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base05

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base02

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base02

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base02

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base0B

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base0B

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg = base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base02

# Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base05

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base02

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base00

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base00

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base00

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base01

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base05

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base00

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base00

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base00

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base01

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base07

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base07

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base02

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base05

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base02

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base05

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base05

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base02

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base05

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base02

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = base00
# End flavours


import os.path

qutainer_config = config.configdir / "config.py"
if os.path.exists(qutainer_config) and qutainer_config != __file__:
    config.source(qutainer_config)
