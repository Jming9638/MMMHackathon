# Documentation for Marketing Mix Modeling (MMM) Analysis

## Introduction

Marketing Mix Modeling (MMM) is a statistical analysis technique used to estimate the impact of various marketing activities on sales and other performance metrics, while accounting for external factors. This allows marketers to optimize their budgets by understanding which channels and campaigns deliver the highest returns. 

For this guide, we use [**Robyn**](https://facebookexperimental.github.io/Robyn/), an open-source library developed by Meta (Facebook), for implementing scalable and automated MMM. Robyn leverages Bayesian models to improve accuracy and incorporates constraints to ensure practical solutions. We'll use **R** and **RStudio** as our development environment.

---

## Prerequisites

Before starting, ensure the following prerequisites are met:

1. **Basic Knowledge**:
   - Familiarity with Marketing Mix Modeling concepts.
   - Understanding of regression analysis, time-series data, and Bayesian statistics (optional but helpful).
   - Experience with R programming.

2. **Software**:
   - **R** (version 4.0 or higher).
   - **RStudio** (latest version recommended).

3. **Data**:
   - Historical marketing data, including media spends, impressions, or clicks.
   - Business KPIs (e.g., sales, revenue, conversions).
   - Data on external factors (e.g., promotions, holidays).

4. **System Requirements**:
   - At least 8GB RAM and a multi-core processor for efficient modeling.
   - Stable internet connection to install required libraries and dependencies.

---

## Installation

Follow these steps to install the necessary tools and libraries for the MMM analysis:

### Step 1: Install R and RStudio
1. Download and install **R**:
   - Visit [CRAN R Project](https://cran.r-project.org/) and download the appropriate version for your operating system.
2. Download and install **RStudio**:
   - Visit [RStudio](https://www.rstudio.com/) and install the IDE compatible with your R installation.

### Step 2: Install packages
Robyn requires several packages to function. Open RStudio and run the following commands:

```r
# Install latest stable CRAN version
install.packages("Robyn", repos="https://cran.rstudio.com/")

# Alternative
packages <- c("ggplot2", "dplyr", "tidyr", "readr", "shiny")
install.packages(packages)

# Install latest dev version
remotes::install_github("facebookexperimental/Robyn/R")
```

### Step 3: Python Packages Installation
Robyn integrated with the Python library Nevergrad for advanced optimization. Follow these steps:
```r
# Copyright (c) Meta Platforms, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

#### Nevergrad installation guide
## ATTENTION: Python version 3.10+ version may cause Nevergrad error
## See here for more info about installing Python packages via reticulate
## https://rstudio.github.io/reticulate/articles/python_packages.html

# Install reticulate first if you haven't already
install.packages("reticulate")

#### Option 1: nevergrad installation via PIP
# 1. load reticulate
library("reticulate")
# 2. create virtual environment
virtualenv_create("r-reticulate")
# 3. use the environment created
use_virtualenv("r-reticulate", required = TRUE)
# 4. point Python path to the python file in the virtual environment. Below is
#    an example for MacOS M1 or above. The "~" is my home dir "/Users/gufengzhou".
#    Show hidden files in case you want to locate the file yourself.
Sys.setenv(RETICULATE_PYTHON = "~/.virtualenvs/r-reticulate/bin/python")
# 5. Check python path
py_config() # If the first path is not as 4, do 6
# 6. Restart R session, run #4 first, then load library("reticulate"), check
#    py_config() again, python should have path as in #4.
#    If you see: "NOTE: Python version was forced by RETICULATE_PYTHON_FALLBACK"
#    if you're using RStudio, go to Global Options > Python, and uncheck the
#    box for "Automatically activate project-local Python environments".
# 7. Install numpy if py_config shows it's not available
py_install("numpy", pip = TRUE)
# 8. Install nevergrad
py_install("nevergrad", pip = TRUE)
# 9. If successful, py_config() should show numpy and nevergrad with installed paths
# 10. Everytime R session is restarted, you need to run #4 first to assign python
#    path before loading Robyn
# 11. Alternatively, add the line RETICULATE_PYTHON = "~/.virtualenvs/r-reticulate/bin/python"
#    in the file Renviron in the the R directory to force R to always use this path by
#    default. One way to create and edit the Renviron file is to install the package "usethis" and run
#    the function usethis::edit_r_environ(). For Unix/Mac, there's also another Renviron file
#    located at path "/Library/Frameworks/R.framework/Resources/etc/". Add the line from above to this file.
#    This way, you don't need to run #4 everytime. Restart R session after editing.
```

---

### Step 4: Verify Installation
Run the following commands in RStudio to check if Robyn is properly installed:

```r
library(Robyn)

# Check Robyn version
packageVersion("Robyn")
```

---

## Usage [(Demo)](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)

Once installation is complete, follow these steps to run the MMM analysis using Robyn:

### Step 1: Prepare Your Data
1. Structure your data into a data frame with the following columns:
   - **Date**: Time-series format (**daily**, weekly, monthly).
   - **Media Spend**: Columns for each marketing channel (e.g., Google, Meta, Tiktok).
   - **Business Outcome**: Target metric like revenue or conversions.
   - **Other Factors**: Include promotions or holidays.
   
2. Save the data as a CSV or RDS file for easy access.

### Step 2: Load Robyn and Your Data
```r
library(Robyn)

# Load your dataset
data <- read.csv("path_to_your_data.csv")

# Initialize Robyn
robyn_object <- robyn_inputs(
  dt_input = data,
  # Specify other inputs like date range, media spends, and KPI
)
```

### Step 3: Run the Model
```r
# Run the MMM
model_results <- robyn_run(robyn_object)

# View outputs
robyn_outputs(model_results)
```

---

## Key Concepts

- **Adstock Transformation**: Models the delayed effect of media exposure on sales.
- **Saturation Curve**: Represents diminishing returns for increased media spend.
- **Bayesian Inference**: Adds prior distributions and ensures robust parameter estimation.

---

## Best Practices

- **Data Quality**: Ensure high-quality, complete, and accurate data for meaningful results.
- **Regular Updates**: Update models periodically with new data to maintain accuracy.
- **Granularity**: Use appropriate data granularity based on your marketing activities.
- **Validation**: Cross-validate results with holdout samples or alternative methods.

---

## Troubleshooting

1. **Installation Errors**:
   - Ensure all dependencies are installed correctly.
   - Use `install.packages` to update any outdated libraries.
   
2. **Data Issues**:
   - Validate data format and ensure no missing values.
   - Verify that column names match Robyn's expected inputs.

3. **Performance Issues**:
   - Use a machine with more RAM and processing power for faster execution.
   - Downsample data if working with very large datasets.

---
