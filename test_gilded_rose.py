from gilded_rose import GildedRose, Item


def test_standard_item_quality_decreases_by_one_each_day():
    items = [Item(name="Milk", sell_in=5, quality=10)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 9


def test_standard_item_quality_decreases_twice_as_fast_after_sell_by_date():
    items = [Item(name="Milk", sell_in=0, quality=3)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 1


def test_standard_item_quality_is_never_negative():
    items = [Item(name="Milk", sell_in=0, quality=0)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 0


def test_aged_brie_quality_increases_by_one_each_day():
    items = [Item(name="Aged Brie", sell_in=10, quality=10)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 11


def test_aged_brie_quality_is_never_above_50():
    items = [Item(name="Aged Brie", sell_in=8, quality=50)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 50


def test_backstage_passes_quality_increases_by_one_each_day():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15,
             quality=20)
    ]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 21


def test_backstage_passes_quality_increases_by_2_when_sell_in_10_or_less():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10,
             quality=24)
    ]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 26


def test_backstage_passes_quality_increases_by_3_when_sell_in_5_or_less():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5,
             quality=33)
    ]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 36


def test_backstage_passes_quality_is_zero_after_sell_in_date():
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=0,
             quality=45)
    ]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 0


def test_sulfuras_quality_and_sell_in_never_change():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80


def test_quality_of_item_never_exceeds_50():
    items = [
        Item(name="Aged Brie", sell_in=10, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5,
             quality=49),
    ]
    inventory = GildedRose(items)
    inventory.update_quality()
    assert items[0].quality == 50
    assert items[1].quality == 50
