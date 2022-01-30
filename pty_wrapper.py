#!/usr/bin/env python3

# This is a wrapper around pty_driver.py that captures Ctrl+D and kills tuterm
# when it does. Tuterm is killed via simple IPC implemented via a file. A random
# file is created by tuterm and its path is passed to this process via a
# `__TUTERM_EVAL_FILE` environment variable. This process can write to this file
# any shell commands that should be sourced by tuterm when this process exits.

import os
import sys
import psutil
import pty
import signal

def kill_parent_shell():
    source_file = os.environ.get("__TUTERM_EVAL_FILE")
    if source_file:
        with open(source_file, "w", encoding="utf-8") as f:
            print('rm "$__TUTERM_EVAL_FILE"; exit 1', file=f)
    sys.exit(1)

def stdin_read(fd):
    data = os.read(fd, 1)
    if data == b"\x04":
        kill_parent_shell()
        return b""
    elif data == b"\x03":
        child = psutil.Process().children(recursive=False)[0]
        os.kill(child.pid, signal.SIGINT)
        return b""
    return data

def master_read(fd):
    data = os.read(fd, 1)
    if data == b"\x03":
        return b""
    return data

sys.argv[0] = os.path.dirname(os.path.abspath(__file__)) + "/pty_driver.py"
status = pty.spawn(["python3"] + sys.argv, master_read, stdin_read=stdin_read)

sys.exit(os.WEXITSTATUS(status))

