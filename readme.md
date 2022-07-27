# The Open University placement work
Code related to the Python for Data Science & Machine Learning summer placement  
## Directory structure
```
│
├── /datasets                                   // All datasets are stored here
│   ├── HousePrices.xlsx                        
│   ├── income.xlsm                             
│   ├── MercedesBensSales.xlsx                  
│   └── VaccinationByCountry.xlsx               
├── /output                                     // Output tables stored here
├── a-differenceBetweenAvgIncome.py             // Q.A: Difference between avg incomes of male/female (35-45yo inc.)
├── b-illAverageIncome.py                       // Q.B: Difference between avg income of ill people by city
├── c-totalVaccinationByCountry.py              // Q.C: Total vaccinations between 2021/01/20 - 2021/02/03 by country
├── d-fullVaccinationByCountry.py               // Q.D: Full vaccination proportion from 2021/03/05 - 2021/03/15 by country
├── e-mercedesBensAggregates.py                 // Sum/standard deviation aggregates of SL/CL sales
├── f-linearRegression.py                       // Linear regression on house price dataset
├── f2-multivariateLinearRegression.py          // Multivariate regression on house price dataset
├── funcs.py                                    // Functions shared by multiple question/python files
└── requirements.txt                            // List of all required modules to install
```

## Running the code
### Prequisites
- [Python 3](https://www.python.org) (tested on 3.10.5)
- Python's pip tool

### Setup
1. Create a virtual environment  
`python -m venv venv`
2. Activate the virtual environment  
`venv/Scripts/activate`
3. Install all required modules  
`python -m pip install -r requirements.txt`
4. Create the folder `./output`  
`mkdir output`
5. Run any python file (excluding `func.py`)

# All files
## `a-differenceBetweenAvgIncome.py`
**Dataset**: `datasets/income.xlsm`  
Determines the difference in average (median) income of males and females aged 35 - 45 years old (inclusive).  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/a.png?raw=true)
---

## `b-illAverageIncome.py`
**Dataset**: `datasets/income.xlsm`  
Visualises the different average income of ill people based on city.  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/b1.png?raw=true)  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/b2.png?raw=true)

---

## `c-totalVaccinationByCountry.py`
**Dataset**: `datasets/VaccinationByCountry.xlsx`  
Visualises the total number of vaccinations given within the period of 20th January, 2021 to 3rd February, 2021 by country.  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/c.png?raw=true)

---

## `d-fullVaccinationByCountry.py`
**Dataset**: `datasets/VaccinationByCountry.xlsx`  
Visualises the changes in proportion of full vaccinations by country from the period 5th March, 2021 to 15th March, 2021.  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/d.png?raw=true)

---

## `e-mercedesBensAggregates.py`
**Dataset**: `datasets/MercedesBensSales.xlsx`  
Calculates the sum and standard deviation aggregates for the CL and SL sales (`unit.cl`, `unit.sl`).  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/e.png?raw=true)

---

## `f-linearRegression.py`
**Dataset**: `datasets/HousePrices.xlsx`  
Makes a univariate linear regression model to predict house prices based the distance to the nearest station, plotting the regression line ontop of a scatter graph of the dataset points.  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/f.png?raw=true)

---

## `f2-multivariateLinearRegression.py`
**Dataset**: `datasets/HousePrices.xlsx`  
Makes a multivariate linear regression model to predict house prices based on the following independent variables:  
- House age  
- Distance to the nearest station  
- Number of nearby convenience stores  

The dataset is plotted on a 4D `matplotlib` graph along with the line of regression.  
![Data visualisation](https://raw.githubusercontent.com/Cyclip/open-university-placement/main/repo/f2.png?raw=true)