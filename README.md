<p align="center">
  <img src="https://user-images.githubusercontent.com/33803413/75342751-51913c00-5897-11ea-8022-5f6864f12a4d.png">
</p>

# Maze

A maze solver and generator.

## Usage

```
maze.py [-h] [-s | -g rows cols] [--pretty]
```

When neither `-s` nor `-g` option is given, `maze.py` prints the maze specified at input.

### Options

Option | Meaning |
--- | ---
`-h`, `--help` | Show help message and exit.
`-s`, `--solve` | Solve maze.
`-g rows cols`, `--generate rows cols` | Generate maze with specified size.
`--pretty` | Pretty-print the results.

### Syntax

A maze consist of `0`'s, `1`'s, and `2`'s, where `0` means an empty cell, `1` means a wall, and `2` is a cell, which is a part of the solution path.
The number of rows and columns should be odd.

#### Example

```
11111111111
10022222101
11121112222
10122210111
10111210001
12222211101
12111110101
12010000001
22111010111
10010010001
11111111111
```

## License

[MIT](https://github.com/wadiim/maze/blob/master/LICENSE)
