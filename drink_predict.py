import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('drinks.csv')
df.set_index('country',inplace=True)
print "\nPRINT ALL COLUMNS IN DATAFRAME : {}".format(df.columns)
print "\n PRINT ALL DATAFRAME : \n",df


print "\nDimentions of data : {}".format(df.shape)

df = df[(df['beer_servings']>50)&(df['spirit_servings']>50)&(df['wine_servings'])&(df['total_litres_of_pure_alcohol']>1.)]
print "\n PRINT ALL DATAFRAME_With_condition : \n",df

print "\n\n\n\n Dataframe info : ",df.info()
for col in df:
    print "\nPRINT COLUMNS IN DATAFRAME : ",col

df_10_rows = df.head(10)
print "\nPRINT FIRST 10 ROWS : \n",df_10_rows

df_10_last_rows = df.tail(10)
print "\nPRINT LAST 10 ROWS: \n ",df_10_last_rows

df_desc = df.describe()
print "\nDescribe OF DATAFRAME : {}".format(df_desc)

df_max_beer = df.iloc[0:,[0]].max()
print "\nMax of beer : ",df_max_beer



df_max_spirit = df.iloc[0:,[1]].max()
print "\nMax of spirit : ",df_max_spirit


df_max_wine = df.iloc[0:,[2]].max()
print "\nMax of wine : ",df_max_wine



df_max_pure_alcohal = df.iloc[0:,[3]].max()
print "\nMax of total alcohal : ",df_max_pure_alcohal


print "\n\n\n\n\n\n\n\n\n\n"
plot_graph_country_tot_alcohal = df.iloc[0:,[3]]
plot_graph_country_beer = df.iloc[0:,[0]]
plot_graph_country_wine = df.iloc[0:,[2]]
plot_graph_country_spirit = df.iloc[0:,[1]]
plot_all_with_country = df.iloc[0:,[0,1,2,3]]

print "\n\n\n\nPLOT A GRAGH FOR COUNTRY AND BEER SERVING : \n"

p1 = plot_graph_country_tot_alcohal.plot.bar()
p1.set_title('Total alcohol consumption in country')

p2 = plot_graph_country_beer.plot.bar()
p2.set_title('Total beer consumption in country')

p3 = plot_graph_country_spirit.plot.bar()
p3.set_title('Total spirit consumption in country')


p4 = plot_graph_country_wine.plot.bar()
p4.set_title('Total wine consumption in country')

p5 = df_desc.plot.bar()
p5.set_title('Statistics of drink consumption in country')

p6 = plot_all_with_country.plot.box()
p6.set_title('Total drink consumption in country')

plt.show()












