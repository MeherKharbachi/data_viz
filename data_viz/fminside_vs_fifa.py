# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_fminside_vs_fifa.ipynb.

# %% auto 0
__all__ = ['df_fm', 'df_fifa', 'explore_data_boxplot']

# %% ../nbs/00_fminside_vs_fifa.ipynb 3
import pandas as pd
import matplotlib.pyplot as plt

# %% ../nbs/00_fminside_vs_fifa.ipynb 5
# fminside data
df_fm = pd.read_csv("pl_fm_stats.csv")

# %% ../nbs/00_fminside_vs_fifa.ipynb 7
# fifa data
df_fifa = pd.read_csv("pl_fifa_stats.csv")

# %% ../nbs/00_fminside_vs_fifa.ipynb 10
def explore_data_boxplot(df_fm, df_fifa, columns):
    
    
    df1 = df_fm.iloc[:,14:].groupby('bucket')
    df2 = df_fifa.iloc[:,14:].groupby('bucket')

    if columns == "all":
        columns =  df1.obj.columns.drop("bucket")
    else:
        columns = [columns]
        
    for column in columns:
        # first axe; fminside data
        axes = df1.boxplot(column= column,layout=(1,9), figsize=(20,10),
                   whis=[5,95], return_type='axes')
        # second axe; fifa data
        axes2 = df2.boxplot(column=column,layout=(1,9), figsize=(20,10),
                   whis=[5,95], return_type='axes')
        # show figure
        plt.show()
