from random import randint
moznosti = ["kameň", "papier", "nožnice"]

def hra():
    pocet_vyhier = [0,0]
    pocet_vyhier_dokoncenych = 0
    meno = getName()
    pocet_max_vyhier = int(getWinCount())
    player_decission = 0
    while pocet_vyhier_dokoncenych != pocet_max_vyhier:
        if pocet_vyhier[0] > pocet_vyhier[1]:
                print("Zatiaľ vyhrávaš [", pocet_vyhier[0],":", pocet_vyhier[1], "] zostávajú ešte", pocet_max_vyhier - pocet_vyhier_dokoncenych)
        elif pocet_vyhier[0] == pocet_vyhier[1]:
            print("Zatiaľ je to remíza [", pocet_vyhier[0],":", pocet_vyhier[1], "] zostávajú ešte", pocet_max_vyhier - pocet_vyhier_dokoncenych)
        else:
            print("Zatiaľ prehrávaš [", pocet_vyhier[0],":", pocet_vyhier[1], "] zostávajú ešte", pocet_max_vyhier - pocet_vyhier_dokoncenych)
        player_decission = input("Pre kameň napíš [0], pre papier [1] a pre nožnice [2]>>>")
        if -1 < int(player_decission) < 3:
            bot_decission = getBot()
            vyhral = controlWin(player_decission, bot_decission)
            print("[",meno,"]", moznosti[int(player_decission)], "<->", moznosti[int(bot_decission)], "[ BOT ]")
            if vyhral == 0:
                print("Je to remíza!")
            elif vyhral == 1:
                print("Vyhral si", meno)
                pocet_vyhier[0] += 1
            elif vyhral == 2:
                print("Prehral si.")
                pocet_vyhier[1] += 1
            pocet_vyhier_dokoncenych = int(max(pocet_vyhier))
            
        else:
            print("Error: Prośim vlož číslo [0] alebo [1] alebo [2].")
    if pocet_vyhier[0] > pocet_vyhier[1]:
        print("Gratulujem vyhral si", pocet_vyhier[0],":", pocet_vyhier[1])
    else:
        print("Je mi ľúto, prehral si", pocet_vyhier[0],":", pocet_vyhier[1] )


def getName():
    meno = input("Ako sa voláš?>>>")
    return meno
def getWinCount():
    pocet_pokusov = input("Na koľko výhier hráme?>>>")
    return pocet_pokusov
def getBot():
    randomne = randint(0,2)
    decission = randomne
    return decission
def controlWin(player, bot):
    player = int(player)
    bot = int(bot)
    if player == bot:
        return 0
    elif player == 0 and bot == 1:
        return int(2)
    elif player == 1 and bot == 2:
        return int(2)
    elif player == 2 and bot == 0:
        return int(2)
    elif player == 0 and bot == 2:
        return int(1)
    elif player == 2 and bot == 1:
        return int(1)
    elif player == 1 and bot == 0:
        return int(1)
        

    
hra()