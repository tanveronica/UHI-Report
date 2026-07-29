# Modelling Urban Heat: LST vs ISF in Burwood North

This is the repository for my high school research project. I investigated how urban development and concrete surfaces affect local temperatures around the Burwood North Metro Precinct rezoning area, using Burwood Park as a baseline.

## My Core Results

* Zone Differences: A One-Way ANOVA proved there is a significant difference in temperature across my three fieldwork zones (F = 71.60, p < 0.001).
* Concrete vs Heat: OLS Linear Regression showed a really strong link between Impervious Surface Fraction (ISF) and Land Surface Temperature (LST), with an R² of 0.874.
* Park Cooling Effect: My 160m transect data showed that while the park cools the immediate area, local buildings and shops create a non-linear "wave" pattern further away.

## The Python Scripts

* microclimatic_transect_profile.py: Plots my 160m walk data and labels real landmarks like the Burwood Park boundary and the local commercial buildings.
* one_way_anova_tukey.py: Runs the ANOVA and a follow-up Tukey HSD test to compare the three zones.
* ols_regression_residuals.py: Builds the linear regression model and plots the residual graphs to check my statistical assumptions.

## Libraries Used

I used Python 3 along with pandas, numpy, matplotlib, seaborn, scipy.stats, and statsmodels.

## My Transect Graph

![Transect Profile](transect_wave_profile.png)

## Project Notes and AI Disclosure

I collected all the temperature data myself during fieldwork over three evenings in May 2026, and mapped the surface grids using Google Earth. I used AI as a tool to help me clean up my matplotlib code, structure the statsmodel library syntax, and fix my LaTeX document formatting.
