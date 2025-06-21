import pandas as pd
import argparse
import sys
import matplotlib.pyplot as plt

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n✅ File loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("\n❌ File not found! Please check the file path.\n")
        sys.exit(1)
    except pd.errors.ParserError:
        print("\n❌ Error parsing the file! Please check the file format.\n")
        sys.exit(1)

def show_basic_info(df):
    print("\n✅ Basic information of the DataFrame:\n")
    print("-" * 40)
    print(f"Shape (rows*columns): {df.shape}")
    print(f"Column Names: {list(df.columns)}")
    print("\nColumn Data Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDuplicated Rows:", df.duplicated().sum())
    print("\nDescriptive Stats:\n", df.describe(include='all'))

def save_cleaned_data(df, original_path):
    cleaned_path = original_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_path, index=False)
    print(f"\n✅ Cleaned data saved as: {cleaned_path}")

def plot_visuals(df):
    print("\n📊 Generating visualizations...\n")

    # Plot histogram for numeric columns
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        df[col].hist(bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{col}_histogram.png")
        plt.close()
        print(f"✅ Saved histogram: {col}_histogram.png")

    # Bar chart for first object (categorical) column
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        col = cat_cols[0]
        plt.figure(figsize=(6, 4))
        df[col].value_counts().nlargest(10).plot(kind='bar', color='orange')
        plt.title(f"Top 10 values in {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{col}_barchart.png")
        plt.close()
        print(f"✅ Saved bar chart: {col}_barchart.png")

def main():
    parser = argparse.ArgumentParser(description="CSV Data Analyzer Tool")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("--dropna", action="store_true", help="Drop rows with missing values")
    parser.add_argument("--saveclean", action="store_true", help="Save cleaned data to a new CSV file")
    args = parser.parse_args()

    df = load_csv(args.file)
    show_basic_info(df)

    if args.dropna:
        df = df.dropna()
        print("\n🧹 Dropped rows with missing values.")
        show_basic_info(df)

    if args.saveclean:
        save_cleaned_data(df, args.file)

    plot_visuals(df)

if __name__ == "__main__":
    main()
