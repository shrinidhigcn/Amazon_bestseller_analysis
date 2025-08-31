# Amazon Top 50 Bestselling Books Analysis

This project performs a data analysis on the Amazon Top 50 Bestselling Books dataset, which contains information on the top-selling books from 2009 to 2019. The analysis is conducted using the pandas library in Python.

## 📖 Dataset

The dataset used is `bestsellers.csv`, which includes the following columns:
- `Name`
- `Author`
- `User Rating`
- `Reviews`
- `Price`
- `Year`
- `Genre`

## 🔬 Analysis Performed

The `main.py` script performs the following data cleaning and analysis steps:

1.  **Data Loading & Inspection**: Loads the dataset and performs an initial inspection to understand its structure, columns, and basic statistics.
2.  **Data Cleaning**:
    - Removes any duplicate rows to ensure data integrity.
    - Standardizes column names for better readability and easier access (e.g., `Name` -> `Title`, `User Rating` -> `Rating`).
    - Converts the `Price` column to a numeric (float) data type for calculations.
3.  **Data Analysis**:
    - Calculates the number of bestselling books for each author and identifies the top authors.
    - Computes the average user rating for each book genre (Fiction and Non-Fiction).
4.  **Data Export**:
    - Exports the list of the top 10 authors to `top_authors.csv`.
    - Exports the average ratings by genre to `avg_rating_by_genre.csv`.

## 🚀 How to Run

To run this analysis on your own machine, follow these steps.

### Prerequisites

- Python 3.x
- pandas library

### Installation

1.  Clone or download this repository.
2.  Install the required Python package:
    ```sh
    pip install pandas
    ```

### Execution

Run the main script from your terminal:

```sh
python main.py
```

The script will print summary statistics to the console and generate two new CSV files in the project directory.

## 📂 Files in this Repository

- `main.py`: The main Python script containing the data analysis code.
- `bestsellers.csv`: The raw input dataset.
- `top_authors.csv`: **(Generated)** A CSV file listing the top 10 authors with the most bestsellers.
- `avg_rating_by_genre.csv`: **(Generated)** A CSV file showing the average user rating for Fiction vs. Non-Fiction books.
