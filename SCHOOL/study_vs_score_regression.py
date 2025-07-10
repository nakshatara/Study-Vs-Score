# Linear Regression: Study Hours vs Exam Score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset from CSV
import os
csv_path = os.path.expanduser(r'C:/Users/V1/Desktop/score_updated.csv')
try:
    data = pd.read_csv(csv_path)
    hours = data['Hours'].values.reshape(-1, 1)
    scores = data['Scores'].values
except FileNotFoundError:
    print(f"CSV file not found at {csv_path}. Please check the path and try again.")
    exit(1)

# Create and fit the model
model = LinearRegression()
model.fit(hours, scores)

# Predict scores
predicted_scores = model.predict(hours)

# Print regression equation and R^2
print(f"Regression equation: score = {model.coef_[0]:.2f} * hours + {model.intercept_:.2f}")
# Percentage increase in score per hour of study (relative to intercept)
if model.intercept_ != 0:
    percentage_increase_per_hour = model.coef_[0] / abs(model.intercept_) * 100
    print(f"Percentage increase in score per hour of study (relative to intercept): {percentage_increase_per_hour:.2f}%")
else:
    print("Intercept is zero, cannot compute percentage increase per hour of study.")
r2 = r2_score(scores, predicted_scores)
print(f"R^2 score: {r2*100:.2f}%")

# Plot
plt.scatter(hours, scores, color='blue', label='Actual Scores')
plt.plot(hours, predicted_scores, color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score (Linear Regression)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot as image
plot_path = os.path.join(os.path.dirname(__file__), 'regression_plot.png')
plt.savefig(plot_path)
print(f"Plot saved as: {plot_path}")
plt.show()
