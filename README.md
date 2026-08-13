# Gilded Rose refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/gilded-rose-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/gilded-rose-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Refactor the existing Gilded Rose implementation while preserving its
inventory behavior. Setup is complete when the characterization tests pass.

## Overview

This kata complements [Clean Code: SOLID Principles, Ep. 9 - The Single Responsibility Principle](https://cleancoders.com/episode/clean-code-episode-9).

This implementation of the Gilded Rose Kata in Python focuses on practicing the
Single Responsibility Principle (SRP). This kata aims to refactor the existing
code to ensure that each class or function has a single responsibility and that
code is easy to understand and maintain.

## Instructions

### Inventory

The Gilded Rose is a fictional inn that sells various goods. The quality of
these goods degrades as they approach their sell-by date, so the inn has a
system to update the inventory daily.

Each item in the inventory has a name, sell-in value (the number of days left
to sell the item), and quality value (how valuable the item is; never negative
or more than 50). Each day, the sell-in and quality values decrease by one, but
once the sell-by date has passed, an item's quality degrades twice as fast.

### Special item types

In addition to standard items, we have a few special item types:

- **Aged Brie**: The item "Aged Brie" increases in quality the older it gets.
- **Sulfuras**: The item "Sulfuras" is a legendary item that never has to be
  sold, and its quality is always 80.
- **Backstage passes**: The item "Backstage passes to ..." increases in quality
  faster as its sell-in value approaches: by 2 when there are ten days or fewer
  and by 3 when there are five days or fewer, but drops to 0 after the concert.
- **Conjured**: The item "Conjured" degrades in quality twice as fast as
  standard items.

### Code

The existing code violates the SRP principle by having a single `GildedRose`
class for managing the inventory of items and updating their quality. The class
has the following responsibilities:

- keep track of a list of `Item` objects;
- update the sell-in and quality values of each item;
- ensure that the quality of each item never goes below 0 or above 50;
- handle special cases for certain types of items (e.g., "Aged Brie,"
  "Backstage passes to a TAFKAL80ETC concert").

### Ideas for refactoring

- Introduce separate update methods for different types of items.
- Introduce a class responsible for updating the quality of an individual item.
- Introduce sub-types and use inheritance to handle special cases.
- Move the item creation logic to a separate class using the Factory design
  pattern.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/gilded-rose-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd gilded-rose-refactoring-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `11 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

Refactor `gilded_rose.py`. The existing behavior is covered by `test_gilded_rose.py`.

Run the tests after each change. Use Make when it is installed:

```console
make test
```

Otherwise, run pytest through `uv` directly:

```console
uv run pytest
```

Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
