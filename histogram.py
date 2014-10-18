# Krzysztof Garbala
'''modul tworzy 9 subplotow-histogramow z wczytanego pliku'''
import matplotlib.pyplot as plt
# Slowacja, wielkopolska, polesie
with open('histogram.txt') as foo:
    RESULTS = foo.read()

RESULTS = RESULTS.split('\n')
# sm - soil moisture; pd - Penetration depth; swe - soil water equivalent
SM_SLOVAKIA = [row.split('\t')[0] for row in RESULTS]
PD_SLOVAKIA = [row.split('\t')[1] for row in RESULTS]
SWE_SLOVAKIA = [row.split('\t')[2] for row in RESULTS]

SM_SLOVAKIA = [float(x) for x in SM_SLOVAKIA[1:]]
PD_SLOVAKIA = [float(x) for x in PD_SLOVAKIA[1:]]
SWE_SLOVAKIA = [float(x) for x in SWE_SLOVAKIA[1:]]

SM_WIELKOPOLSKA = [row.split('\t')[3] for row in RESULTS]
PD_WIELKOPOLSKA = [row.split('\t')[4] for row in RESULTS]
SWE_WIELKOPOLSKA = [row.split('\t')[5] for row in RESULTS]

SM_WIELKOPOLSKA = [float(x) for x in SM_WIELKOPOLSKA[1:]]
PD_WIELKOPOLSKA = [float(x) for x in PD_WIELKOPOLSKA[1:]]
SWE_WIELKOPOLSKA = [float(x) for x in SWE_WIELKOPOLSKA[1:]]

SM_POLESIE = [row.split('\t')[6] for row in RESULTS]
PD_POLESIE = [row.split('\t')[7] for row in RESULTS]
SWE_POLESIE = [row.split('\t')[8] for row in RESULTS]

SM_POLESIE = [float(x) for x in SM_POLESIE[1:]]
PD_POLESIE = [float(x) for x in PD_POLESIE[1:]]
SWE_POLESIE = [float(x) for x in SWE_POLESIE[1:]]


KUBELEK = 44/2
SM_COLOR = '#06267F'
PD_COLOR = '#626262'
SWE_COLOR = '#C0D9D9'
##########
AXES_SM = [0.05, 0.36, 0, 10.2]
AXES_PD = [1.0, 4.6, 0, 10.2]
AXES_SWE = [0.3, 0.42, 0, 8.2]

###################### SLOVAKIA
plt.subplot(3, 3, 1)
plt.title("Soil moisture\n\n\n")
plt.hist(SM_SLOVAKIA, bins=KUBELEK, color=SM_COLOR)
plt.axis(AXES_SM)
plt.ylabel("Frequency [pixels]")


plt.subplot(3, 3, 2)
plt.title("Penetration depth\n\n\n")
plt.hist(PD_SLOVAKIA, bins=KUBELEK, color=PD_COLOR)
plt.axis(AXES_PD)
plt. text(2.8, 10.5, 'Slovakia', horizontalalignment='center', fontsize=17)

plt.subplot(3, 3, 3)
plt.title("Soil water equivalent\n\n\n")
plt.hist(SWE_SLOVAKIA, bins=KUBELEK, color=SWE_COLOR)
plt.axis(AXES_SWE)

###################### WIELKOPOLSKA
plt.subplot(3, 3, 4)
plt.hist(SM_WIELKOPOLSKA, bins=KUBELEK, color=SM_COLOR)
plt.axis(AXES_SM)
plt.ylabel("Frequency [pixels]")

plt.subplot(3, 3, 5)
plt.hist(PD_WIELKOPOLSKA, bins=KUBELEK, color=PD_COLOR)
plt.axis(AXES_PD)
plt. text(2.8, 10.5, 'Wielkopolska', horizontalalignment='center', fontsize=17)

plt.subplot(3, 3, 6)
plt.hist(SWE_WIELKOPOLSKA, bins=KUBELEK, color=SWE_COLOR)
plt.axis(AXES_SWE)

###################### POLESIE
plt.subplot(3, 3, 7)
plt.hist(SM_POLESIE, bins=KUBELEK, color=SM_COLOR)
plt.xlabel(r'Soil moisture [$m^3m^{-3}$]')
plt.ylabel("Frequency [pixels]")
plt.axis(AXES_SM)

plt.subplot(3, 3, 8)
plt.hist(PD_POLESIE, bins=KUBELEK, color=PD_COLOR)
plt.xlabel(r'Penetration depth [$\lambda$]')
plt.axis(AXES_PD)
plt.text(2.8, 10.5, 'Polesie', horizontalalignment='center', fontsize=17)

plt.subplot(3, 3, 9)
plt.hist(SWE_POLESIE, bins=KUBELEK, color=SWE_COLOR)
plt.xlabel(r'Soil water equivalent [-]')
plt.axis(AXES_SWE)
plt.show()
