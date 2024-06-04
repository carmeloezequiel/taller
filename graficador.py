import pandas as pd
import matplotlib.pyplot as plt
from detecta import detect_peaks
from scipy.signal import deconvolve

from peakutils import baseline


#LEER LOS ARCHIVOS CSV
datos_yodo = pd.read_csv('csv-yodo-2.0.csv', sep=';')
datos_abs = pd.read_csv('dabs-just-luz.csv', sep=';')

datos_vo = pd.read_excel('valles0.xlsx')
datos_v1 = pd.read_excel('valles1.xlsx')
datos_v2 = pd.read_excel('valles2.xlsx')

#CREAR LOS DATAFRAMES

df_datos_yodo = pd.DataFrame(datos_yodo)
df_datos_yodo['abs'] = - df_datos_yodo['cuentas'] / datos_abs['cuentas']

df_datos_vo = pd.DataFrame(datos_vo)
df_datos_v1 = pd.DataFrame(datos_v1)
df_datos_v2 = pd.DataFrame(datos_v2)

#Deteccion de valles
index = detect_peaks(df_datos_yodo['cuentas'], valley=True)
#index = detect_peaks(df_datos_yodo_luz['cuentas'])
df_picos = df_datos_yodo.loc[index]
picos = df_picos.loc[df_datos_yodo['cuentas'] > 1500]


df_datos_yodo['lamda'].loc[df_datos_yodo['lamda'] < 515] = None
df_datos_yodo['lamda'].loc[df_datos_yodo['lamda'] > 600] = None


df_picos['lamda'].loc[df_picos['lamda'] < 515] = None
df_picos['lamda'].loc[df_picos['lamda'] > 600] = None

#df_picos.to_excel('valles2.xlsx')

#banda v0

valores_xvo = df_datos_vo['lamda']
valores_yvo = df_datos_vo['abs']
#grafico = plt.plot(valores_xvo, valores_yvo, c='g')

#banda v1

valores_xv1 = df_datos_v1['lamda']
valores_yv1 = df_datos_v1['abs']
#grafico = plt.plot(valores_xv1, valores_yv1, c='r')

#banda v2

valores_xv2 = df_datos_v2['lamda']
valores_yv2 = df_datos_v2['abs']
#grafico = plt.plot(valores_xv2, valores_yv2, c='Purple')

#grafico 
valores_x = df_datos_yodo['lamda']
valores_y = df_datos_yodo['abs']
grafico = plt.plot(valores_x, valores_y)

#grafico valles
valores_xp = df_picos['lamda']
valores_yp = df_picos['abs']
#grafico = plt.scatter(valores_xp, valores_yp, marker= '.', alpha= 0.9, c='g')

plt.title('Espectro Molecular del Yodo')
plt.xlabel('Coeficiente de Absorción')
plt.ylabel('Longitud de Onda (nm)')

plt.show()

print(df_datos_vo.head())