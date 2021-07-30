There are two demos that we generate for the GitHub README. The main demo is run
as

```shell
./demo
```

The other demo is a demo of the available customizations. Each of the 3
customizations can be run by

```shell
./customized_git_demo N
```
replacing `N` with the number of the customization.

If you want to record the main demo so you can upload it to [ascinema.org](https://asciinema.org), run

```shell
./record_main
```

This will create the file `tuterm.cast`.

For the customization demo, run

```shell
./record_customized
```
It will create the file `customized_final.cast`.

The way this works is a bit complicated. First each customization gets recorded
and saved to its own asciicast file `customized<N>.cast`, sequentially. After
that, each of the casts gets replayed in its own `tmux` window. This gets
recorded again by asciinema.

The recording will be saved to the file `tuterm.cast`.

For the recordings to work, you must have `asciinema` and `tmux` installed.
While recording, do not interact with the terminal. All scripts must be run from
the current directory.
