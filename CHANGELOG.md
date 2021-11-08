# Latest

## Fixes

- `fake_home` now checks number of arguments

# Version 0.3.0

## Features

- Added `SKIP` and `UNSKIP` for debugging
- Added `depends` API function
- Added `--progress` option (experimental)

## Fixes

- Enhanced safety of the `fake_home` function

# Version 0.2.0

## Features

- Improved behavior of tuterm called without arguments
- Improved evaluation of user input
- Better random home directory generation
- New API functions: `set_option`, `sleep`
- Script installation path now supports subdirectories
- Improved input (now uses readline)

## Fixes

- Fake home is now automatically created if it's not done by the script itself
- Fixed bug in script lookup when PREFIX is different from /usr
