import pyglet
import pyglet.gl
from pyglet import gl

#KONSTANTY OKNA
SIRKA = 1000
VYSKA = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST_LOPTY = 200 #pixely za sekundu

#PALKY
TLSTKA_PALKY = 10
VYSKA_PALKY = 100
RYCHLOST_PALKY = RYCHLOST_LOPTY * 1.5

#PROSTREDNA CIARA
CIARA_HRUBKA = 20

#FONT
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#STAVOVE PREMENEJ
pozicia_palok = [VYSKA//2,VYSKA//2]
pozicia_lopty = [SIRKA//2,VYSKA//2]
rychlost_lopty = [0,0]
stisnute_klavesy = set()
skore = [0,0]

def vykresli_obdlznik(x1,y1,x2,y2):

    # Tady pouzijeme volani OpenGL, ktere je pro nas zatim asi nejjednodussi
    # na pouziti
    gl.glBegin(gl.GL_TRIANGLE_FAN)  # zacni kreslit spojene trojuhelniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # u
"""
def pohyb_palok(tlacidlo):
    if tlacidlo == 'w':
        pozicia_palok[0] = pozicia_palok[0] + 10
    if tlacidlo == 's':
        pozicia_palok[0] = pozicia_palok[0] - 10
    if tlacidlo == 'o':
        pozicia_palok[1] = pozicia_palok[1] + 10
    if tlacidlo == 'l':
        pozicia_palok[1] = pozicia_palok[1] - 10

"""
def nakresli_text(text, x ,y, pozice_x):
    napis = pyglet.text.Label(text, font_size=VELKOST_FONTU, x=x, y=y, anchor_x=pozice_x)
    napis.draw()
def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)# smaz obsah okna
    gl.glColor3f(1, 1, 1) #biela farba kreslenia
    #vykresli loptu
    vykresli_obdlznik(
        pozicia_lopty[0] - VELKOST_LOPTY //2,
        pozicia_lopty[1] - VELKOST_LOPTY //2,
        pozicia_lopty[0] + VELKOST_LOPTY //2,
        pozicia_lopty[1] + VELKOST_LOPTY //2,
    )
    #vykreslit palky
    for x, y in [(0, pozicia_palok[0]), (SIRKA, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - TLSTKA_PALKY,
            y - VYSKA_PALKY//2,
            x + TLSTKA_PALKY,
            y + VYSKA_PALKY//2
        )

    #vykreslenie: poliacia ciara
    for y in range(CIARA_HRUBKA // 2, VYSKA, CIARA_HRUBKA * 2):
        vykresli_obdlznik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + CIARA_HRUBKA
        )
    #vykreslit score
    nakresli_text(str(skore[0]), x=ODSADENIE_TEXTU,y = VYSKA-ODSADENIE_TEXTU-VELKOST_FONTU, pozice_x='left')
    nakresli_text(str(skore[1]), x=SIRKA - ODSADENIE_TEXTU, y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU, pozice_x='right')


window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
   # on_text=pohyb_palok,

)



pyglet.app.run()