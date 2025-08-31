import pandas as pd
df = pd.read_csv('bestsellers.csv')

# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

#The first thing we can do is check for and remove any duplicate rows in the dataset using the drop_duplicates() function
df.drop_duplicates(inplace=True)

# It's good practice to rename columns first for consistency before manipulating them.
# Here we rename several columns, including 'Price' to 'price'.
df.rename(columns={
    "Name": "Title",
    "Year": "Publication Year",
    "User Rating": "Rating",
    "Price": "price"
}, inplace=True)

#we can convert the "Price" column to a float data type to make it easier to work with. We can use the astype() function to do this.
# Now we can safely use the new lowercase 'price' column name.
df['Price'] = df['price'].astype('float')

author_counts = df['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
