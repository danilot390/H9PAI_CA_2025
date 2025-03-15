import matplotlib
matplotlib.use("Agg") # For Mac compatibility

from app.utils.utils import load_csv, load_corrected_iris
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

import io, os

def iris_summary():
    """
    Load Iris Dataset from CSV file using load_csv helper function, and display summary that contains the shape, data types, and list of Species.
    Return:
        dict that contains shape, data types, and list of species.
    """
    df = load_csv()
    df_shape = df.shape
    df_types= df.dtypes.astype(str).to_dict()
    species = df['Species'].value_counts().to_dict()

    i_summary = {
        'shape': f'The shape is {df_shape[1]}rows x  {df_shape[0]}columns',
        'columns': df_types,
        'species': species,
    }
    return i_summary

def correct_irirs_df(correct_df_path='data/iris_corrected.csv'):
    """
    Load Iris Dataset, corrected the 35th and 38th row of the dataset, and save as CSV file.
    Args:
        correct_df_path path of the correct dataset, value for default in data/ 
    Return:
        dict that contains rows 35, 38 corrected.
    """
    df = load_csv()
    df.loc[34] = [4.9, 3.1, 1.5, 0.2, 'setosa']
    df.loc[37] = [4.9, 3.6, 1.4, 0.1, 'setosa']

    df.to_csv(correct_df_path, index=False)

    return df.loc[34],df.loc[37]
    
def add_features():
    """
    Updated the sataset with two new features such as Petal Ratio and Sepal Ratio, and save as CSV file.
    Return:
        dict that contains the head (5 first rows) of the updated dataset.
    """
    correct_df_path='data/iris_corrected.csv'
    try:
        df = load_csv(correct_df_path)
    except:
        correct_irirs_df()
        df = load_csv(correct_df_path)

    df['Petal.Ratio'] = df['Petal.Length']/df['Petal.Width']
    df['Sepal.Ratio'] = df['Sepal.Length']/df['Sepal.Width']

    df.to_csv(correct_df_path, index=False)

    return df.head()

def iris_pair_wise():
    """
    Calculate the Correlation Matrix among numeric columns, dispaly and explain the positive and negative higest values.
    Return:
        bottom dict that contains the 2 lowest values and that explanation.
        top dict that contains the 2 higest values and thei explanations.
        dict that contains the Correlation Matrix of the dataset.
    """
    df = load_corrected_iris()
    numerical_cols = df.select_dtypes(include=np.number).columns
    correlations = df[numerical_cols].corr()
    
    corr_unstacked = correlations.where(~np.eye(correlations.shape[0], dtype=bool)).stack()
    top = corr_unstacked.nlargest(2)
    bottom = corr_unstacked.nsmallest(2)

    bottom = [
        {"pair": f"{idx[0]} - {idx[1]}", 
         "correlation": val} 
        for idx, val in bottom.items()
        ]

    top = [
        {"pair": f"{idx[0]} - {idx[1]}", 
         "correlation": val} 
        for idx, val in top.items()
        ]
    
    return correlations.to_dict(), top, bottom

def scatter_plot():
    """
    Graph Scatter Plot from the corrected Iris Dataset display and save as PDF file.
    Return:
        scatter plot png
    """
    df = load_corrected_iris()

    plt.figure(figsize=(8, 6))
    scatter_plot = sns.lmplot(data=df, x='Sepal.Ratio', y='Petal.Ratio', hue='Species', ci=None)

    pdf_path = 'data/iris_scatter_with_regression.pdf'
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    scatter_plot.savefig(pdf_path, format='pdf')

    img = io.BytesIO()
    scatter_plot.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return img

def pair_plot():
    """
    Graph Pair Plot from the corrected Iris Dataset display and save as PDF file.
    Return:
        Pair plot png
    """
    df = load_corrected_iris()

    plt.figure(figsize=(8,6))
    scatter_plot = sns.pairplot(df, hue='Species', vars=["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width","Petal.Ratio","Sepal.Ratio"])

    pdf_path = 'data/iris_apirplots_with_original_feaatures.pdf'
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    scatter_plot.savefig(pdf_path, format='pdf')

    img = io.BytesIO()
    scatter_plot.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return img
