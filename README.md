<h1 align="center">tuterm</h1>

<p align="center">
  <a href="https://aur.archlinux.org/packages/tuterm/"> <img src="https://img.shields.io/aur/version/tuterm?label=AUR" alt="AUR"/> </a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-blueviolet" alt="License"/></a>
</p>
<p align="center">
  <a href="https://asciinema.org/a/427932" target="_blank">
    <img src="https://gist.github.com/HarisGusic/66336d488e8d87c7b3fb696c5dbd93d1/raw/4b8bc0b043faf166abc92e12fc0bfb5acea55345/tuterm-demo.svg" />
  </a>
</p>

**UNDER CONSTRUCTION:** [A collection of tutorials for your favorite CLI programs][collection]

Tuterm is a framework for running and creating real-time interactive tutorials
and demonstrations of CLI programs.

Key features:

**For users**
* Ridiculously easy to use
* Step by step instructions
* Learn at your own pace
* No mistakes possible
* Customizable colors, delays and prompts

<p align="center">
  <a href="https://asciinema.org/a/428011" target="_blank">
    <img src="https://gist.github.com/HarisGusic/66336d488e8d87c7b3fb696c5dbd93d1/raw/6b79b61de44e11e561c67b8f91446f14895e85ae/tuterm-customization-demo.svg" />
  </a>
</p>

**For tutorial creators**
* Nothing more than a bash extension
* Create interactive tutorials and non-interactive demos with the same code
* Simple framework and minimalistic design
* Well documented
* Doesn't reinvent the wheel
* 100% repeatable

# Example

The following script defines a short tutorial/demo for the command `ls`.
```bash
# file: ls_tutorial
configure() {
    DELAY=0.09
    DELAY_SEP=0.12
    DELAY_PROMPT=1.5
    COLOR_MESSAGE='1;32'
}

fake_home

run() {
    mkdir dir
    touch file1 file2 .file3 dir/file
    M "Let's just run the command."
    cmdline ls
    M "The -a option shows hidden files."
    # c is an alias for cmdline
    c ls -a
    M "The -R option recurses into directories"
    c ls -R
    M "You can also see the file modes"
    c ls -l
}
```
This script is run as:
```shell
tuterm ls_tutorial --mode MODE
```
There are two supported MODEs: tutorial and demo. Demo mode types out the
commands in real time just like a human would. Tutorial mode shows the user what
to type and then waits for them to type it, correcting any mistakes.

Demo mode is great for creating terminal recordings. The video below was
generated using asciinema:

```shell
asciinema rec -c 'tuterm ls_tutorial --mode demo' ls_tutorial.cast
```

<p align="center">
  <a href="https://asciinema.org/a/XT938YRCtcrPAhnCkd5H6MsS4" target="_blank">
    <img src="https://gist.github.com/HarisGusic/66336d488e8d87c7b3fb696c5dbd93d1/raw/4b8bc0b043faf166abc92e12fc0bfb5acea55345/tuterm-example-ls.svg" />
  </a>
</p>

# Installation

After cloning this repository or downloading the source code, simply run

```shell
make install
```
(You may need to use `sudo`)

This will install tuterm under `/usr/local`. You can change this by setting `PREFIX=/your/path/of/choice`.

# Documentation

Everything is documented inside the man page that is installed with tuterm.

# Contributing

Please, feel free to report any issues or feature requests [here][issues].
But before you do that, have a look at [TODO](./TODO.org).
(this file will steadily dissolve into GitHub issues)

If you want to submit a bug fix, you can simply open a pull request. But if you
want to add a new feature, open an issue so we can discuss it first.

Everyone is welcome to contribute.

*A note: Tuterm is a simple program, so most issues or features should be a good choice for a beginner.*

[collection]: https://github.com/HarisGusic/tuterm-collection
[issues]: https://github.com/HarisGusic/tuterm/issues
