# Can Mathematics Predict Urban Heat? 
### Modelling the Thermal Impact of Green Infrastructure in Burwood North

This repository hosts the data analysis scripts, mathematical models, and statistical workflows used to evaluate the Urban Heat Island (UHI) mitigation efficacy of the 2026 Burwood North Metro Precinct (BNMP) Rezoning Masterplan. 

---

## Core Research Findings
* **One-Way ANOVA:** Identified statistically significant differences in Land Surface Temperature (LST) across the three microclimatic zones (**F = 71.60, p < 0.001**).
* **OLS Linear Regression:** Demonstrated a strong positive correlation between Impervious Surface Fraction (ISF) and LST (**r = 0.935, R² = 0.874**).
* **Spatial Decay Analysis:** Confirmed that the Park Cooling Effect (PCE) is strongest near the park boundary, with local morphology causing non-linear microclimatic wave patterns further down the 160m transect.

---

## Repository Architecture & Python Scripts

### 1. `microclimatic_transect_profile.py`
Plots the 160-metre continuous thermal trajectory moving away from the Burwood Park control baseline. It maps specific geographic landmarks (such as the high-density commercial "Chicken Store" zone and local urban canyons) against post-sunset LST values.

### 2. `one_way_anova_tukey.py`
Executes a One-Way Analysis of Variance (ANOVA) to evaluate the null hypothesis across Zone A (Burwood Park), Zone B (Burwood Station high-rises), and Zone C (BNMP Residential zone). Follows up with a post-hoc **Tukey HSD** test for pairwise group comparisons.

### 3. `ols_regression_residuals.py`
Constructs the Ordinary Least Squares (OLS) linear regression model mapping the predictive influence of the independent variable ISF ($X$) on the dependent variable LST ($Y$). It automatically generates diagnostic **residual analysis graphs** to mathematically validate the assumptions of homoscedasticity and linearity.

---

## Tech Stack & Environment
This project uses **Python 3** with the following scientific computing libraries:
* `statsmodels` — OLS Regression modelling & Tukey HSD pairwise test
* `scipy.stats` — Inferential statistics & One-way ANOVA calculation
* `matplotlib` & `seaborn` — Microclimatic profile plotting and residual graphics
* `pandas` & `numpy` — Array manipulation and matrix math

---

## Visual Data Profiles
### 160m Continuous Microclimatic Transect Profile
Below is the generated wave profile showing the thermal trajectory away from the parkland control baseline:

![Transect Profile](transect_wave_profile.png)

---

## Academic Integrity & AI Transparency
* **Primary Data:** Fieldwork observations, spatial grid evaluations via Google Earth satellite orthophotography, and 3-night longwave thermal re-emission measurements were captured entirely by the author.
* **Technical Implementation:** AI assistance was utilised as a programmatic tool to optimise Python syntax for data analysis and assist with LaTeX document formatting.
