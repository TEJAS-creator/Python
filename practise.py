number = []
a = int(input("Enter the amt of numbers: "))
for i in range(a):
    num = int(input("Enter the numbers: "))
    number.append(num)
print(number)

largest=max(number)
smallest=min(number)
total=sum(number)
average=total/len(number)

print("-----------------------------------------")

print("Largest number: ",largest)
print("Smallest number: ",smallest)
print("Total number: ",total)
print("Average : ",average)

specific = int(input("Enter the number to count: "))
n=number.count(specific)
print("Occurrences of ",specific,": ",n)




sentence = input("Enter the sentence: ")
new = sentence.split()
words = {}

for i in new:
    words[i]=words.get(i,0)+1

print("\nWord Frequency:")
for i, count in words.items():
    print(f"{i}: {count}")




import numpy as np

array = np.random.randint(1,10,size=(3,4))
print(array)

a = np.mean(array)
b = np.median(array)
c = np.std(array)
d = np.sum(array)
e = np.sum(array,axis=1)
f = array.reshape(2,6)

print("\n",a)
print("\n",b)
print("\n",c)
print("\n",d)
print("\n",e)
print("\n",f)




import numpy as np

mat1 = np.random.randint(1,10,size=(3,3))
mat2 = np.random.randint(1,10,size=(3,3))
print(mat1)
print(mat2)

a = mat1+mat2
b = mat1-mat2
c = mat1*mat2
d = np.dot(mat1,mat2)
e = np.linalg.det(mat1)
f = np.linalg.det(mat2)

print("\n",a)
print("\n",b)
print("\n",c)
print("\n",d)
print("\n",e)
print("\n",f)

if e!=0:
    print("\n",np.linalg.inv(mat1))
else:
    print("Inverse not possible")
if e!=0:
    print("\n",np.linalg.inv(mat2))
else:
    print("Inverse not possible")





import pandas as pd 

temperatures = pd.Series([20,30,40,50],index=["monday","tuesday","wednesday","thursday"])
print("Daily Temperatures:\n")
print(temperatures)

print("Average temperature: ",temperatures.mean())
print("Max temperature: ",temperatures.max()," on ",temperatures.idxmax())
print("Min temperature: ",temperatures.min()," on ",temperatures.idxmin())

specific = int(input("Enter the temperature: "))
temp_greater = temperatures[temperatures>specific]
print("\nTemperature greater than ",specific,"is: \n",temp_greater)
print("\nTemperature in Fahrenheit: \n",temperatures*9/5+32)




import pandas as pd

data = {
    'Roll Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'M'],
    'Marks1': [85, 56, 78, 45, 67, 90, 88, 66, 54, 72],
    'Marks2': [45, 56, 32, 78, 89, 23, 45, 90, 67, 39],
    'Marks3': [78, 92, 88, 76, 65, 70, 85, 60, 72, 81]
}
df = pd.DataFrame(data)
print(df)

df["Total"]=df["Marks1"]+df["Marks2"]+df["Marks3"]
print()
print(df["Total"])

lowest = df['Marks1'].min()
highest = df['Marks1'].max()
average = df['Marks1'].mean()
failed_student = df[df['Marks2'] < 40].shape[0]

df['Average'] = df[['Marks1', 'Marks2', 'Marks3']].mean(axis=1)
top_student = df.loc[df['Average'].idxmax()]['Name']

print("Lowest marks 1: ",lowest)
print("Highest marks 1: ",highest)
print("Average marks 1: ",average)
print("Topper: ",top_student)
print("Failed student in marks 2: ",failed_student)





import pandas as pd
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

df_movies = pd.DataFrame(movies_data)
df_movies.to_csv('Movies.csv', index=False)
print("Movies.csv file has been created successfully.")

df_movies = pd.read_csv('Movies.csv')
highest_rated_movie = df_movies.loc[df_movies['Rating'].idxmax()]
print("\nMovie with the Highest Rating:",highest_rated_movie)

hindi_movies = df_movies[df_movies['Language'] == 'Hindi']
hindi_movies.to_csv('HindiMovies.csv', index=False)
print("\nHindiMovies.csv file has been created with all Hindi movie details.")





import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("anime.csv")

# Remove rows with missing important values
df = df.dropna(subset=['Ratings', 'Budget (in Million USD)', 'Release Year'])

# Convert necessary columns to numbers
df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')
df['Budget (in Million USD)'] = pd.to_numeric(df['Budget (in Million USD)'], errors='coerce')
df['Release Year'] = df['Release Year'].astype(int)

# Convert text columns to strings and fill missing values
df['Anime Name'] = df['Anime Name'].astype(str)
df['Genre'] = df['Genre'].astype(str)
df['Animation Studio Name'] = df['Animation Studio Name'].astype(str)

# --- 1. Top Rated Anime ---
top_rated = df.nlargest(10, 'Ratings')
plt.figure(figsize=(10, 5))
plt.barh(top_rated['Anime Name'], top_rated['Ratings'], color='blue')
plt.xlabel('Ratings')
plt.ylabel('Anime Name')
plt.title('Top 10 Highest Rated Anime')
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()

# --- 2. Most Common Genres ---
top_genres = df['Genre'].value_counts().head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_genres.index, top_genres.values, color='green')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.title('Top 10 Most Common Anime Genres')
plt.gca().invert_yaxis()
plt.show()

# --- 3. Anime with Most Episodes ---
most_episodes = df.nlargest(10, 'Number of Episodes')
plt.figure(figsize=(10, 5))
plt.barh(most_episodes['Anime Name'], most_episodes['Number of Episodes'], color='red')
plt.xlabel('Number of Episodes')
plt.ylabel('Anime Name')
plt.title('Top 10 Anime with Most Episodes')
plt.gca().invert_yaxis()
plt.show()

# --- 4. Budget Distribution ---
budgets = df['Budget (in Million USD)'].dropna().sort_values().reset_index(drop=True)
plt.figure(figsize=(10, 5))
plt.plot(budgets, color='purple', linewidth=2)  # Line plot
plt.xlabel('Budget (in Million USD)')
plt.ylabel('Count')
plt.title('Distribution of Anime Budgets')
plt.show()

# --- 5. Number of Anime Released Per Year ---
anime_per_year = df['Release Year'].value_counts().sort_index()
plt.figure(figsize=(12, 5))
plt.plot(anime_per_year.index, anime_per_year.values, marker='o', color='blue', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Number of Anime')
plt.title('Anime Releases Per Year')
plt.show()

# --- 6. Popular Animation Studios ---
top_studios = df['Animation Studio Name'].value_counts().head(10)
plt.figure(figsize=(10, 5))
plt.barh(top_studios.index, top_studios.values, color='orange')
plt.xlabel('Number of Anime')
plt.ylabel('Animation Studio')
plt.title('Top 10 Animation Studios')
plt.gca().invert_yaxis()
plt.show()

