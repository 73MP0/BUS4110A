import pandas as pd

xl = pd.ExcelFile("SalesDataFull.xlsx")
profits = xl.parse("Orders")
df = profits.copy()



headers = list(df.columns.values)
dateHeaders = headers[3:4]

for head in headers[:16]:
    if head in dateHeaders:
        df[head] = pd.to_datetime(df[head])


        
products = df[["Product Name", "Profit", "Order Date"]]
topProducts = products.sort_values(by="Profit" , ascending=False,)
yearFilter = topProducts.loc[topProducts["Order Date"].dt.year == 2016]
quarters = yearFilter.loc[yearFilter["Order Date"].dt.quarter.unique()]
count = 0
lines = "=" * 80





for quarter in quarters:
    topProdQtr = yearFilter.loc[yearFilter["Order Date"].dt.quarter == count]
    print(topProdQtr.head(10))
    print(lines)
    count = count + 1




uYear = "2017-01-01"
iYear = "2016"

