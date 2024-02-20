from gildedrose_console.gilded_rose import GildedRose, Item

def test_everything():
# Well almost ... we're not checking running from console here ...
    app = GildedRose(items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(
                 name="Backstage passes to a TAFKAL80ETC concert", 
                 sell_in=15, 
                 quality=20
                 )
            ]
    )
    expected = GildedRose(items = [
             Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
             Item(name="Aged Brie", sell_in=1, quality=1),
             Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(
                 name="Backstage passes to a TAFKAL80ETC concert", 
                 sell_in=14, 
                 quality=21
                 )
            ]
    )
    for appitem, expecteditem in zip(app.items, expected.items):
        assert appitem.name == expecteditem.name
        assert appitem.sell_in == expecteditem.sell_in
        assert appitem.quality == expecteditem.quality
 
    # app.update_quality()