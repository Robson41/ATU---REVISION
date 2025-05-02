'''Requirements:

Create a list of movies with their corresponding ratings (out of 10).
Allow the user to enter their favorite movie, and the program should ask for a rating (out of 10).
After the user provides their rating, the movie should be added to the list.
Sort the list by the ratings (from highest to lowest).
Display the movie list, showing the movie name and rating (in sorted order).
The user should be able to continue entering movies and ratings until they type "exit".
When they type "exit", the program should stop collecting input and display the final movie rankings.'''

movies = []

while len(movies) < 3:
#for movie in movies:
    movie = input('Please enter the name of your favourite movie: ')
    rating = int(input('Please enter your rating out of 10 for this movie: '))
    movies.append([movie, rating])


movies.sort(key=lambda movie: movie[1], reverse=True)

for movie in movies:
    print(f'The rating for {movie[0]} is {movie[1]}')








