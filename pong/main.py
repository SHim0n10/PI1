import pyglet
import pyglet.gl
from pyglet import gl
import random
from pyglet.window import key
from pyglet.window import Window

#KONSTANTY OKNA
SIRKA = 1000
VYSKA = 700

#lopta
VELKOST_LOPTY = 20
RYCHLOST_LOPTY = 500 #pixely za sekundu

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
stisknute_klavesy = set()
skore = [0, 0]
matchpoint = [0]
mozne_hrat = [1]
mozne_kreslit = [1]
vyhra_hrac = [0]

def reset():
    pozicia_lopty[0] = SIRKA//2
    pozicia_lopty[1] = VYSKA//2

    #x-ova rychlost
    if random.randint(0,1):
        rychlost_lopty[0] = RYCHLOST_LOPTY
    else:
        rychlost_lopty[0] = -RYCHLOST_LOPTY

    #y-ova rychlost
    rychlost_lopty[1] = random.uniform(-1,1) * RYCHLOST_LOPTY

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

def nakresli_text(text, x ,y, pozice_x):
    napis = pyglet.text.Label(text, font_size=VELKOST_FONTU, x=x, y=y, anchor_x=pozice_x)
    napis.draw()

def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.add(("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.add(("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(("dole", 1))
    if symbol == key.P:
        mozne_hrat[0] = 0

def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.discard(("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(("dole", 1))
    if symbol == key.P:
        mozne_hrat[0] = 1

def vykresli():
    if mozne_kreslit[0] == 1:
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
        if matchpoint[0] == 1:
            nakresli_text("MATCHPOINT", x=SIRKA//2, y=VYSKA//2, pozice_x="center")
        if matchpoint[0] == 2:
            nakresli_text("LAST ROUND", x=SIRKA//2, y=VYSKA//2, pozice_x="center")
        if mozne_hrat[0] == 0:
            vykresli_obdlznik(
                SIRKA//2 - 20,
                VYSKA//2 - 20,
                SIRKA//2 - 10,
                VYSKA//2 + 20
            )
            vykresli_obdlznik(
                SIRKA//2 + 10,
                VYSKA//2 - 20,
                SIRKA//2 + 20,
                VYSKA//2 + 20
            )
    else:
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glColor3f(1, 1, 1)
        if vyhra_hrac[0] == 1:
            nakresli_text("VYHRAL HRAC 1", x=SIRKA//2,y = VYSKA//2, pozice_x='center')
        elif vyhra_hrac[0] == 2:
            nakresli_text("VYHRAL HRAC 2", x=SIRKA//2,y = VYSKA//2, pozice_x='center')


def obnov_stav(dt):
    if mozne_hrat[0] == 1:
        #pohyb palok
        for cislo_palky in (0,1):
            if ("hore", cislo_palky) in stisknute_klavesy:
                pozicia_palok[cislo_palky] += RYCHLOST_PALKY * dt
            if ("dole", cislo_palky) in stisknute_klavesy:
                pozicia_palok[cislo_palky] -= RYCHLOST_PALKY * dt
        #dolna zarazka
            if pozicia_palok[cislo_palky] < VYSKA_PALKY /2:
                pozicia_palok[cislo_palky] = VYSKA_PALKY /2
            if pozicia_palok[cislo_palky] > VYSKA - VYSKA_PALKY /2:
                pozicia_palok[cislo_palky] = VYSKA - VYSKA_PALKY /2

        # pohyb lopty
        pozicia_lopty[0] += rychlost_lopty[0] * dt
        pozicia_lopty[1] += rychlost_lopty[1] * dt

        #odrazenie lopty
        if pozicia_lopty[1] < VELKOST_LOPTY //2:
            rychlost_lopty[1] = abs(rychlost_lopty[1])
        if pozicia_lopty[1] > VYSKA - VELKOST_LOPTY //2:
            rychlost_lopty[1] = -abs(rychlost_lopty[1])
        #zistenie borderov palky
        palka_min = pozicia_lopty[1] - VELKOST_LOPTY / 2 - VYSKA_PALKY / 2
        palka_max = pozicia_lopty[1] + VELKOST_LOPTY / 2 + VYSKA_PALKY / 2
        polka_palky = pozicia_lopty[1]

        # odraz zlava
        if pozicia_lopty[0] < TLSTKA_PALKY + VELKOST_LOPTY / 2:
            if palka_min < pozicia_palok[0] < polka_palky:
                #odrazenie lopty
                #horna polka
                rychlost_lopty[0] = abs(rychlost_lopty[0])
                rychlost_lopty[1] = random.uniform(0,1) * RYCHLOST_LOPTY
                
            elif polka_palky < pozicia_palok[0] <palka_max:
                #dolna polka
                rychlost_lopty[0] = abs(rychlost_lopty[0])
                rychlost_lopty[1] = random.uniform(-1,0) * RYCHLOST_LOPTY
            #palka je inde ako lopta, hrac prehral
            else:
                skore[1] += 1
                reset()
        #odraz zprava
        if pozicia_lopty[0] > SIRKA - VELKOST_LOPTY / 2:
            if palka_min < pozicia_palok[1] < polka_palky:
                #odrazenie lopty
                rychlost_lopty[0] = -abs(rychlost_lopty[0])
                rychlost_lopty[1] = random.uniform(0,1) * RYCHLOST_LOPTY
            elif polka_palky< pozicia_palok[1] < palka_max:
                rychlost_lopty[0] = -abs(rychlost_lopty[0])
                rychlost_lopty[1] = random.uniform(-1,0) * RYCHLOST_LOPTY
                #palka je inde ako lopta, hrac prehral
            else:
                skore[0] += 1
                reset()
        if skore[0] > 10:
            vyhra_hrac[0] = 1
            mozne_hrat[0] = 0
            mozne_kreslit[0] = 0
        if skore[1] > 10:
            vyhra_hrac[0] = 2
            mozne_hrat[0] = 0
            mozne_kreslit[0] = 0
        if skore[0] == 10:
            matchpoint[0] = 1
        if skore[1] == 10:
            matchpoint[0] = 1
        if skore[0] == 10:
            if skore[1] ==10:
                matchpoint[0] = 2

reset()



window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice,
)
pyglet.clock.schedule(obnov_stav)



pyglet.app.run()