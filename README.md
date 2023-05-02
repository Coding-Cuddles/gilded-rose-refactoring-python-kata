# Gilded Rose Refactoring Python Kata

[![Run on Replit](https://replit.com/badge/github/Coding-Cuddles/gilded-rose-refactoring-python-kata)](https://replit.com/new/github/Coding-Cuddles/gilded-rose-refactoring-python-kata)

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

  * **Aged Brie**: The item "Aged Brie" increases in quality the older it gets.
  * **Sulfuras**: The item "Sulfuras" is a legendary item that never has to be
    sold, and its quality is always 80.
  * **Backstage passes**. The item "Backstage passes to ..." increases in quality
    faster as its sell-in value approaches: by 2 when there are ten days or less
    and by 3 when there are five days or less, but drops to 0 after the concert.
  * **Conjured**: The item "Conjured" degrades in quality twice as fast as
    standard items.

### Code

The existing code violates the SRP principle by having a single `GildedRose`
class for managing the inventory of items and updating their quality. The class
has the following responsibilities:

  * keep track of a list of `Item` objects;
  * update the sell-in and quality values of each item;
  * ensure that the quality of each item never goes below 0 or above 50;
  * handle special cases for certain types of items (e.g., "Aged Brie,"
    "Backstage passes to a TAFKAL80ETC concert").

### Ideas for refactoring

* Introduce separate update methods for different types of items.
* Introduce a class responsible for updating the quality of an individual item.
* Introduce sub-types and use inheritance to handle special cases.
* Move the item creation logic to a separate class using the Factory design
  pattern.

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```
