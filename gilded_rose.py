class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


class GildedRose:

    def __init__(self):
        self.items = []

    def add_item(self, name, sell_in, quality):
        self.items.append(Item(name, sell_in, quality))

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality -= 1

            else:
                if item.quality < 50:
                    item.quality += 1

                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality += 1

                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality += 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1
