import pyglet
import math
window = pyglet.window.Window(width=1000,height=1000)

def tik(t):
    had.x = had.x + t * 20
    had.y = had.y + 20 * math.sin(had.x / 5)
    #had.rotation = 250

def zpracuj_text(text):
    had.x = 150

def vykresli():
    window.clear()
    had.draw()

obrazok = pyglet.image.load('snake.jpg')
had = pyglet.sprite.Sprite(obrazok)
obrazok1 = pyglet.image.load('snake2.png')

def zmen(t):
    had.image = obrazok1
    pyglet.clock.schedule_once(zmen_nazad, 3)

def zmen_nazad(t):
    had.image = obrazok
    pyglet.clock.schedule_once(zmen, 3)


pyglet.clock.schedule_once(zmen, 3)


def klik(x,y,tlacitko,mod):
    had.x = x
    had.y = y
    print(x)
    print(y)
    print(tlacitko)
    print(mod)



window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik
)
pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()