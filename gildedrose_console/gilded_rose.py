# -*- coding: utf-8 -*-

from collections import defaultdict


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        def calculate_backstagepass(s, q):
            qualityincrement = 1
            if s < 11:
                qualityincrement = 2
            if s < 6:
                qualityincrement = 3
            if s < 0:
                qualityincrement = -q
            return q + qualityincrement

        specific_calculators = {
            "Conjured": lambda s, q: q - (2 if s >= 0 else 4),
            "Sulfuras": lambda s, q: q,
            "Aged Brie": lambda s, q: q + (1 if s >= 0 else 2),
            "Backstage pass": calculate_backstagepass,
        }

        def default_calculator(s, q):
            return q - (1 if s >= 0 else 2)

        for item in self.items:

            # Update sell_in first, so we know how old it is now
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            for itemtype, calculator in specific_calculators.items():
                if item.name.startswith(itemtype):
                    item.quality = calculator(item.sell_in, item.quality)
                    break
            else:
                item.quality = default_calculator(item.sell_in, item.quality)

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50

    def __eq__(self, _other) -> bool:
        try:
            equal = [
                all(
                    [
                        myitem.name == otheritem.name,
                        myitem.sell_in == otheritem.sell_in,
                        myitem.quality == otheritem.quality,
                    ]
                )
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
    app = GildedRose(
        items=[
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]
    )

    app.update_quality()
    input()
