# Tissue Spatial Geometrics Lab (www.TSG-Lab.org)
# David H. Nguyen PhD; Mihir Kalyanthaya MS

###### Instructions ######
# 0. This script was written to be run in VSCode or an IDE that allows
#    interactive graphical pop-up windows.
# 1. The input file should be a CSV file that is formatted as seen below. 
# 2. The csv file MUST contain a column that has labels for each category. The name of this column
#    must be speclled as "Category".
#      -Example of Categories: Dog, Cat, CarType, FavoriteFood, etc.
#      -If you don't have any categories, then the rows in this column should have some word, 
#       like "NA". The rows of this column should not be empty.
# 3. Paste in the file path to the working directory in Step 1.
# 4. Paste in the name of the input file in Step 2. Then run the whole script. 
#
# The input file should be formatted like this: 
#  
#  Category   Sample_Name    PC1     PC2     PC3
#  Dog        Woofy         0.2     0.3     0.1
#  Dog        Spikey        0.3     0.2     0.8
#  Cat        Tinker        0.04    0.1     0.03
#  Cat        Whiskas       0.07    0.11    0.06
#
######

# Load the dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import plotly.express as px

# Step 1. Load the CSV file
file_path = r'/Users/davidnguyen/Documents/demo2/Practice Files/LCPC Data for Practicing PCA_1st3PCvalues_CorrectlyFormatted_AD.csv'

df = pd.read_csv(file_path)

# Copy dataframe so original PCA values stay unchanged
df_plot = df.copy()

# Add tiny jitter only to plotting coordinates in case of data overlap
jitter_strength = 0.1

df_plot["PC1_plot"] = df_plot["PC1"] + np.random.normal(0, jitter_strength, size=len(df_plot))
df_plot["PC2_plot"] = df_plot["PC2"] + np.random.normal(0, jitter_strength, size=len(df_plot))
df_plot["PC3_plot"] = df_plot["PC3"] + np.random.normal(0, jitter_strength, size=len(df_plot))
fig = px.scatter_3d(
    df_plot,
    x="PC1",
    y="PC2",
    z="PC3",
    color="Category",
    hover_name="Sample_Name",
    hover_data={
        "Category": True,
        "PC1": True,
        "PC2": True,
        "PC3": True,
        "PC1_plot": False,
        "PC2_plot": False,
        "PC3_plot": False
    },
    title="Name of Graph"
)

fig.update_traces(
    marker=dict(
        size=4, # This changes the size of the dots
        line=dict(width=1, color="black")
    )
)

fig.show()
