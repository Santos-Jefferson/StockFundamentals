import pandas as pd
import requests
import sys

url = 'https://www.oceans14.com.br/acoes/vale/vale3/balanco-dividendos'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

dfs = pd.read_html(r.text)

print(dfs[0])
print(dfs[1])
print(dfs[2])

df_names = ['profitabiliy', 'debts', 'cashflow', 'balancesheet', 'liquidity']
dfs_after = []
for i, name in zip(range(3, len(dfs) + 1), df_names):
    print(i, name)
    dfs[i] = dfs[i].set_index([0])
    new_header = dfs[i].iloc[0]  # grab the first row for the header
    dfs[i] = dfs[i][1:]  # take the data less the header row
    dfs[i].columns = new_header  # set the header row as the df header
    name = dfs[i]
    # print(name)
    dfs_after.append(name)


# dfs[3] = dfs[3].set_index([0])
# new_header = dfs[3].iloc[0]  # grab the first row for the header
# dfs[3] = dfs[3][1:]  # take the data less the header row
# dfs[3].columns = new_header  # set the header row as the df header

# lastquote = dfs[0]
# profitabiliy = dfs[3]
# debts = dfs[4]
# cashflow = dfs[5]
# balancesheet = dfs[6]
# liquidity = dfs[7]

print(dfs_after)
