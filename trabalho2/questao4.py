import math

#No átomo de hidrogênio, a distância média entre o elétron e o próton é de aproximadamente 0,5 Å. Calcule a razão entre as atrações coulombiana e gravitacional das duas partículas no átomo. A que distância entre o elétron e o próton sua atração coulombiana se tornaria igual à atração gravitacional existente entre eles no átomo? Compare o resultado

#proton
mPro = 1.673e-27  # Massa do próton (kg)
cPro = 1.602e-19  # Carga do próton (C)

#eletron
cElet = 1.602e-19  # Carga do elétron (C)
mElet = 9.109e-31  # Massa do elétron (kg)

#constantes
dMic = 5e-11    #distancia entre o elétron e o próton no átomo de hidrogenio em metros "distancia microscopica"
g = 6.674e-11   # Constante gravitacional (N·m²/kg²)
k = 8.9875e9    # Constante eletrostática (N·m²/C²)


#forca que o próton exerce no elétron na molécula de hidrogenio
fEletMic = abs(k*(cElet * cPro) / dMic**2)

fGravMic = abs(g*(mElet * mPro) / dMic**2)


#distancia que as duas se igualam

dist = math.sqrt( (k*cElet*cPro) / (g*mElet*mPro) )


#resultados
print(f"A força elétrica é {fEletMic/fGravMic:.2e}, ou {fEletMic/fGravMic:.0f} mais forte que a força gravitacional na distância atômica do átomo do hidrogênio")
print(f"As duas forças vão se igualar a uma distância de {dist:.2e} metros, ou o equivalente a {dist/9.46e+15:.0f} anos luz")