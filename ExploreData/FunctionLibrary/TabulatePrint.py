from tabulate import tabulate

def tabulatePrint(df):
    print(tabulate(df,headers = 'keys', tablefmt='psql'))