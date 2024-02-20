import pytest
from gildedrose_console.gilded_rose import GildedRose, Item

@pytest.fixture
def app():
    return GildedRose(items = [
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

@pytest.fixture
def expected():
    return GildedRose(items = [
            Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
            Item(name="Aged Brie", sell_in=1, quality=1),
            Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", 
                sell_in=14, 
                quality=21
                ),
            Item(name="Conjured Mana Cake", sell_in=2, quality=4)
        ]
)

def test_everything(app, expected):
# Well almost ... we're not checking running from console here ...
    app.update_quality()

    assert app == expected

def test_inequality(app, expected):
    assert app != expected