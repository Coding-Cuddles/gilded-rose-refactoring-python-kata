import pytest

from gilded_rose import GildedRose


@pytest.fixture
def inn():
    return GildedRose()


def test_standard_item_quality_decreases_by_one_each_day(inn):
    inn.add_item("Milk", 5, 10)
    inn.update_quality()

    assert inn.items[0].quality == 9


def test_standard_item_quality_decreases_twice_as_fast_after_sell_by_date(inn):
    inn.add_item("Milk", 0, 3)
    inn.update_quality()

    assert inn.items[0].quality == 1


def test_standard_item_quality_is_never_negative(inn):
    inn.add_item("Milk", 0, 0)
    inn.update_quality()

    assert inn.items[0].quality == 0


def test_aged_brie_quality_increases_by_one_each_day(inn):
    inn.add_item("Aged Brie", 10, 10)
    inn.update_quality()

    assert inn.items[0].quality == 11


def test_aged_brie_quality_is_never_above_50(inn):
    inn.add_item("Aged Brie", 8, 50)
    inn.update_quality()

    assert inn.items[0].quality == 50


def test_backstage_passes_quality_increases_by_one_each_day(inn):
    inn.add_item("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    inn.update_quality()

    assert inn.items[0].quality == 21


def test_backstage_passes_quality_increases_by_2_when_sell_in_10_or_less(inn):
    inn.add_item("Backstage passes to a TAFKAL80ETC concert", 10, 24)
    inn.update_quality()

    assert inn.items[0].quality == 26


def test_backstage_passes_quality_increases_by_3_when_sell_in_5_or_less(inn):
    inn.add_item("Backstage passes to a TAFKAL80ETC concert", 5, 33)
    inn.update_quality()

    assert inn.items[0].quality == 36


def test_backstage_passes_quality_is_zero_after_sell_in_date(inn):
    inn.add_item("Backstage passes to a TAFKAL80ETC concert", 0, 45)
    inn.update_quality()

    assert inn.items[0].quality == 0


def test_sulfuras_quality_and_sell_in_never_change(inn):
    inn.add_item("Sulfuras, Hand of Ragnaros", 10, 80)
    inn.update_quality()

    assert inn.items[0].sell_in == 10
    assert inn.items[0].quality == 80


def test_quality_of_item_never_exceeds_50(inn):
    inn.add_item("Aged Brie", 10, 50)
    inn.add_item("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    inn.update_quality()

    assert inn.items[0].quality == 50
    assert inn.items[1].quality == 50
