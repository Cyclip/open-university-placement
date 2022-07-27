import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from funcs import get_equation

DATASET_PATH    = "datasets/houseprices.xlsx"
COL_AGE         = 'House age'
COL_DISTANCE    = 'Distance to the nearest station'
COL_STORES      = 'Number of nearby convenience stores'
COL_PRICE       = 'House Price'
VARIABLES       = ['x', 'z', 'c']


def main():
    # load dataset
    df = pd.read_excel(DATASET_PATH)

    # drop all null rows
    df = df.dropna(subset=[COL_AGE, COL_DISTANCE, COL_STORES, COL_PRICE])

    # independent variables
    x = df[COL_AGE].to_numpy()
    z = df[COL_DISTANCE].to_numpy()
    c = df[COL_STORES].to_numpy()

    # dependent variable
    y = df[COL_PRICE].to_numpy()

    # get model x and y
    model_x = np.vstack((x, z, c)).T
    model_y = y

    # make a linear regression model
    model = LinearRegression().fit(model_x, model_y)

    # get score and equation
    score = model.score(model_x, model_y)
    equation = "y = " + get_equation(model, VARIABLES)
    print(model.coef_)

    # plot points
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # scatter map of points
    # 4th dimension represented through viridis colour map
    img = ax.scatter(x, y, z, c=c, cmap='viridis', label='Dataset points')
    fig.colorbar(img, ax=ax, label="Number of nearby convenience stores")
    
    # plot regression line
    ax.plot3D(x, model.predict(model_x), z, color='#a6a6a659', label='Regression line')

    # set title and labels
    ax.set_title(f"Multivariate linear regression for house prices\nEquation: {equation}\nR²: {score}")
    ax.set_xlabel('House Age (years)')
    ax.set_ylabel('House Price (£)')
    ax.set_zlabel('Distance to the nearest station (m)')
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()