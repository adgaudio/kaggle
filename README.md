kaggle
======

# Data Transformation

## Create dummy variables
* Site --> a variable for each site.
* Weekday --> a variable for each day.

## Lag timeseries
First test each variable for autoregression. They will almost certainly be autoregressive, but we are unsure how much. We are looking for a threshold at which point older values are not statistically significant after controlling for more recent values.

After we have established that threshold, create a set of lagged variables for each timeseries variable. Each original column will be transformed into X lagged columns based on position within chunk, where X is the threshold hour. This will reduce the number of observations available, but it is likely that we will gain more information than we lose.

## Linearize
For any non-normal weather variable, take the log.

## Estimate missing values
Fill in points by averaging nearest 2 times. Fill in segments by copying nearest site.


# Model fitting

## Ordinary Least Squares
Form a baseline by using OLS on the complete set of variables (including lagged and dummy variables)

## Dimensionality reduction

## 

# Visualization

Use gapminder.org style animation