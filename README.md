# Business KPI Performance Summary

## Project Overview

This project uses Python and Pandas to analyse a sample wholesale business dataset and generate a Key Performance Indicator (KPI) summary.

It compares business performance between September 2026 and October 2026 and generates plain-language explanations to help management understand business performance.

## KPIs Analysed

1. Total Revenue
2. Total Orders
3. Average Order Value
4. Gross Profit
5. Gross Profit Margin

## Key Features

- Loads sales data from a CSV file.
- Calculates revenue, cost and gross profit.
- Compares two reporting periods.
- Calculates percentage changes.
- Classifies KPI performance.
- Generates plain-language business explanations.
- Exports the KPI summary to CSV.

## Technologies Used

- Python
- Pandas
- pathlib

## Project Structure

```text
business_kpi_summary/
├── data/
│   └── sales_data.csv
├── output/
│   └── kpi_summary.csv
├── kpi_analysis.py
└── README.md
```

## How to Run

1. Clone this repository.
2. Open the project folder in VS Code.
3. Install Pandas:

```powershell
pip install pandas
```

4. Run the analysis:

```powershell
python kpi_analysis.py
```

5. Find the generated report in:

`output/kpi_summary.csv`

## Reporting Periods

- Previous period: September 2026
- Current period: October 2026

## Project Purpose

This project demonstrates how Python can automate business performance reporting and transform raw sales data into meaningful management insights.