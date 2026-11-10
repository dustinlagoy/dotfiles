## Shell Commands and Bash

For all shell commands use the bash tool in your path called `du`. Example:

```sh
du -c 'git clone example.org/repo'
```

### Avoiding Permission Prompts

Keep each `du -c '...'` command to one simple command. No `;`, `&&`, `|`, `$(...)`, backticks, `$VAR` or `>` redirects. If a task needs any of those, write a script and run it with `du <name>.sh`.

## Web Search and Web Page Downloading

Use the `trafilatura` tool in your path for all web search and web page access that will produce HTML output.

## Web Access

For direct web access that should not produce HTML output, use the `curl.sh` tool in your path.
