import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where( (df['weight'] / (df['height'] * 0.01) ** 2) > 25, 1, 0)

# Normalize data
df.loc[(df['cholesterol'] == 1),'cholesterol'] = 0
df.loc[(df['cholesterol'] > 1),'cholesterol'] = 1
df.loc[(df['gluc'] == 1),'gluc'] = 0
df.loc[(df['gluc'] > 1),'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot
    df_cat = df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio' and show the counts of each feature
    df_cat['total'] = np.random.randn()
    df_cat = df_cat.groupby(['variable', 'cardio', 'value'], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(
    x = 'variable', 
    y = 'total', 
    hue = 'value', 
    data = df_cat, 
    col = 'cardio', 
    kind = 'bar')

    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Cleaning the data
    mask1 = (df['ap_lo'] <= df['ap_hi'])
    mask2 = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    mask3 = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df[mask1 & mask2 & mask3]

    # the correlation matrix
    corr_mtrx = df_heat.corr()

    # the upper triangle mask
    mask = np.triu(np.ones(corr_mtrx.shape),0)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(
                    data=corr_mtrx,
                    cmap='coolwarm',
                    vmin = -0.1,
                    vmax = 0.25,
                    center = 0,
                    robust=True,
                    annot = True,
                    fmt = '.1f',
                    square = True,
                    mask=mask)

    fig.savefig('heatmap.png')
    return fig
