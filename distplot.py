import seaborn as sns

sex_list = df['Sex'].unique()
for x in sex_list:
    sns.distplot(df[df['Sex']==x]['Pclass'], 
                 kde_kws={'bw':1, 'linewidth': 3}, label = x)
