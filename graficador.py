import pandas as pd
import matplotlib.pyplot as plt
from detecta import detect_peaks

from peakutils import baseline


#LEER LOS ARCHIVOS CSV
datos_yodo = pd.read_csv('csv-yodo-2.0.csv', sep=';')


#CREAR LOS DATAFRAMES

df_datos_yodo = pd.DataFrame(datos_yodo)
df_datos_yodo['abs'] = - df_datos_yodo['cuentas']


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



#grafico 
valores_x = df_datos_yodo['lamda']
valores_y = df_datos_yodo['abs']
grafico = plt.plot(valores_x, valores_y, c='r')

#grafico valles
valores_xp = df_picos['lamda']
valores_yp = df_picos['abs']
#grafico = plt.scatter(valores_xp, valores_yp, marker= '.', alpha= 0.9, c='g')

plt.title('Espectro Molecular del Yodo')
plt.xlabel('Coeficiente de Absorción')
plt.ylabel('Longitud de Onda (nm)')


plt.savefig('datos')

