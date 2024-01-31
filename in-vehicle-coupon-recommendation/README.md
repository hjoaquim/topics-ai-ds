# In-Vehicle Coupon Recommendation

This project aims to provide a recommendation system for in-vehicle coupons. It utilizes predictive analysis techniques to generate recommendations based on user preferences.

## Project Setup

To reproduce this project, follow these steps:

> [!TIP]
> Create a new virtual environment for this project before installing the dependencies.

1. Install [Poetry](https://python-poetry.org/), a dependency management tool for Python.

2. Clone the project repository:

    ```shell
    git clone https://github.com/hjoaquim/topics-ai-ds.git
    ```

3. Navigate to the project directory:

    ```shell
    cd in-vehicle-coupon-recommendation
    ```

4. Install the project dependencies using Poetry:

    ```shell
    poetry install
    ```

    This will create a virtual environment and install all the required dependencies specified in the `pyproject.toml` file.

## Predictive Analysis

The predictive analysis for this project was performed in the `analysis.ipynb` notebook. It contains the code for training and evaluating the recommendation model.

## Generating the Report

To generate the report in a data science fashion, we leverage the `analysis.ipynb` notebook and use `nbconvert` to convert it to a report format (e.g., HTML, PDF, etc.). The notebook includes markdown cells and code cells that can be executed to generate the report.

Find the report: `analysis.pdf`
