import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


DATASET_PATH = "datasets/HousePrices.xlsx"


def get_equation(model):
    coefficient = model.coef_[0]
    intercept = model.intercept_

    return f"{coefficient}x {'+' if intercept >= 0 else '-'} {intercept}"


def main():
    # Load dataset
    df = pd.read_excel(DATASET_PATH)

    # drop all null rows
    df = df.dropna(subset=['Distance to the nearest station', 'House Price'])

    # get x and y points
    # must be reshaped (transpose)
    x = df['Distance to the nearest station'].to_numpy().reshape((-1, 1))
    y = df['House Price'].to_numpy()

    # make a linear regression model
    model = LinearRegression().fit(x, y)

    # get score
    score = model.score(x, y)

    # get resulting equation
    equation = get_equation(model)

    print(score)
    print(equation)

    # plot points
    plt.scatter(x, y, label='Dataset points')
    plt.plot(x, model.predict(x), color='red', label='Regression line')
    plt.title(f"Linear regression for House Prices against Distance to the nearest station")
    plt.xlabel('Distance to the nearest station')
    plt.ylabel('House Price')
    plt.text(1, 1, f"Equation: {equation}\nR²: {score}")
    plt.legend()
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.show()


if __name__ == "__main__":
    main()