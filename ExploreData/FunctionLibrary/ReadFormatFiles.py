import pandas as pd
from tabulate import tabulate
import calendar
import datetime as dt

def readDataframes(sheetList, path,file):
    df =[]
    for index, sheet in enumerate(sheetList):
        print("Reading {}".format(sheet))
        temp = pd.read_excel(path + file, sheet_name=sheet)
        temp['Day'] = temp['Date'].apply(lambda x: dt.datetime.weekday(x))
        temp['DayName'] = temp['Date'].apply(lambda x: dt.datetime.strftime(x, "%A"))
        temp['WeekNum'] = temp['Date'].apply(lambda x: int(dt.datetime.strftime(x, "%V")))
        temp['Month'] = pd.DatetimeIndex(temp['Date']).month
        temp['Year'] = pd.DatetimeIndex(temp['Date']).year
        temp['Quarter'] = pd.PeriodIndex(temp['Date'], freq='Q-MAR').strftime('Q%q')
        # temp['WeekDay'] = calendar.weekday(temp['Date'])
        df.append(temp)
        del temp
    return df