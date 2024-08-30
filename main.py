def on_on_overlap(sprite, otherSprite):
    sprites.destroy(car_behind)
    sprites.destroy(incoming_car)
    music.play(music.melody_playable(music.knock),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.enemy, on_on_overlap)

def on_countdown_end():
    game.game_over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(incoming_car)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.UNTIL_DONE)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

incoming_car: Sprite = None
car_behind: Sprite = None
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999111111111119999999999999999999999999999999999999991111999999999999999999999999999999999999999999111111111111
        99999999999999999999999999999999999999999999999999991ddddddddd19999999999999999999999999991111199999991dd11999999999999999999999999999999999999999991dddddddddd1
        99999999999999999999999999999911111999999999999999991ddddddddd19999999999999999999999999991ddd199999991ddd1999999999999999999991111999999999999999991dddddddddd1
        9999999999999999999999999999911ddd1199999999999999991d11dddddd19999999999999999999999999111ddd111999911ddd1199999999999999999911dd1199999999999999991dd1d1ddddd1
        999999999999999999999999999911ddddd199999999999999991ddddddd1d199999999111999999111111191ddddddd199991ddddd19999999999999999111dddd199999999999999991dddddd11dd1
        99999911119999999999999999991dddddd199911199999999991ddddddddd1999999911d19999991ddddd191ddddddd199911ddddd119999999999999991dddddd199911119999999991dddddddddd1
        9999991dd19999999999999999991ddd1d119991d199999999991ddddddddd199999991dd19999991ddddd191ddddddd199911ddddd119999999999999991ddd1d119991dd19999999991dddd1ddddd1
        1111111dd19111111991111111111dddddd19111d111999999991ddddddd1d111111111dd19999991ddddd111d11dddd19111ddddddd11111991111111111dddddd19911dd11999999991ddddddd1dd1
        d11dddddd191d1dd1991ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd199999911dd1dd11ddddddd191dddddddddd1dd1991ddddddddddddd1d1111dddd1191111111dddddd11ddd
        dddd1dddd191dddd19911d1dd1ddddddddd111ddddd111dd1dd11ddddddddd11dddd1d1dd11111111dddddd11dd1dddd191ddddddddddddd1991dd1ddd1dddddddd1111dddd1191d11dd1ddddddddddd
        ddddddddd111dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11ddddddddddddddd191ddddddddddd1d1111dddddddddddddddd11dddddd111ddddddddddddddddd
        d11d1dddd1ddddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd1111ddddddd1ddd11dd1ddddddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddddddddd
        ddddddddd1ddddddd1dddddddddddddddddddd1dddddd11ddddddddddddddddddddddddddddd1ddd1ddddddddddddddd1d1ddddddddddddddd1dddddddddddddddddddddddddd1dddddddddddddddddd
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc
        11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
        11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
        11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        1111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd111
        111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbcbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d111d1111d111dd11dd
        d11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11d
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
        11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbccbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        cccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
        bccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccc
        ccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbb
        bbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddb
        bbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111dd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc
        dbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
car = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . 2 2 2 2 2 2 2 2 . . . . 
            . . . 2 4 2 2 2 2 2 2 c 2 . . . 
            . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
            . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
            . 2 c 2 e e e e e e e b c 4 2 2 
            . 2 2 e b b e b b b e e b 4 2 2 
            . 2 e b b b e b b b b e 2 2 2 2 
            . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
            . e e e e e e f e e e f e 2 d d 
            . e e e e e e f e e f e e e 2 d 
            . e e e e e e f f f e e e e e e 
            . e f f f f e e e e f f f e e e 
            . . f f f f f e e f f f f f e . 
            . . . f f f . . . . f f f f . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
car.set_stay_in_screen(True)
controller.move_sprite(car, 100, 100)
scroller.scroll_background_with_speed(-50, 0)
animation.run_image_animation(car,
    [img("""
            . . . . e e e e e . . . . . . . 
                . . . e 2 2 2 2 2 e e . . . . . 
                . . e 2 2 2 2 2 2 2 e e . . . . 
                . e b 4 2 2 2 2 2 4 9 e . . . . 
                e b 9 4 2 2 2 2 4 4 9 9 e e . . 
                e 9 9 4 2 2 2 4 4 4 9 9 2 2 e . 
                e 9 9 2 4 4 4 4 4 2 9 9 2 2 2 e 
                e 9 9 e e e e e e e 9 9 2 2 2 e 
                e 9 b e b e b b b e b 9 2 2 2 e 
                e b e b b e b b b b e e e e 2 e 
                e e e 2 2 e 2 2 2 2 e e 3 3 e e 
                e e e e e e e e e e e e e 3 3 e 
                e e e e e e e e e e e e e e e e 
                e e f f f e e e e f f f e e e e 
                . f c c b f e e f c c b f e e . 
                . . f b b . . . . f b b . . . .
        """),
        img("""
            . . . . e e e e e . . . . . . . 
                . . . e 2 2 2 2 2 e e . . . . . 
                . . e 2 2 2 2 2 2 2 e e . . . . 
                . e b 4 2 2 2 4 4 4 9 e . . . . 
                e b 9 4 2 2 4 4 4 4 9 9 e e . . 
                e 9 9 4 2 4 4 4 4 4 9 9 2 2 e . 
                e 9 9 2 4 4 4 4 4 2 9 9 2 2 2 e 
                e 9 9 e e e e e e e 9 9 2 2 2 e 
                e 9 b e b e b b b e b 9 2 2 2 e 
                e b e b b e b b b b e e e e 2 e 
                e e e 2 2 e 2 2 2 2 e e 3 3 e e 
                e e e e e e e e e e e e e 3 3 e 
                e e e e e e e e e e e e e e e e 
                e e f f f e e e e f f f e e e e 
                . f b f f f e e f b f f f e e . 
                . . b b c . . . . b b c . . . .
        """),
        img("""
            . . . . e e e e e . . . . . . . 
                . . . e 2 2 2 2 2 e e . . . . . 
                . . e 2 2 2 2 2 2 2 e e . . . . 
                . e b 4 4 4 2 2 2 4 9 e . . . . 
                e b 9 4 4 4 2 2 2 4 9 9 e e . . 
                e 9 9 4 4 2 2 2 4 4 9 9 2 2 e . 
                e 9 9 2 4 4 4 4 4 2 9 9 2 2 2 e 
                e 9 9 e e e e e e e 9 9 2 2 2 e 
                e 9 b e b e b b b e b 9 2 2 2 e 
                e b e b b e b b b b e e e e 2 e 
                e e e 2 2 e 2 2 2 2 e e 3 3 e e 
                e e e e e e e e e e e e e 3 3 e 
                e e e e e e e e e e e e e e e e 
                e e f f f e e e e f f f e e e e 
                . f b b c f e e f b b c f e e . 
                . . f f f . . . . f f f . . . .
        """),
        img("""
            . . . . e e e e e . . . . . . . 
                . . . e 2 2 2 2 2 e e . . . . . 
                . . e 2 2 2 2 2 2 2 e e . . . . 
                . e b 4 2 2 2 2 2 4 9 e . . . . 
                e b 9 4 2 2 2 2 2 4 9 9 e e . . 
                e 9 9 4 2 2 2 2 4 4 9 9 2 2 e . 
                e 9 9 2 4 4 4 4 4 2 9 9 2 2 2 e 
                e 9 9 e e e e e e e 9 9 2 2 2 e 
                e 9 b e b e b b b e b 9 2 2 2 e 
                e b e b b e b b b b e e e e 2 e 
                e e e 2 2 e 2 2 2 2 e e 3 3 e e 
                e e e e e e e e e e e e e 3 3 e 
                e e e e e e e e e e e e e e e e 
                e e f f f e e e e f f f e e e e 
                . f c b b f e e f c b b f e e . 
                . . f f c . . . . f f c . . . .
        """)],
    100,
    True)
info.start_countdown(15)
music.play(music.string_playable("C D E F G A B C5 ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_forever():
    global incoming_car
    incoming_car = sprites.create_projectile_from_side(img("""
            . . . . . . . 8 8 8 8 8 . . . . 
                    . . . . . 8 8 6 6 6 6 6 8 . . . 
                    . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                    . . . . 8 9 7 6 6 6 7 7 7 b 8 . 
                    . . 8 8 9 9 7 6 6 6 7 7 7 9 b 8 
                    . 8 6 6 9 9 7 7 6 6 6 7 7 9 9 8 
                    8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                    8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                    8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                    8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                    8 8 3 3 3 8 6 6 6 6 8 6 6 8 8 8 
                    8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 f f f 8 8 8 8 f f f 8 8 
                    . 8 8 f c b b f 8 8 f c b b f . 
                    . . . . f f f . . . . f f f . .
        """),
        -90,
        0)
    incoming_car.y = randint(15, 115)
    incoming_car.set_kind(SpriteKind.enemy)
    animation.run_image_animation(incoming_car,
        [img("""
                . . . . . . . 8 8 8 8 8 . . . . 
                        . . . . . 8 8 6 6 6 6 6 8 . . . 
                        . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                        . . . . 8 9 7 6 6 6 6 6 7 b 8 . 
                        . . 8 8 9 9 7 7 6 6 6 6 7 9 b 8 
                        . 8 6 6 9 9 7 7 7 6 6 6 7 9 9 8 
                        8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                        8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                        8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                        8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                        8 8 3 3 8 8 6 6 6 6 8 6 6 8 8 8 
                        8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 f f f 8 8 8 8 f f f 8 8 
                        . 8 8 f b c c f 8 8 f b c c f . 
                        . . . . b b f . . . . b b f . .
            """),
            img("""
                . . . . . . . 8 8 8 8 8 . . . . 
                        . . . . . 8 8 6 6 6 6 6 8 . . . 
                        . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                        . . . . 8 9 7 7 7 6 6 6 7 b 8 . 
                        . . 8 8 9 9 7 7 7 7 6 6 7 9 b 8 
                        . 8 6 6 9 9 7 7 7 7 7 6 7 9 9 8 
                        8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                        8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                        8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                        8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                        8 8 3 3 8 8 6 6 6 6 8 6 6 8 8 8 
                        8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 f f f 8 8 8 8 f f f 8 8 
                        . 8 8 f f f b f 8 8 f f f b f . 
                        . . . . c b b . . . . c b b . .
            """),
            img("""
                . . . . . . . 8 8 8 8 8 . . . . 
                        . . . . . 8 8 6 6 6 6 6 8 . . . 
                        . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                        . . . . 8 9 7 6 6 6 7 7 7 b 8 . 
                        . . 8 8 9 9 7 6 6 6 7 7 7 9 b 8 
                        . 8 6 6 9 9 7 7 6 6 6 7 7 9 9 8 
                        8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                        8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                        8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                        8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                        8 8 3 3 8 8 6 6 6 6 8 6 6 8 8 8 
                        8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 f f f 8 8 8 8 f f f 8 8 
                        . 8 8 f c b b f 8 8 f c b b f . 
                        . . . . f f f . . . . f f f . .
            """),
            img("""
                . . . . . . . 8 8 8 8 8 . . . . 
                        . . . . . 8 8 6 6 6 6 6 8 . . . 
                        . . . . 8 8 6 6 6 6 6 6 6 8 . . 
                        . . . . 8 9 7 6 6 6 6 6 7 b 8 . 
                        . . 8 8 9 9 7 6 6 6 6 6 7 9 b 8 
                        . 8 6 6 9 9 7 7 6 6 6 6 7 9 9 8 
                        8 6 6 6 9 9 6 7 7 7 7 7 6 9 9 8 
                        8 6 6 6 9 9 8 8 8 8 8 8 8 9 9 8 
                        8 6 6 6 9 b 8 b b b 8 b 8 b 9 8 
                        8 6 8 8 8 8 b b b b 8 b b 8 b 8 
                        8 8 3 3 8 8 6 6 6 6 8 6 6 8 8 8 
                        8 3 3 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 8 8 f f f 8 8 8 8 f f f 8 8 
                        . 8 8 f b b c f 8 8 f b b c f . 
                        . . . . c f f . . . . c f f . .
            """)],
        100,
        True)
    pause(2100)
forever(on_forever)

def on_forever2():
    global car_behind
    car_behind = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 6 6 6 6 6 6 6 6 . . . . 
                    . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                    . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                    . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                    . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                    . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                    . 6 8 b b b 8 b b b b 8 6 6 6 6 
                    . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                    . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                    . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                    . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                    . 8 f f f f 8 8 8 8 f f f 8 8 8 
                    . . f f f f f 8 8 f f f f f 8 . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        90,
        0)
    car_behind.y = randint(15, 115)
    car_behind.set_kind(SpriteKind.enemy)
    animation.run_image_animation(car_behind,
        [img("""
                . . . . 8 8 8 8 8 . . . . . . . 
                        . . . 8 6 6 6 6 6 8 8 . . . . . 
                        . . 8 6 6 6 6 6 6 6 8 8 . . . . 
                        . 8 b 7 6 6 6 6 6 7 9 8 . . . . 
                        8 b 9 7 6 6 6 6 7 7 9 9 8 8 . . 
                        8 9 9 7 6 6 6 7 7 7 9 9 6 6 8 . 
                        8 9 9 6 7 7 7 7 7 6 9 9 6 6 6 8 
                        8 9 9 8 8 8 8 8 8 8 9 9 6 6 6 8 
                        8 9 b 8 b 8 b b b 8 b 9 6 6 6 8 
                        8 b 8 b b 8 b b b b 8 8 8 8 6 8 
                        8 8 8 6 6 8 6 6 6 6 8 8 3 3 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 3 3 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 f f f 8 8 8 8 f f f 8 8 8 8 
                        . f c c b f 8 8 f c c b f 8 8 . 
                        . . f b b . . . . f b b . . . .
            """),
            img("""
                . . . . 8 8 8 8 8 . . . . . . . 
                        . . . 8 6 6 6 6 6 8 8 . . . . . 
                        . . 8 6 6 6 6 6 6 6 8 8 . . . . 
                        . 8 b 7 6 6 6 7 7 7 9 8 . . . . 
                        8 b 9 7 6 6 7 7 7 7 9 9 8 8 . . 
                        8 9 9 7 6 7 7 7 7 7 9 9 6 6 8 . 
                        8 9 9 6 7 7 7 7 7 6 9 9 6 6 6 8 
                        8 9 9 8 8 8 8 8 8 8 9 9 6 6 6 8 
                        8 9 b 8 b 8 b b b 8 b 9 6 6 6 8 
                        8 b 8 b b 8 b b b b 8 8 8 8 6 8 
                        8 8 8 6 6 8 6 6 6 6 8 8 3 3 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 3 3 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 f f f 8 8 8 8 f f f 8 8 8 8 
                        . f b f f f 8 8 f b f f f 8 8 . 
                        . . b b c . . . . b b c . . . .
            """),
            img("""
                . . . . 8 8 8 8 8 . . . . . . . 
                        . . . 8 6 6 6 6 6 8 8 . . . . . 
                        . . 8 6 6 6 6 6 6 6 8 8 . . . . 
                        . 8 b 7 7 7 6 6 6 7 9 8 . . . . 
                        8 b 9 7 7 7 6 6 6 7 9 9 8 8 . . 
                        8 9 9 7 7 6 6 6 7 7 9 9 6 6 8 . 
                        8 9 9 6 7 7 7 7 7 6 9 9 6 6 6 8 
                        8 9 9 8 8 8 8 8 8 8 9 9 6 6 6 8 
                        8 9 b 8 b 8 b b b 8 b 9 6 6 6 8 
                        8 b 8 b b 8 b b b b 8 8 8 8 6 8 
                        8 8 8 6 6 8 6 6 6 6 8 8 3 3 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 3 3 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 f f f 8 8 8 8 f f f 8 8 8 8 
                        . f b b c f 8 8 f b b c f 8 8 . 
                        . . f f f . . . . f f f . . . .
            """),
            img("""
                . . . . 8 8 8 8 8 . . . . . . . 
                        . . . 8 6 6 6 6 6 8 8 . . . . . 
                        . . 8 6 6 6 6 6 6 6 8 8 . . . . 
                        . 8 b 7 6 6 6 6 6 7 9 8 . . . . 
                        8 b 9 7 6 6 6 6 6 7 9 9 8 8 . . 
                        8 9 9 7 6 6 6 6 7 7 9 9 6 6 8 . 
                        8 9 9 6 7 7 7 7 7 6 9 9 6 6 6 8 
                        8 9 9 8 8 8 8 8 8 8 9 9 6 6 6 8 
                        8 9 b 8 b 8 b b b 8 b 9 6 6 6 8 
                        8 b 8 b b 8 b b b b 8 8 8 8 6 8 
                        8 8 8 6 6 8 6 6 6 6 8 8 3 3 8 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 3 3 8 
                        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                        8 8 f f f 8 8 8 8 f f f 8 8 8 8 
                        . f c b b f 8 8 f c b b f 8 8 . 
                        . . f f c . . . . f f c . . . .
            """)],
        100,
        True)
    pause(2100)
forever(on_forever2)
