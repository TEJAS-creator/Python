# Input numbers into a list
numbers = []
n = int(input("How many numbers do you want to enter? "))

for _ in range(n):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Calculations
largest = max(numbers)
smallest = min(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)

# Count occurrences of a specific number
specific_number = float(input("Enter a number to count its occurrences: "))
occurrences = numbers.count(specific_number)

# Display results
print("\nResults:")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of numbers: {total_sum}")
print(f"Average of numbers: {average:.2f}")
print(f"Occurrences of {specific_number}: {occurrences}")


# Create a tuple with five elements
my_tuple = (1, 2, 3, 4, 5)

try:
    # Attempt to change one of the elements
    my_tuple[1] = 10
except TypeError as e:
    # Handle the error and explain why it occurred
    print("Error:", e)
    print("Explanation: Tuples are immutable, meaning their elements cannot be changed after the tuple is created.")


# Create a dictionary of cricket World Cup winners
world_cup_winners = {
    1975: "West Indies",
    1979: "West Indies",
    1983: "India",
    1987: "Australia",
    1992: "Pakistan",
    1996: "Sri Lanka",
    1999: "Australia",
    2003: "Australia",
    2007: "Australia",
    2011: "India",
    2015: "Australia",
    2019: "England"
}

# Count the number of wins for each country
win_count = {}
for year, country in world_cup_winners.items():
    win_count[country] = win_count.get(country, 0) + 1

# Find the best-performing country
best_country = max(win_count, key=win_count.get)

# Get the unique list of countries that have won the World Cup
unique_countries = set(world_cup_winners.values())

# Display results
print("Best-performing country:", best_country)
print("Unique list of countries that have won the World Cup:", unique_countries)


# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the frequency of each word
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Display the dictionary
print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")


# Input numbers into the first set
set1 = set()
n1 = int(input("How many numbers do you want to add to the first set? "))
print("Enter numbers for the first set:")
for _ in range(n1):
    num = int(input())
    set1.add(num)

# Input numbers into the second set
set2 = set()
n2 = int(input("How many numbers do you want to add to the second set? "))
print("Enter numbers for the second set:")
for _ in range(n2):
    num = int(input())
    set2.add(num)

# Perform set operations
union_result = set1 | set2
intersection_result = set1 & set2
difference_result = set1 - set2

# Display results
print("\nSet Operations Results:")
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")
print(f"Difference (Set1 - Set2): {difference_result}")


import numpy as np

# Generate a 3x4 NumPy array with random integers between 1 and 50
array = np.random.randint(1, 51, size=(3, 4))
print("Original 3x4 Array:")
print(array)

# a. Calculate and print the Mean, Median, and Standard Deviation
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)

print("\nStatistics:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

# b. Print the Sum of all elements and the sum of each row
total_sum = np.sum(array)
row_sum = np.sum(array, axis=1)

print("\nSum Results:")
print(f"Sum of all elements: {total_sum}")
print(f"Sum of each row: {row_sum}")

# c. Reshape the 3x4 array into a 2x6 array and print it
reshaped_array = array.reshape(2, 6)
print("\nReshaped 2x6 Array:")
print(reshaped_array)


import numpy as np

# Create two (3x3) matrices using NumPy
matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# a. Matrix addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# b. Matrix subtraction
subtraction = matrix1 - matrix2
print("\nMatrix Subtraction:")
print(subtraction)

# c. Matrix multiplication (element-wise and dot product)
elementwise_multiplication = matrix1 * matrix2
dot_product = np.dot(matrix1, matrix2)

print("\nElement-wise Multiplication:")
print(elementwise_multiplication)
print("\nDot Product:")
print(dot_product)

# d. Transpose of a matrix
transpose_matrix1 = matrix1.T
print("\nTranspose of Matrix 1:")
print(transpose_matrix1)

# e. Determinant and inverse (if applicable)
det_matrix1 = np.linalg.det(matrix1)
det_matrix2 = np.linalg.det(matrix2)

print("\nDeterminant:")
print(f"Determinant of Matrix 1: {det_matrix1}")
print(f"Determinant of Matrix 2: {det_matrix2}")

# Compute the inverse if the determinant is non-zero
if det_matrix1 != 0:
    inverse_matrix1 = np.linalg.inv(matrix1)
    print("\nInverse of Matrix 1:")
    print(inverse_matrix1)
else:
    print("\nMatrix 1 is singular, inverse does not exist.")

if det_matrix2 != 0:
    inverse_matrix2 = np.linalg.inv(matrix2)
    print("\nInverse of Matrix 2:")
    print(inverse_matrix2)
else:
    print("\nMatrix 2 is singular, inverse does not exist.")


import pandas as pd

# Create a Series from a list of daily temperatures
temperatures = pd.Series([22, 24, 19, 21, 25, 20, 23], 
                         index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

print("Daily Temperatures (Celsius):")
print(temperatures)

# a. Find and print the average (mean) temperature for the week
average_temp = temperatures.mean()
print(f"\nAverage Temperature for the Week: {average_temp:.2f}°C")

# b. Identify and print the maximum and minimum temperatures and their respective days
max_temp = temperatures.max()
min_temp = temperatures.min()
max_day = temperatures.idxmax()
min_day = temperatures.idxmin()

print(f"\nMaximum Temperature: {max_temp}°C on {max_day}")
print(f"Minimum Temperature: {min_temp}°C on {min_day}")

# c. Display the temperatures greater than a specific value
specific_value = 22
temps_greater_than_value = temperatures[temperatures > specific_value]

print(f"\nTemperatures Greater Than {specific_value}°C:")
print(temps_greater_than_value)

# d. Convert all temperatures to Fahrenheit
temperatures_fahrenheit = temperatures * 9/5 + 32

print("\nTemperatures in Fahrenheit:")
print(temperatures_fahrenheit)

# e. Print the days with temperatures above the average
above_average_days = temperatures[temperatures > average_temp]

print("\nDays with Temperatures Above Average:")
print(above_average_days)


import pandas as pd

# Create a DataFrame with student details
data = {
    'Roll Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'M'],
    'Marks1': [85, 56, 78, 45, 67, 90, 88, 66, 54, 72],
    'Marks2': [45, 56, 32, 78, 89, 23, 45, 90, 67, 39],
    'Marks3': [78, 92, 88, 76, 65, 70, 85, 60, 72, 81]
}

df = pd.DataFrame(data)

print("Student Details DataFrame:")
print(df)

# a. Create a new column with total marks
df['Total Marks'] = df['Marks1'] + df['Marks2'] + df['Marks3']

# b. Find the lowest marks in Marks1
lowest_marks1 = df['Marks1'].min()
print(f"\nLowest Marks in Marks1: {lowest_marks1}")

# c. Find the highest marks in Marks2
highest_marks2 = df['Marks2'].max()
print(f"Highest Marks in Marks2: {highest_marks2}")

# d. Find the average marks in Marks3
average_marks3 = df['Marks3'].mean()
print(f"Average Marks in Marks3: {average_marks3:.2f}")

# e. Find student name with the highest average
df['Average'] = df[['Marks1', 'Marks2', 'Marks3']].mean(axis=1)
top_student = df.loc[df['Average'].idxmax()]['Name']
print(f"\nStudent with the Highest Average Marks: {top_student}")

# f. Find how many students failed in Marks2 (<40)
failed_students = df[df['Marks2'] < 40].shape[0]
print(f"\nNumber of Students Failed in Marks2 (Marks < 40): {failed_students}")


# Create CSV files
import pandas as pd

# Movie data
movies_data = {
    'Movie Name': ['Dilwale', '3 Idiots', 'Kabir Singh', 'PK', 'Lagaan', 
                   'Sholay', 'Kahaani', 'Jab Tak Hai Jaan', 'Zindagi Na Milegi Dobara', 'Dangal'],
    'Language': ['Hindi', 'Hindi', 'Hindi', 'Hindi', 'Hindi', 
                 'Hindi', 'Hindi', 'Hindi', 'Hindi', 'Hindi'],
    'Genre': ['Romance', 'Drama', 'Romance', 'Comedy', 'Drama', 
              'Action', 'Thriller', 'Romance', 'Drama', 'Drama'],
    'Rating': [7.5, 8.4, 7.1, 8.3, 8.1, 
               8.2, 8.0, 7.8, 8.1, 8.6],
    'Review': ['Good movie', 'Excellent', 'Average', 'Great', 'Inspirational', 
               'Legendary', 'Thrilling', 'Romantic', 'Entertaining', 'Inspirational']
}


# Reading CSV file
# Create DataFrame and write it to a CSV file
df_movies = pd.DataFrame(movies_data)
df_movies.to_csv('Movies.csv', index=False)

print("Movies.csv file has been created successfully.")


# Read the CSV file into a DataFrame
df_movies = pd.read_csv('Movies.csv')

# a. Find the movie with the highest rating
highest_rated_movie = df_movies.loc[df_movies['Rating'].idxmax()]

print("\nMovie with the Highest Rating:")
print(highest_rated_movie)

# b. Write the details of all Hindi movies into a file "HindiMovies.csv"
hindi_movies = df_movies[df_movies['Language'] == 'Hindi']
hindi_movies.to_csv('HindiMovies.csv', index=False)

print("\nHindiMovies.csv file has been created with all Hindi movie details.")


