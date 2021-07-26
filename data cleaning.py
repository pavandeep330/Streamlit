import pandas as pd
data = pd.read_csv(r"C:/Users/Pavan Deep/Desktop/ipl_data/IPL Ball-by-Ball 2008-2020.csv")
df = pd.DataFrame(data, index = None)
result = df.sort_values(by = ['id','inning','over','ball'])
result.to_csv(r'C:\Users\Pavan Deep\Desktop\ipl_data\cleaned.csv', index = False)
print(result)