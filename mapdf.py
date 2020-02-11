import pandas as pd
from datetime import timedelta, date
import calc_date as cd

dow_map = {
    'Mon': 1,
    'Tue': 2,
    'Sun': 7,
    'Sat': 6
}

df = pd.DataFrame({'col1':['Tue 01:45PM CST', 'Mon 10:25PM CST', 'Sun 11:40PM CST', 'Sat 10:25PM CST'],
                   'col5':[5,3,6, 9],
                   'col6':[7,4,3, 10]})

print(df)

df['col1'] = df['col1'].apply(lambda x: int(dow_map[x[0:3]]))
print(df)

calc_date = cd.calc_date_factory(1, date(2020, 3, 30))
print(list(map(lambda x: calc_date(x).strftime('%d, %b %Y'), df['col1'])))
