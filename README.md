# 🧠 Data Analyzer CLI Tool

data-analyzer (CLI tool)

A Python command-line tool for fast and efficient analysis of your CSV data - designed for cleaning, summarizing, and visualizing data.

Perfect for data analysts, automation engineers, and backend developers who work with structured tabular data.

---

## 🚀 Features

- ✅ load CSV files and validate the files
- 📊 print a simple summary (number of rows and columns, column types, nulls, duplicates, statistics)
- 🧹 unclean your data (removing nulls optional)
- 💾 save the cleaned data to a new file
- 📈 generate histograms from numerical columns
- 📉 generate bar charts from the top 10 values from categorical columns

---

## 🛠️ Tech Stack

1. Python 3.8+
2. pandas
3. matplotlib
4. argparse

---

## 🔧 Usage

Install the app dependencies:

bash
pip install -r requirements.txt

---

## Run Toola
- python main.py <filename.csv> [--dropna] [--saveclean]
