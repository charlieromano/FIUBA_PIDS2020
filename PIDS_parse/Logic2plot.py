import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Path='/home/charlieromano/Documents/Academico/CESE/Proyecto2020/TallerCastelar/Mediciones/traza/dataOut'

dt = pd.read_csv(Path+'/Wave_bin.txt', header=34, sep='\t', index_col=0)

dt.head()
dt.columns
dt.dtypes

# reemplazar '                 ' por '	'

# crear df a partir de dt con los canales de datos
df = dt[['A0','A1']]

# reemplazar U por NaN-->None
df = df.replace('U', df.replace(['U'], [np.nan])) # or .replace('-', {0: None})
df['A1'].plot()
plt.show()

# TO DO:
# castear a binario si hace falta
# pasar el index a timeseries
# ajustar el timestep y condensar datos 

# User Story
# quiero leer la frecuencia de la señal de datos
# quiero leer los datos en hexa
