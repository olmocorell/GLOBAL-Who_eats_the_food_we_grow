import pandas as pd

def loadCleanData():
    """
    Load data, rename year`s columns, drop duplicates
    and return clean dataframe
    """
    df = pd.read_csv("input/FAO.csv",encoding='cp1252')
    columnas = df.columns[10:]
    nombres = []
    for a in columnas:
        nombres.append((a,a[1:]))
    nombres = dict(nombres)
    df = df.rename(columns=nombres)
    df = df.drop_duplicates()
    return df


def choice(param):
    """
    generates a simple dataframe with the unique data of 
    the area and item columns for the selectbox
    """
    data = loadCleanData()
    dfarea = {"Area":data.Area.unique()}
    data1 = pd.DataFrame(dfarea)
    dfitem = {"Item":data.Item.unique()}
    data2 = pd.DataFrame(dfitem)
    data3 = pd.DataFrame(list(range(1961,2014)))
    data3["Years"] = pd.DataFrame(list(range(1961,2014)))
    if param == "Item":
        return data2["Item"]
    elif param == "Year":
        return data3["Years"]
    else:
        return data1["Area"]

def grafico(area,item):
    """
    data filtering according to the user's choice
    """
    years = list(range(1980,2014))
    data = loadCleanData()
    data = data.fillna(0)
    data = data[(data["Area"]==f"{area}")&(data["Item"]==f"{item}")]
    feed = []
    food = []
    if len(data) == 1:
        indice = data.index[0]
        if data.Element[indice] == 'Food':
            for ye in years:
                temporal = list(data[f"{ye}"])
                for elemento in temporal:
                    food.append(elemento)
                    feed.append(0)
        
        elif data.Element[indice] == 'Feed':
            for ye in years:
                temporal = list(data[f"{ye}"])
                for elemento in temporal:
                    food.append(0)
                    feed.append(elemento)
    
    elif len(data)== 0:
        for ye in years:
            food.append(0)
            feed.append(0)

    else:
        for ye in years:
            temporal = list(data[f"{ye}"])
            food.append(temporal[0])
            feed.append(temporal[1])

    years = [str(a) for a in years]
    diccionario = {"Feed": feed, "Food":food,"Year":years}
    data = pd.DataFrame(diccionario)
    data = data.set_index("Year")
   
    return data


def paraMapa(item,year,param):
    param = str(param)
    data = loadCleanData()
    data = data[(data["Item"] == f"{item}") & (data["Element"] == f"{param}")]
    columnas = ["Area","Element",f"{year}"]
    return data[columnas]


