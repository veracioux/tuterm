DELAY=0.02
DELAY_SEP=0.08
DELAY_PROMPT=0.6
COLOR_CMDLINE='1;33'
COLOR_WARNING='1;91'
COLOR_MESSAGE='1;32'
TUTERM_SHELL='bash'

# Custom command line prompt (used if TUTERM_SHELL is unset)
prompt() {
    echo -n "$TUTERM_NAME \$ "
}

# vim: filetype=bash
