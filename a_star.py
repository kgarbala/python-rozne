''' Krzysztof Garbala
A star algorithm'''

import random
from collections import deque

def stworzmape(dim_x, dim_y, poziom_trudnosci = 2):
    '''tworze mape o wymiarach dimx x dimy na ktorej losowo ustawia przeszkody
    poziom_trudnosci = 1 -> 50% to przeszkody, 2-> 33%, 3 -> 25%...
    wolne pole ustawione na -1
    przeszkody na -200
    (dim_x, dim_y) -> dict np {(0, 0): 2, (0, 1): 2} '''	
    przeszkoda = -200
    wolne_pole = -1
    wspolrzedne_mapy = [[(x, y) for x in range(dim_x)] for y in range(dim_y)]
    zajete_wolne = [[wolne_pole if random.randint(0, poziom_trudnosci) != 0
		     else przeszkoda for x in range(dim_x)] for y in range(dim_y)]
    slownik = {wspolrzedne_mapy[x][y]: zajete_wolne[x][y] for x in range(dim_x)
              for y in range(dim_y)}
    return slownik

def szukajdrogi(SLOWNIK, start_x, start_y, stop_x, stop_y):
    ''' szuka drogi z punktu (start_x, start_y) do punktu (stop_x, stop_y)
    (start_x, start_y, stop_x, stop_y) -> dict np {(0, 0): 2, (0, 1): 2}
    lub komunikat, ze nie znaleziono
    '''
    if (start_x, start_y) not in SLOWNIK or (stop_x, stop_y) not in SLOWNIK:
	print 'zle wybrane wspolrzedne'
	return 0
    czy_zwiedzone = -1 in SLOWNIK.values()
    kolejka = deque()
    SLOWNIK[(start_x, start_y)], SLOWNIK[(stop_x, stop_y)] = 0, -1
    kolejka.append((start_x, start_y))
    wsp = (start_x, start_y)
    while wsp != (stop_x, stop_y) and czy_zwiedzone:
	# tworzenie "rownomiernej" mapy wag od stratu
	# do 'wszedzie', jak znajdzie cel - skonczy
        wsp = kolejka[0]
        kolejka.popleft()

        ## GORA DOL LEWO PRAWO
        if (wsp[0]+1, wsp[1]) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]+1, wsp[1])] != -200:
            SLOWNIK[(wsp[0]+1, wsp[1])] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]+1, wsp[1]))

        if (wsp[0], wsp[1]+1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0], wsp[1]+1)] != -200:
            SLOWNIK[(wsp[0], wsp[1]+1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0], wsp[1]+1))

        if (wsp[0]-1, wsp[1]) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]-1, wsp[1])] != -200:
            SLOWNIK[(wsp[0]-1, wsp[1])] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]-1, wsp[1]))

        if (wsp[0], wsp[1]-1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0], wsp[1]-1)] != -200:
            SLOWNIK[(wsp[0], wsp[1]-1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0], wsp[1]-1))

        ## NA SKOSY
        if (wsp[0]-1, wsp[1]-1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]-1, wsp[1]-1)] != -200:
            SLOWNIK[(wsp[0]-1, wsp[1]-1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]-1, wsp[1]-1))

        if (wsp[0]-1, wsp[1]+1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]-1, wsp[1]+1)] != -200:
            SLOWNIK[(wsp[0]-1, wsp[1]+1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]-1, wsp[1]+1))

        if (wsp[0]+1, wsp[1]-1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]+1, wsp[1]-1)] != -200:
            SLOWNIK[(wsp[0]+1, wsp[1]-1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]+1, wsp[1]-1))

        if (wsp[0]+1, wsp[1]+1) in SLOWNIK.keys() and \
        -1 == SLOWNIK[(wsp[0]+1, wsp[1]+1)] != -200:
            SLOWNIK[(wsp[0]+1, wsp[1]+1)] = SLOWNIK[wsp] +1
            kolejka.append((wsp[0]+1, wsp[1]+1))
        if not kolejka:
            #print "Nie znaleziono celu."
            return
        czy_zwiedzone = -1 in SLOWNIK.values()
    else:
        # zbieranie punktow, ktore utworza droge do celu - szukanie
        # pola o 1 mniejszego niz pole na ktorym stoje, poczynajac
        # od celu, idac do startu
        #print "Znaleziono cel:"
        war = (stop_x, stop_y)
        droga = []
        while war != (start_x, start_y):
            droga.append(war)

            if (war[0]+1, war[1]) in SLOWNIK.keys() and (war[0]+1, war[1])\
             != -200 and SLOWNIK[(war[0]+1, war[1])] == SLOWNIK[war] - 1:
                war = (war[0]+1, war[1])
                continue

            if (war[0], war[1]+1) in SLOWNIK.keys() and (war[0], war[1]+1)\
             != -200 and SLOWNIK[(war[0], war[1]+1)] == SLOWNIK[war] - 1:
                war = (war[0], war[1]+1)
                continue

            if (war[0]-1, war[1]) in SLOWNIK.keys() and (war[0]-1, war[1])\
             != -200 and SLOWNIK[(war[0]-1, war[1])] == SLOWNIK[war] - 1:
                war = (war[0]-1, war[1])
                continue

            if (war[0], war[1]-1) in SLOWNIK.keys() and (war[0], war[1]-1)\
             != -200 and SLOWNIK[(war[0], war[1]-1)] == SLOWNIK[war] - 1:
                war = (war[0], war[1]-1)
                continue

            if (war[0]+1, war[1]+1) in SLOWNIK.keys() and (war[0]+1, war[1]+1)\
	    != -200 and SLOWNIK[(war[0]+1, war[1]+1)] == SLOWNIK[war] - 1:
                war = (war[0]+1, war[1]+1)
                continue

            if (war[0]-1, war[1]-1) in SLOWNIK.keys() and (war[0]-1, war[1]-1)\
            != -200 and SLOWNIK[(war[0]-1, war[1]-1)] == SLOWNIK[war] - 1:
                war = (war[0]-1, war[1]-1)
                continue

            if (war[0]+1, war[1]-1) in SLOWNIK.keys() and (war[0]+1, war[1]-1)\
             != -200 and SLOWNIK[(war[0]+1, war[1]-1)] == SLOWNIK[war] - 1:
                war = (war[0]+1, war[1]-1)
                continue

            if (war[0]-1, war[1]+1) in SLOWNIK.keys() and (war[0]-1, war[1]+1)\
             != -200 and SLOWNIK[(war[0]-1, war[1]+1)] == SLOWNIK[war] - 1:
                war = (war[0]-1, war[1]+1)
                continue

        droga.append(war)
        #print 'droga:', droga
        return droga



if __name__ == '__main__':
    DIM_X = 50
    DIM_Y = 50
    START_Y = 0 
    START_X = 49
    STOP_X = 49
    STOP_Y = 0
    SLOWNIK = stworzmape(DIM_X, DIM_Y)
    DROGA = szukajdrogi(SLOWNIK, START_X, START_Y, STOP_X, STOP_Y)
    #print SLOWNIK
    print DROGA
    