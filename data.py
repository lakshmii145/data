import pandas as pd  
df = pd.read_csv(r'EV_Population.csv')
print(df)
df_sorted = df.sort_values(by='Model Year')
print("data sorted by model year:")
print(df_sorted)
print("latest model:")
df_lm = df['Model Year'].max()
df_latest_model = df[df['Model Year'] == df_lm]
print(df_latest_model[['Model Year','Make','Electric Vehicle Type','Electric Range']])
df_mr= df['Electric Range'].max()
df_mrg= df[df['Electric Range']==df_mr]
print("vehicles with maximum electric range ")
print(df_mrg[['Model Year','Make','Electric Range']])
df_me= df['Make'].value_counts().idxmax()
print(f"most electric vehicles are made by:{df_me}")


