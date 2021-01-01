# import json
# import pandas as pd
# import csv
# from itertools import zip_longest
#
# with open("/home/fed/Desktop/AppData/AppData/PlayStoreData/items.json") as f:
#     datas = json.load(f)
#
# list1 = []
# for data in datas[0]['names']:
#     list1.append(data)
#
# print(list1)
#
# with open('/home/fed/Desktop/AppData/AppData/PlayStoreData/items.csv', "w") as f:
#     writer = csv.writer(f)
#     # writer.writerow(("Name"))
#     writer.writerow(list1)
#
#
#
#

import pandas as pd

df = pd.read_json("/home/fed/Desktop/AppData/AppData/PlayStoreData/items.json")
df.to_csv("/home/fed/Desktop/AppData/AppData/PlayStoreData/items.csv", mode ='a', header= False, index=False)

