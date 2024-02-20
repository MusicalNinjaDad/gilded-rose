import pytest
from gildedrose_console.gilded_rose import GildedRose, Item

@pytest.mark.parametrize(
    "items",
    [
        pytest.param(
            [Item(name="+5 Dexterity Vest", sell_in=10, quality=0)], 
            id="Normal"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=2, quality=0)],
            id="Aged Brie"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=0)],
            id="Backstage passes"
        ),
    ]
)
def test_qualitynevernegative(items):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality >= 0

@pytest.mark.parametrize(
    "items",
    [
        pytest.param(
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            marks=pytest.mark.xfail(reason="Sulfuras quality always 80"), 
            id="Sulfuras"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=2, quality=50)],
            id="Aged Brie"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=50)],
            id="Backstage passes +3"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=50)],
            id="Backstage passes +2"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=18, quality=50)],
            id="Backstage passes +1"
        ),
    ]
)
def test_qualitymax50(items):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality <= 50

@pytest.mark.xfail
def test_conjured():
    gr = GildedRose(items=[
            Item(name="Conjured Mana Cake", sell_in=3, quality=6)
        ])
    gr.update_quality()
    assert gr == GildedRose(items=[
            Item(name="Conjured Mana Cake", sell_in=3, quality=4)
        ]) 