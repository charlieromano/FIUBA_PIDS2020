import pandas as pd


Path='/home/charlieromano/Documents/Academico/CESE/Proyecto2020/TallerCastelar/Mediciones/traza/dataOut'

dt = pd.read_csv(Path+'/Wave_bin.txt', header=34, sep='\t')
