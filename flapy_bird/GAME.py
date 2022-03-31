import pyglet
from pyglet import gl
from pyglet.window import key
from random import *


#OKNO
SIRKA = 925
VYSKA = 500

RYCHLOST = 0

#PREKAZKA
VYSKA_PODSTAVY = 15
SIRKA_PODSTAVY = 50
SIRKA_PREKAZKY = 30
MEDZERA = 80

#HRAC
VYSKA_HRACA = 30
SIRKA_HRACA = 30
AKCELERACIA = 5

pozicia_hraca = [100,200]
pozicia_prekazky1 = [300,250]
pozicia_prekazky2 = [600,200]
pozicia_prekazky3 = [900,300]
rychlost_hraca = [0]
stisknuta_klavesnica = [0]
body = [0]
schopny_hrat = [1]

def vykresli_obdlznik(x1,y1, x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)  
    gl.glVertex2f(int(x1), int(y1))  
    gl.glVertex2f(int(x1), int(y2))  
    gl.glVertex2f(int(x2), int(y2))  
    gl.glVertex2f(int(x2), int(y1))  
    gl.glEnd()

def vykresli_pozadie():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(0, 0.75, 1)

    vykresli_obdlznik(
        0,
        0,
        SIRKA,
        VYSKA
    )

def vykresli_podlahu():
    gl.glColor3f(0.2,0.6,0.2)
    vykresli_obdlznik(
        0,
        0,
        SIRKA,
        50
    )
def vykresli_prekazku1():
    #horna prekazka_____
    #nastavi farbu:
    gl.glColor3f(0.11, 0.59 , 0.11 )
    #nakresli podstavu
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] + MEDZERA//2,
        pozicia_prekazky1[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky1[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky1[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )

    #dolna prekazka
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] - MEDZERA//2,
        pozicia_prekazky1[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky1[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky1[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky1[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky1[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )
def vykresli_prekazku2():
    #horna prekazka_____
    #nastavi farbu:
    gl.glColor3f(0.11, 0.59 , 0.11 )
    #nakresli podstavu
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] + MEDZERA//2,
        pozicia_prekazky2[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky2[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky2[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )

    #dolna prekazka
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] - MEDZERA//2,
        pozicia_prekazky2[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky2[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky2[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky2[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky2[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )
def vykresli_prekazku3():
    #horna prekazka_____
    #nastavi farbu:
    gl.glColor3f(0.11, 0.59 , 0.11 )
    #nakresli podstavu
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] + MEDZERA//2,
        pozicia_prekazky3[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] + MEDZERA//2 + VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PREKAZKY//2,
        pozicia_prekazky3[1] + MEDZERA//2 + VYSKA_PODSTAVY,
        pozicia_prekazky3[0] + SIRKA_PREKAZKY//2,
        VYSKA
    )

    #dolna prekazka
    gl.glColor3f(0.11, 0.59 , 0.11 )
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] - MEDZERA//2,
        pozicia_prekazky3[0] + SIRKA_PODSTAVY//2,
        pozicia_prekazky3[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )
    gl.glColor3f(0.1, 0.8, 0.1)
    vykresli_obdlznik(
        pozicia_prekazky3[0] - SIRKA_PREKAZKY//2,
        0,
        pozicia_prekazky3[0] + SIRKA_PREKAZKY//2,
        pozicia_prekazky3[1] - MEDZERA//2 - VYSKA_PODSTAVY
    )

def vykresli_hrac():
    gl.glColor3f(1, 0, 0)
    vykresli_obdlznik(
        pozicia_hraca[0] - SIRKA_HRACA//2,
        pozicia_hraca[1] - VYSKA_HRACA//2,
        pozicia_hraca[0] + SIRKA_HRACA//2,
        pozicia_hraca[1] + VYSKA_HRACA//2
    )

def vykresli():
    vykresli_pozadie()
    vykresli_hrac()
    vykresli_prekazku1()
    vykresli_prekazku2()
    vykresli_prekazku3()
    vykresli_podlahu()

rychlost_hraca1 = 0

def obnov_stav(dt):
    #pohyb hraca
    print(dt)
    rychlost_hraca1 = int(rychlost_hraca[0])
    if stisknuta_klavesnica[0] == 1:
        pozicia_hraca[1] += rychlost_hraca1 * dt
        rychlost_hraca[0] += AKCELERACIA
    if stisknuta_klavesnica[0] == 0:
        pozicia_hraca[1] += rychlost_hraca1 * dt
        rychlost_hraca[0] -= AKCELERACIA
    #pohyb_prekazok
    pozicia_prekazky1[0] -= RYCHLOST * dt
    pozicia_prekazky2[0] -= RYCHLOST * dt
    pozicia_prekazky3[0] -= RYCHLOST * dt
    #portnutie prekazok
    if pozicia_prekazky1[0] < 25:
        nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
        pozicia_prekazky1[0] = SIRKA - 25
        pozicia_prekazky1[1] = nova_pozicia
    if pozicia_prekazky2[0] < 25:
        nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
        pozicia_prekazky2[0] = SIRKA - 25
        pozicia_prekazky2[1] = nova_pozicia
    if pozicia_prekazky3[0] < 25:
        nova_pozicia = randint(50+MEDZERA//2, VYSKA-MEDZERA//2)
        pozicia_prekazky3[0] = SIRKA - 25
        pozicia_prekazky3[1] = nova_pozicia
    #spodna hranica
    if pozicia_hraca[1] < 50 + VYSKA_HRACA//2:
        if rychlost_hraca[0] < 0:
            rychlost_hraca[0] = 0
    #kontaktna zona
    if int(pozicia_hraca[0]) + SIRKA_HRACA//2 + SIRKA_PODSTAVY//2 > int(pozicia_prekazky1[0]) >int(pozicia_hraca[0]) - SIRKA_HRACA//2 - SIRKA_PODSTAVY//2:
        if pozicia_prekazky1[1] - MEDZERA//2 + VYSKA_HRACA//2 > pozicia_hraca[1]:
            print("koniec")
        elif pozicia_hraca[1] > pozicia_prekazky1[1] + MEDZERA//2 - VYSKA_HRACA//2:
            print("ahoj")
       # if pozicia_hraca[0] - 0.3 < pozicia_prekazky1[0] < pozicia_hraca[0] + 0.3:
         #   body[0] += 1

def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.SPACE:
        stisknuta_klavesnica[0] = 1
    if symbol == key.UP:
        stisknuta_klavesnica[0] = 1
def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.SPACE:
        stisknuta_klavesnica[0] = 0
    if symbol == key.UP:
        stisknuta_klavesnica[0] = 0
        


window = pyglet.window.Window(width=SIRKA,height=VYSKA)
window.push_handlers(
    on_draw=vykresli,
    on_key_press=stisk_klavesnice,
    on_key_release=pusti_klavesnice
)
pyglet.clock.schedule_interval(obnov_stav, 1/165)


pyglet.app.run() 