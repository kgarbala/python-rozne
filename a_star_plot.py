'''Krzysztof Garbala
skrypt rysujacy sciezke dla A*
'''
def stworzwykresdrogi(DROGA):
    wsp_x = [x[0] for x in DROGA]
    wsp_y = [y[1] for y in DROGA]
    return wsp_x, wsp_y

def stworzmape(SLOWNIK, WSP_X, WSP_Y):
    import numpy as np
    import matplotlib.pyplot as plt
    for key in SLOWNIK.keys():
        if SLOWNIK[key] == -200:
            SLOWNIK[key] = -1
        else:
            SLOWNIK[key] = 0
    sorted_map = sorted(zip(SLOWNIK.keys(), SLOWNIK.values()))
    macierz_war = [num[1] for num in sorted_map]
    macierz_war1 = np.matrix(macierz_war).reshape(DIM_X, DIM_Y)

    plt.figure("A star")
    plt.hold(True)
    plt.grid(True)
    plt.title("A star")
    plt.xlabel('x')
    plt.ylabel("y")
    plt.axis([0, DIM_X-1, 0, DIM_Y-1])
    plt.plot(WSP_Y, WSP_X, color='g', linewidth=4)
    plt.imshow(macierz_war1, interpolation='nearest')

    cbar = plt.colorbar(ticks=[-1, 0])
    cbar.ax.set_yticklabels(['przeszkoda', 'wolne pole'])
    plt.show()

if __name__ == '__main__':
    import a_star
    import time
    DIM_X = DIM_Y = 50
    START_X = 0
    START_Y = 0
    STOP_X = 49
    STOP_Y = 49
    POZIOM_TRUDNOSCI = 3
    TIME = time.time()
    SLOWNIK = a_star.stworzmape(DIM_X, DIM_Y, POZIOM_TRUDNOSCI)
    DROGA = a_star.szukajdrogi(SLOWNIK, START_X, START_Y, STOP_X, STOP_Y)
    print 'czas dzialania to: {0:.2f} sekund'.format(time.time() - TIME)
    if not DROGA:
        print "droga do celu zablokowana"
    else:
        WSP_X, WSP_Y = stworzwykresdrogi(DROGA)
        stworzmape(SLOWNIK, WSP_X, WSP_Y)
