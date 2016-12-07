# Zappa Language Specification

Just some notes for now.

## Opinionated to make code more readable

- Only camel-case identifiers allowed
  - Legal: `calculateThings`
  - Illegal: `calculate_things`, `calculate-things`
  - `CalculateThings` is a type identifier
- Functions with `?` suffix must return `Bool`, e.g. `foo? a = "FOO! " ++ a` is
  illegal
- Spaces, not tabs

### Optional

- Suffix function names with `!` to indicate destructive side-effects, e.g.
  `doThings!`

### Allowed, but poor style

- Prefer `things` to `getThings`

## Error handling

If your computation might result in an error, return a `Maybe`. Zappa does not
have exceptions.
