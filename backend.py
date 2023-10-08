import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
file_path = r'/content/drive/MyDrive/movies.csv'
# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)
def recommend_movies(user_history, genre_preference, n_recommendations=5):
    # Filter movies not in the user's history
    user_movies = df[~df['title'].isin(user_history)]
    # Filter movies based on genre preference
    genre_filtered_movies = user_movies[user_movies['genres'].str.contains(genre_preference, case=False)]
    # Sort the remaining movies by rating in descending order
    recommended_movies = genre_filtered_movies.sort_values(by='vote_average', ascending=False)
    # Get the top N recommended movies
    top_recommendations = recommended_movies.head(n_recommendations)
    return top_recommendations
# Example usage
user_history = ['Movie A']  # User's watched movies
genre_preference = input("Enter the Genre:").capitalize()  # User's genre preference
recommendations = recommend_movies(user_history, genre_preference)
print("Recommended Movies:")
print(recommendations[['title', 'vote_average']])