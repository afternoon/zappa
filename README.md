# Zappa

A simple, general purpose functional language.

- Small, simple, expressive language which enforces good style
- Compiled with LLVM
- Statically-typed with type inference

## Syntax

<table>
  <thead>
    <tr>
      <th>Expression</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Identifiers</td>
      <td><code>foo</code>, <code>toString</code>, <code>foo?</code>, <code>save!</code></td>
    </tr>
    <tr>
      <td>Type identifiers</td>
      <td><code>Int</code>, <code>Bool</code>, <code>String</code>, <code>Date</code>, <code>List</code></td>
    </tr>
    <tr>
      <td>Integers</td>
      <td><code>1</code>, <code>2</code>, <code>274,877,906,944</code></td>
    </tr>
    <tr>
      <td>Float, decimal, hex, octal</td>
      <td><code>99.99</code>, <code>0d99.99</code>, <code>0xff</code>, <code>0o777</code></td>
    </tr>
    <tr>
      <td>Strings</td>
      <td><code>"Hello"</code></td>
    </tr>
    <tr>
      <td>Characters</td>
      <td><code>'x'</code></td>
    </tr>
    <tr>
      <td>Booleans</td>
      <td><code>true</code>, <code>false</code></td>
    </tr>
    <tr>
      <td>Arithmetic expressions</td>
      <td><code>99 + 1 - 50</code></td>
    </tr>
    <tr>
      <td>Lists</td>
      <td><code>[1, 2, 3]</code></td>
    </tr>
    <tr>
      <td>List, string append</td>
      <td><code>[1, 2] ++ [3, 4]</code>, <code>"Hello " ++ "World!"</code></td>
    </tr>
    <tr>
      <td>String interpolation</td>
      <td><code>"Hello ${object}!"</code></td>
    </tr>
    <tr>
      <td>Records</td>
      <td><code>{name: "Zappa", version: 1}</code></td>
    </tr>
    <tr>
      <td>Record access</td>
      <td><code>foo.bar</code></td>
    </tr>
    <tr>
      <td>Record update</td>
      <td><code>{ person | name = "George" }</code></td>
    </tr>
    <tr>
      <td>Boolean expressions</td>
      <td><code>a == b</code>, <code>a != b</code>, <code>a &lt;= b</code></td>
    </tr>
    <tr>
      <td>Binding</td>
      <td><code>x = 99 + 1</code></td>
    </tr>
    <tr>
      <td>Functions</td>
      <td><code>square x = x * x</code></td>
    </tr>
    <tr>
      <td>Anonymous functions</td>
      <td><code>(x) -&gt; x * x</code></td>
    </tr>
    <tr>
      <td>Conditional expressions</td>
      <td><code>if a == b then 1 else 0</code></td>
    </tr>
    <tr>
      <td>Pattern matching</td>
      <td>
        <pre>case head l of
  Just x -> "head is ${x}"
  Nothing -> "list empty"</pre>
      </td>
    </tr>
    <tr>
      <td>Type declarations</td>
      <td><code>type Point3D = {x: Float, y: Float, z: Float}</code></td>
    </tr>
    <tr>
      <td>Modules</td>
      <td><code>module things</code></td>
    </tr>
    <tr>
      <td>Import</td>
      <td><code>import things</code></td>
    </tr>
    <tr>
      <td>Comments</td>
      <td><code>-- Watch out where the huskies go</code></td>
    </tr>
  </tbody>
</table>

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
