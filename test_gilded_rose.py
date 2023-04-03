from gilded_rose import Item, Inventory


def test_standard_item_quality_decreases_by_one_each_day():
    items = [Item(name="foo", sell_in=10, quality=10)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 9


def test_standard_item_quality_decreases_twice_as_fast_after_sell_in_date():
    items = [Item(name="foo", sell_in=0, quality=10)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 8


def test_standard_item_quality_is_never_negative():
    items = [Item(name="foo", sell_in=10, quality=0)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 0


def test_aged_brie_increases_in_quality_each_day():
    items = [Item(name="Aged Brie", sell_in=10, quality=10)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 11


def test_aged_brie_quality_is_never_above_50():
    items = [Item(name="Aged Brie", sell_in=10, quality=50)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 50


def test_backstage_passes_increase_in_quality_each_day():
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 21


def test_backstage_passes_increase_twice_as_fast_when_sell_in_date_is_10_days_or_less():
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 22


def test_backstage_passes_increase_three_times_as_fast_when_sell_in_date_is_5_days_or_less():
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 23


def test_backstage_passes_quality_is_zero_after_sell_in_date():
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].quality == 0


def test_sulfuras_quality_and_sell_in_never_change():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
    inventory = Inventory(items)
    inventory.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80
