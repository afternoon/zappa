# Zappa

A simple, general purpose functional language.

- Small, simple, expressive language which enforces good style
- Compiled with LLVM
- Statically-typed with type inference

## Syntax

| Expression                  | Example                                         |
| --------------------------- | ----------------------------------------------- |
| Identifiers                 | `foo`, `toString`, `foo?`, `save!`              |
| Type identifiers            | `Int`, `Bool`, `String`, `Date`, `List`         |
| Integers                    | `1`, `2`, `274,877,906,944`                     |
| Float, decimal, hex, octal  | `99.99`, `0d99.99`, `0xff`, `0o777`             |
| Strings                     | `"Hello"`                                       |
| Characters                  | `'x'`                                           |
| Booleans                    | `true`, `false`                                 |
| Arithmetic expressions      | `99 + 1 - 50`                                   |
| Lists                       | `[1, 2, 3]`                                     |
| List, string append         | `[1, 2] ++ [3, 4]`, `"Hello " ++ "World!"`      |
| String interpolation        | `"Hello ${object}!"`                            |
| Records                     | `{name: "Zappa", version: 1}`                   |
| Record access               | `foo.bar`                                       |
| Record update               | `{ person | name = "George" }`                  |
| Boolean expressions         | `a == b`, `a != b`, `a <= b`                    |
| Binding                     | `x = 99 + 1`                                    |
| Functions                   | `square x = x * x`                              |
| Anonymous functions         | `(x) -> x * x`                                  |
| Conditional expressions     | `if a == b then 1 else 0`                       |
| Pattern matching            | `case list.head l of`...                        |
| Type declarations           | `type Point3D = {x: Float, y: Float, z: Float}` |
| Modules                     | `module things`                                 |
| Import                      | `import things`                                 |
| Comments                    | `-- Watch out where the huskies go`             |

## `zappa` command line tool

### REPL

```sh
$ zappa repl
```

### Building

Compile everything in the current directory (recursively) into a single binary:

```sh
$ zappa build
```

Build a single file:

```sh
$ zappa build foo.zp
```

### Package manager

Packages are installed from GitHub and identified by user and repo name.

Install a new package, and record it in `zappa-package.json`:

```sh
$ zappa package install afternoon/blah
```
