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
    data = loadCleanData()
    dfarea = {"Area":data.Area.unique()}
    data1 = pd.DataFrame(dfarea)
    dfitem = {"Item":data.Item.unique()}
    data2 = pd.DataFrame(dfitem)

    if param == "Item":
        return data2["Item"]
    else:
        return data1["Area"]