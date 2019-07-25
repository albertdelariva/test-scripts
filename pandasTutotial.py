# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:23:05 2019

@author: Albert de la Riva

From https://www.dataquest.io/blog/excel-and-pandas/
"""

import pandas as pd

#o poses tot el path així:
#excel_file = r'C:\Users\Albert de la Riva\PandasTutorialMovies\movies.xls'
#la r' es perquè no es lii amb els backslash

#o el excel file ha d'estar a la mateixa carpeta que el *.py
excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)

movies.head()

#podem especificar el sheet (comença per 0), ara es sheet_name amb subguió, abans sense
#podem definir que una columna sigui l'index, en aquest cas la primera (0)
movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet1.head()
movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet2.head()
movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies_sheet3.head()

#amb concat enganxem els 3 sheets i fer overwrite del df movies
movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

#amb el codi següent només accedeixes un cop al excel per llegir totes les sheets, més eficient
'''
xlsx = pd.ExcelFile(excel_file)
movies_sheets = []
for sheet in xlsx.sheet_names:
    movies_sheets.append(xlsx.parse(sheet))
movies = pd.concat(movies_sheets)
'''

#veure dimensions del df
movies.shape

#veure X primeres o últimes rows del df
movies.head(10)
movies.tail()

#sorting
sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)
sorted_by_gross["Gross Earnings"].head(10)


#MatPlotLib
import matplotlib.pyplot as plt

#agafes el dataframe, selecciones el tros que vols i li dius tipus de plot
sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")

#plt.show() no longer needed
#plt.show()

movies['IMDB Score'].plot(kind="hist")
#plt.show()

#Mirar màxima i mínima puntuació
sorted_by_imbd = movies.sort_values(['IMDB Score'], ascending=True)
print(sorted_by_imbd["IMDB Score"].head(1))
print(sorted_by_imbd["IMDB Score"].tail(1))


name = "john yuki"
age = 24
job = "student"

print("Hello, " + name + ". You are", age, "years old. You are a " + job + ".")
print(f"Hello, {name}. You are {age} years old. You are a {job}.")












