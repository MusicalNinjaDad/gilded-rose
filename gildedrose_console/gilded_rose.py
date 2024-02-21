# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            # Update sell_in first, so we know how old it is now
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.name.startswith("Conjured"):
                qualityincrement = 2
            elif item.name.startswith("Backstage pass"):
                qualityincrement = 1
                if item.sell_in < 11:
                    qualityincrement = 2
                if item.sell_in < 6:
                    qualityincrement = 3
                if item.sell_in < 0:
                    item.quality = 0
                    qualityincrement = 0
            elif item.name.startswith("Sulfuras"):
                qualityincrement = 0
            else:
                qualityincrement = 1

            if item.sell_in < 0:
                qualityincrement = qualityincrement * 2

            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality - qualityincrement
            else:
                item.quality = item.quality + qualityincrement

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

    def __eq__(self, _other) -> bool:
        try:
            equal = [
                all([
                    myitem.name == otheritem.name,
                    myitem.sell_in == otheritem.sell_in,
                    myitem.quality == otheritem.quality
                ])
                for myitem, otheritem in zip(self.items, _other.items)
            ]
        except AttributeError:
            return False
        return all(equal)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == "__main__":
    print("OMGHAI!")
    app = GildedRose(items=[
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=15,
            quality=20
        ),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6)
    ]
    )

    app.update_quality()
    input()
