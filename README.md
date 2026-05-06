# 🐔 Chicken Language

**Chicken Language** is a tiny, chicken-themed esoteric programming
language implemented in Python.\
It's inspired by tape-based languages like Brainfuck, but replaces
symbols with poultry.

------------------------------------------------------------------------

## Overview

Chicken Language operates on a **linear memory tape** of cells and a
**pointer** that moves across them.

-   Each cell stores an integer (starts at `0`)
-   The pointer selects the "current" cell
-   Commands modify values, move the pointer, or control execution flow

Think: **Brainfuck, but with chickens and slightly more readable
commands**

------------------------------------------------------------------------

## Running Programs

``` bash
python main.py program.bok
```

Programs use the `.bok` file extension.

------------------------------------------------------------------------

## Language Semantics

### Memory Model

-   Tape size: **30,000 cells**
-   Each cell stores an integer
-   All cells start at `0`
-   A pointer tracks the current cell

------------------------------------------------------------------------

## Core Commands

### Value Manipulation

  Command                  Description
  ------------------------ ---------------------------------
  `bok`                    Increment current cell
  `peck`                   Decrement current cell
  `hatch`                  Reset current cell to `0`
  `lay N`                  Set current cell to integer `N`
  `feed cluck cluck ...`   Set value to number of `cluck`s

------------------------------------------------------------------------

### Pointer Movement

  Command     Description
  ----------- --------------------
  `strut`     Move pointer right
  `shuffle`   Move pointer left

------------------------------------------------------------------------

### Output

  Command     Description
  ----------- ---------------------------------------
  `cluck`     Print current cell as number
  `crow`      Print current cell as ASCII character
  `crack`     Print newline
  `scratch`   Debug info (pointer, value, labels)

------------------------------------------------------------------------

## Control Flow

Chicken Language uses **block-based control flow** with:

    coop ... roost

### Loops

  Command            Description
  ------------------ -----------------------------
  `coop ... roost`   Loop while current cell ≠ 0

------------------------------------------------------------------------

### Conditionals

  Command              Description
  -------------------- -------------------------
  `ifcoop ... roost`   Run if current cell ≠ 0
  `ifzero ... roost`   Run if current cell = 0

------------------------------------------------------------------------

## Labels & Named Cells

Unlike raw Brainfuck, Chicken Language lets you name memory locations.

  Command       Description
  ------------- ------------------------------------------
  `nest name`   Assign current pointer position to label
  `roam name`   Move pointer to that label

------------------------------------------------------------------------

## Syntax Rules

-   Commands are separated by whitespace
-   One command per line is recommended (but not required)
-   Comments start with `#`

------------------------------------------------------------------------

## 🐣 Hello Example

``` bok
# prints "Hello"

lay 72 crow
lay 101 crow
lay 108 crow
lay 108 crow
lay 111 crow
crack
```

------------------------------------------------------------------------

## 🐓 Final Words

> If it compiles, it clucks.
