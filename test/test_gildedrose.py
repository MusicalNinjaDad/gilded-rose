import pytest
from gildedrose_console.gilded_rose import GildedRose, Item

@pytest.mark.parametrize(
    ("items","expected_quality"),
    [
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10)],
            11,
            id="Sell in 20"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=10)],
            12,
            id="Sell in 11"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)],
            12,
            id="Sell in 10"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=10)],
            13,
            id="Sell in 6"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)],
            13,
            id="Sell in 5"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10)],
            13,
            id="Sell in 1"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)],
            0,
            id="Sell in 0"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=10)],
            0,
            id="Sell in -1"
        ),
    ]
)
def test_backstagepasses(items, expected_quality):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality == expected_quality