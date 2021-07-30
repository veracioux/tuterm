DELAY='0.05s'
DELAY_SEP='0.2s'
DELAY_PROMPT='1s'

export TUTERM_CONFIG="$PWD/../config.sh"

prompt() {
    echo -ne "\e[$COLOR_CUSTOM_PROMPT"m'$ '"\e[$COLOR_CUSTOM_CMDLINE"m
}
