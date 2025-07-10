Study Hours vs Exam Score Regression

This project demonstrates how to use linear regression to analyze the relationship between hours studied and exam scores using Python. The script visualizes the data, fits a regression model, and provides useful metrics to interpret the results.

Features
Loads study hours and exam scores from a CSV file
Fits a linear regression model
Prints the regression equation
Shows the R2 score (fit quality) as a percentage
Calculates and prints the percentage increase in score per hour of study (relative to the intercept)
Plots the data and regression line, saving the plot as an image

Prerequisites
Python 3.x
Required Python packages:
  numpy
  pandas
  matplotlib
  scikit-learn

Output Explanation
Regression equation: Shows how the predicted exam score changes with each additional hour studied.
R2 score: Indicates how well the model fits the data (closer to 100 means a better fit).
Percentage increase in score per hour of study: How much the score increases per hour, relative to the intercept.
Plot: Visualizes the actual data points and the regression line.

Example Output
Regression equation: score = 9.90 hours + 1.86
Percentage increase in score per hour of study (relative to intercept): 531.31%
R2 score: 98.14%

