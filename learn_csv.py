import pandas as pd

# Reading the CSV file
a = pd.read_csv("cars.csv")  # Reads the CSV file into a DataFrame

# Display the DataFrame
print(a)  # Prints the entire DataFrame

# Basic DataFrame information
print(a.info())  # Displays information about the DataFrame (column names, non-null counts, data types)

# Statistical summary of numerical columns
print(a.describe())  # Generates summary statistics (count, mean, std, min, max, etc.)

# Checking for missing values in each column
print(a.isnull().sum())  # Returns the number of missing values per column

# Display the first few rows of the DataFrame
print(a.head())  # Displays the first 5 rows of the DataFrame

# Display the last few rows of the DataFrame
print(a.tail())  # Displays the last 5 rows of the DataFrame

# Checking the shape of the DataFrame
print(a.shape)  # Returns the number of rows and columns in the DataFrame as a tuple (rows, columns)

# Checking column names
print(a.columns)  # Lists all column names in the DataFrame

# Displaying unique values in a specific column
print(a["column_name"].unique())  # Replace "column_name" with the actual column name to get unique values

# Counting unique values in a column
print(a["column_name"].nunique())  # Returns the number of unique values in the column

# Sorting the DataFrame by a column
print(a.sort_values(by="column_name"))  # Sorts the DataFrame based on the values of a specified column

# Sorting in descending order
print(a.sort_values(by="column_name", ascending=False))  # Sorts in descending order

# Selecting a specific column
print(a["column_name"])  # Prints the values of a specific column

# Selecting multiple columns
print(a[["column1", "column2"]])  # Replace with actual column names

# Filtering rows based on a condition
print(a[a["column_name"] > 100])  # Returns rows where values in "column_name" are greater than 100

# Replacing values in a column
a["column_name"] = a["column_name"].replace("old_value", "new_value")  # Replaces old_value with new_value

# Dropping missing values
a = a.dropna()  # Removes rows with missing values

# Filling missing values with a specific value
a = a.fillna(0)  # Replaces all missing values with 0

# Renaming columns
a = a.rename(columns={"old_name": "new_name"})  # Renames a column

# Grouping data by a column and aggregating
print(a.groupby("column_name").mean())  # Groups by a column and calculates the mean

# Merging two DataFrames
b = pd.read_csv("other_data.csv")  # Another DataFrame
merged_df = a.merge(b, on="common_column")  # Merges both DataFrames on a common column

# Concatenating DataFrames
concatenated_df = pd.concat([a, b])  # Stacks the DataFrames together

# Resetting index
a = a.reset_index(drop=True)  # Resets the index of the DataFrame

# Setting a new index
a = a.set_index("column_name")  # Sets a column as the new index

# Checking for duplicate rows
print(a.duplicated().sum())  # Returns the number of duplicate rows

# Dropping duplicate rows
a = a.drop_duplicates()  # Removes duplicate rows

# Saving the modified DataFrame to a CSV file
a.to_csv("cleaned_cars.csv", index=False)  # Saves the DataFrame as a CSV file without the index

# Read csv from url
url = "https://example.com/data.csv"
a = pd.read_csv(url)

chunk_size = 5  # Define the number of rows in each chunk
for chunk in pd.read_csv("cars.csv", chunksize=chunk_size):
    print(chunk.head())  # Process each chunk separately

total_rows = 0
for chunk in pd.read_csv("cars.csv", chunksize=5):
    total_rows += len(chunk)  # Count rows in each chunk
print("Total rows:", total_rows)



