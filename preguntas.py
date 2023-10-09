"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    filas=tbl0.shape[0]
    return filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    cols=tbl0.shape[1]
    return cols


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    cuenta=tbl0['_c1'].value_counts().sort_index()
    return cuenta


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    serie=pd.Series()
    letras=['A','B','C','D','E']
    for letra in letras:
        serie[f'{letra}']=(tbl0[tbl0['_c1']==letra]['_c2']).mean()
    return serie


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    serie=pd.Series()
    letras=['A','B','C','D','E']

    for letra in letras:
        serie[f'{letra}']=(tbl0[tbl0['_c1']==letra]['_c2']).max()
    return serie


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    serie=pd.Series(tbl1['_c4'])

    serie=pd.Series(serie.sort_values().unique())
    lista=list(valor.upper() for valor in serie)
    return lista


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    serie=pd.Series()
    for letra in pd.Series(tbl0['_c1']).unique():
        cuenta=sum(tbl0[tbl0['_c1']==letra]['_c2'])
        serie[letra]=cuenta
    serie=serie.sort_index()
    return serie


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tbl0['suma']=tbl0['_c0']+tbl0['_c2']
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    year=pd.Series(col.split('-')[0] for col in tbl0['_c3'])
    tbl0['year']=year
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    serie=pd.Series()
    tabla=pd.DataFrame()
    for letra in pd.Series(tbl0['_c1']).unique():
        nums=list(tbl0[tbl0['_c1']==letra]['_c2'])
        nums.sort()
        nums=':'.join(map(str,nums))
        serie[letra]=nums
    serie=serie.sort_index()
    tabla.index=serie.index
    tabla.index.name='_c1'
    tabla['_c2']=serie.values
    return tabla


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    serie=pd.Series()
    tabla=pd.DataFrame()
    for num in pd.Series(tbl1['_c0']).unique():
        letra=list(tbl1[tbl1['_c0']==num]['_c4'])
        letra.sort()
        letra=','.join(map(str,letra))
        serie[num]=letra

    tabla['_c0']=serie.index
    tabla['_c4']=serie.values
    return tabla


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    serie=pd.Series()
    tabla=pd.DataFrame()
    lista=[]
    lista_pares=[]

    tabla['_c0']=tbl2['_c0'].unique()
    for indice in tbl2['_c0'].unique():
        lista=[]
        df=tbl2[tbl2['_c0']==indice]
        for index,fila in df.iterrows():
            par=':'.join([fila['_c5a'],str(fila['_c5b'])])
            lista.append(par)
            lista.sort()
            str(lista)
        lista_pares.append(lista)
        serie=pd.Series(lista_pares)
    tabla['_c5']=serie
    tabla['_c5']=tabla['_c5'].apply(lambda x:','.join(x))
    return tabla


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    lista_letras=pd.Series(tbl0['_c1']).unique()
    lista_letras.sort()
    lista_temp=[]
    suma:int
    serie=pd.Series()

    for letra in lista_letras:
        suma=0
        lista_temp=list(tbl0[tbl0["_c1"]==letra]['_c0'])
        for num in lista_temp:
            suma=suma+(tbl2[tbl2['_c0']==num]['_c5b']).sum()
        serie[letra]=suma
    return serie
