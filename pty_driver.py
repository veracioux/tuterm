#!/usr/bin/env python3

# NOTE: This module is only to be used by tuterm internally.

import argparse
import os
import pty
import sys
import time
import re
import subprocess as sp
from threading import Timer
import signal

signal.signal(signal.SIGINT, lambda _, __: sys.exit(1))

# ┏━━━━━━━━━━━┓
# ┃ Utilities ┃
# ┗━━━━━━━━━━━┛

class _Timer():
    def __init__(self, interval, function):
        self._timer = Timer(interval, function)

    def start(self):
        self._timer.start()

    def reset(self):
        self._timer.cancel()
        self._timer = Timer(self._timer.interval, self._timer.function)
        self._timer.start()

    def is_alive(self):
        return self._timer.is_alive()

def is_separator(char: str):
    return not re.match("[a-zA-Z0-9]", char)

# ┏━━━━━━━━━━┓
# ┃ Commands ┃
# ┗━━━━━━━━━━┛

def _print_expected(args):
    # Fill missing arguments with fallback values
    if not args.delay_sep:
        args.delay_sep = args.delay
    if not args.delay_prompt:
        args.delay_prompt = args.delay
    if args.fast:
        args.delay = args.delay_sep = args.delay_prompt = None
    # This delay is the timeout after which we consider that the shell has
    # finished writing its output to the PTY
    BASE_DELAY = 0.3 if os.path.basename(args.shell) == "fish" else 0.1

    class vars:
        already_printed = False

    def parent(child_pid, fd):
        def print_slowly():
            if vars.already_printed:
                return
            vars.already_printed = True
            print(f"\033[{args.color}m" if args.color else "\033[0m", end='')
            # Wait for a delay after the shell prompt is displayed
            if args.delay_prompt:
                sp.run(["sleep", args.delay_prompt])
            # Print the expected input in real time
            if not args.delay:
                print(args.expected, end='', flush=True)
            else:
                for char in args.expected:
                    print(char, end='', flush=True)
                    # Keeps track of remaining text in case a keyboard interrupt
                    # is received
                    args.expected = args.expected[1:]
                    sp.run(["sleep", args.delay_sep if is_separator(char) else args.delay])
            os.kill(child_pid, signal.SIGKILL)

        def interrupt(_, __):
            """Print remaining cmdline prompt on exit."""
            print(args.expected, flush=True)
            os.kill(os.getpid(), signal.SIGKILL)

        try:
            timer = _Timer(BASE_DELAY, print_slowly)
            signal.signal(signal.SIGINT, interrupt)
            # Print data coming from the child shell
            while data := os.read(fd, 1024):
                timer.reset()
                print(data.decode(), end='')
        except OSError:
            pass

    def child(pid, fd):
        _args = args.shell
        # TODO make this configurable?
        if os.path.basename(args.shell.split(" ", 1)[0]) == "fish":
            _args += " -C \"set fish_history ''\""
        sp.run(_args, shell=True)

    pid, fd = pty.fork()
    if pid == 0:
        child(pid, fd)
    else:
        parent(pid, fd)

def _evaluate(args):
    class vars:
        data = b""
    def stdin_read(fd):
        data = os.read(fd, 1)
        if data == b"\x7f":  # Backspace deletes one character
            vars.data = vars.data[:-1]
        elif data == b"\x1b":
            if os.read(fd, 1) == b"[" and os.read(fd, 1) == b"Z":
                print("\033[0;1m", args.expected, "\033[0m", sep="", end="")
                sys.exit(0)
            else:
                return "\u25A1".encode()
        elif data == b"\x03":
            sys.exit(1)
        elif data not in [b"\r", b"\n"]:
            vars.data += data
        else:
            if vars.data == args.expected.encode():
                sys.exit(0)
            sys.exit(1)
        return data
    pty.spawn(args.shell, stdin_read=stdin_read)

# ┏━━━━━━━━━━━━━━━━━━┓
# ┃ SETUP CLI PARSER ┃
# ┗━━━━━━━━━━━━━━━━━━┛

parser = argparse.ArgumentParser()
parser.add_argument("--shell")
parser.set_defaults(func=lambda _: print("You must specify a subcommand!", file=sys.stderr))
sub = parser.add_subparsers(title="commands", metavar="")
print_expected = sub.add_parser(
    "print_expected", help="Print shell prompt and the expected command"
)
evaluate = sub.add_parser(
    "evaluate", help=(
        "Print shell prompt and wait for the user to type the expected command"
    )
)

def add_common_options(parser):
    parser.add_argument("expected")
    parser.add_argument("--shell", default="bash")

# SETUP 'print_expected' command
add_common_options(print_expected)
print_expected.add_argument("--prompt", action="store_true", help="Display shell prompt")
print_expected.add_argument("--fast", action="store_true", help="Print the output without delay")
print_expected.add_argument("--delay", help="Delay between characters")
print_expected.add_argument("--delay-sep", help="Delay after separator characters")
print_expected.add_argument("--delay-prompt", help="Delay between prompt and expected command")
print_expected.add_argument("--color", help="Color of the printed command")
print_expected.set_defaults(func=_print_expected)
# SETUP 'evaluate' command
add_common_options(evaluate)
evaluate.set_defaults(func=_evaluate)

args = parser.parse_args()

args.func(args)
