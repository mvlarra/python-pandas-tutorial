
# 02.1 Create a Script _________________________
print("Hello World")

# 02.2 Import _________________________
import pandas as pd
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print (data_frame)

# 03 Datasets _________________________

# 04 Series __________________________________________________
data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

# 04.1 Date Range  __________________________________________________
data_dates = pd.date_range("2021-05-01", "2021-05-12")
print(data_dates)

# 04.2 Series Apply  __________________________________________________
my_series = pd.Series([2, 4, 6, 8, 10])
modified_series = my_series.apply(lambda x:x/2)
print(modified_series)

# 05 DataFrames  __________________________________________________
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
print (df)

# 05.1 DataFrame Dict   __________________________________________________

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]

df = pd.DataFrame(data)

print(df)

# 05.2 DataFrame iLoc   __________________________________________________
df = pd.read_csv ('.learn/assets/pokemon_data.csv')
print(data_frame.iloc[133,6])

# 05.3 DataFrame Head __________________________________________________
print(df.head(3))

# 05.4 DataFrame Tail __________________________________________________
print(df.tail(3))

# 05.5 Print Columns __________________________________________________
print(df[['Name', 'Type 1']][0:10])

# 05.6 Loc Function __________________________________________________

print(df.loc[df['Attack'] > 80])

# 05.7 Filter and Count __________________________________________________
print(len(df.loc[df['Legendary'] == True]))
    # My Notes:

    # df['Legendary'] == True:
    #
    #       Esto crea una serie booleana (una columna de valores True o False) en la cual 
    #       cada fila se evalúa según si el valor en la columna Legendary es True. 
    #       Esto filtra las filas en las que la columna Legendary tiene el valor True.
    #
    #       Si, por ejemplo, df['Legendary'] tiene valores como [True, False, True, True], 
    #       entonces df['Legendary'] == True dará como resultado [True, False, True, True].

    # df.loc[df['Legendary'] == True]:
    #
    #       El .loc[] es un método de pandas que se utiliza para acceder a un subconjunto 
    #       de filas o columnas de un DataFrame.
    # 
    #       Al pasarle la serie booleana df['Legendary'] == True, .loc[] selecciona solo 
    #       aquellas filas donde la condición es True. Esto filtra el DataFrame para mostrar 
    #       solo las filas donde la columna Legendary tiene el valor True.

    # len(...):
    #
    #       len() devuelve la longitud de un objeto. En este caso, está contando cuántas filas
    #       hay en el DataFrame filtrado (es decir, cuántas filas tienen Legendary == True).
    #       
    #       Si, por ejemplo, hay 3 filas en las que Legendary es True, entonces len() devolverá 3.


# 06 Clean Datasets __________________________________________________

df_Baby_Names = pd.read_csv (".learn/assets/us_baby_names_right.csv")
print(df_Baby_Names.head(5))

# 06.1 Remove Column __________________________________________________
del df_Baby_Names[df_Baby_Names.columns[0]]
print(df_Baby_Names.head(5))

    # My Notes:
        # del:
            # El comando del se utiliza para eliminar un objeto en Python.
            # En este caso, del df_Baby_Names[...] elimina la columna especificada (en este caso, la columna cuyo nombre está en df_Baby_Names.columns[0]).
            # Internamente, pandas elimina la columna completa y la remueve del DataFrame.


# 06.2 Value Counts __________________________________________________

count = df_Baby_Names['Gender'].value_counts()
print(count)


# 06.3 Group By __________________________________________________

names = df_Baby_Names.groupby("Name").sum()
print(len(names))

# __________________________________________________
# __________________________________________________
# __________________________________________________
# __________________________________________________

# python app.py