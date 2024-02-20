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