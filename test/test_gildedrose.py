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
        pytest.param(
            [Item(name="Conjured Mana Cake", sell_in=2, quality=1)],
            id="Conjured"
        ),
    ],
)
def test_qualitynevernegative(items):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality >= 0


@pytest.mark.parametrize(
    "items",
    [
        pytest.param(
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)],
            marks=pytest.mark.xfail(reason="Sulfuras quality always 80", strict=True),
            id="Sulfuras"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=2, quality=50)], 
            id="Aged Brie"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=-1, quality=50)],
            id="Aged Brie - overdue"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=50)],
            id="Backstage passes +3"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert",sell_in=8,quality=50)],
            id="Backstage passes +2"
        ),
        pytest.param(
            [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=18, quality=50)],
            id="Backstage passes +1"
        ),
    ],
)
def test_qualitymax50(items):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality <= 50


def test_conjured():
    gr = GildedRose(items=[Item(name="Conjured Mana Cake", sell_in=3, quality=6)])
    gr.update_quality()
    assert gr == GildedRose(
        items=[Item(name="Conjured Mana Cake", sell_in=2, quality=4)]
    )


@pytest.mark.parametrize(
    ("items", "expected_age"),
    [
        pytest.param(
            [Item(name="Aged Brie", sell_in=2, quality=10)], 
            11, 
            id="Sell in 2"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=0, quality=10)],
            12, 
            id="Sell in 0"
        ),
        pytest.param(
            [Item(name="Aged Brie", sell_in=-2, quality=10)], 
            12, 
            id="Sell in -2"
        ),
    ],
)
def test_agedbrieincreases(items, expected_age):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality == expected_age


@pytest.mark.parametrize(
    ("items", "expected_age"),
    [
        pytest.param(
            [Item(name="+5 Dexterity Vest", sell_in=0, quality=10)],
            8,
            id="Dex Vest sell in 0",
        ),
        pytest.param(
            [Item(name="+5 Dexterity Vest", sell_in=-1, quality=10)],
            8,
            id="Dex Vest sell in -1",
        ),
        pytest.param(
            [Item(name="Conjured Mana Cake", sell_in=0, quality=10)],
            6,
            id="conjured sell in 0",
        ),
        pytest.param(
            [Item(name="Conjured Mana Cake", sell_in=-1, quality=10)],
            6,
            id="conjured sell in -1",
        ),
    ],
)
def test_qualitychangesfaster(items, expected_age):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality == expected_age


@pytest.mark.parametrize(
    "items",
    [
        pytest.param(
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80)],
            id="Sell in 2",
        ),
        pytest.param(
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)],
            id="Sell in 0",
        ),
        pytest.param(
            [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-2, quality=80)],
            id="Sell in -2",
        ),
    ],
)
def test_sulfurasalways80(items):
    gr = GildedRose(items=items)
    gr.update_quality()
    assert gr.items[0].quality == 80


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
