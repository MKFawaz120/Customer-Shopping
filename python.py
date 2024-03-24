df.drop (underscore)duplicates()
to delet coulm 
df.droup('coulm name')
df
to read excel file 
pd.read(underscore)excel(r'file path')
to delete duplicates
df = df.drop(underscore)duplicates()
to clean data 
df ["coulm name"] = df ["coulm name"].str.(r\l)strip("\ or ...or ,,")
another way 
df ["coulm name"].str.strip("123.\,")
to clean numbers 
df ["coulm name"].apply(lambda x: x[0:3]+ '-' + x[3:6] + '-' + x[6:10])
df ["coulm name"].apply(lambda x: str(x))
df ["coulm name"].str.replace('what to delete', 'what to replace')
df ["coulm name"] = df ["coulm name"].str.replace('what to delete', 'what to replace')
taqseem el coulm
df[["new names of coulm"]] = df["coulm who qssem"].str.split',or mark to taqsem', num of coulm, expand = True
for loop
to find null value 
df.isnill().sum()
unique value
df.nunique()
sort values by .......
df.sort_values(by="age",ascending = False).head(20)
to show heat map for numirc
sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (10,10)
plt.show
..
filter
df[df['shopping_mall'].str.contains('Cevahir AVM','Mall of Istanbul')]


##https://github.com/MKFawaz120/Customer-Shopping.git
