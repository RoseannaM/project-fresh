"""This is where the video objects are created"""
import urllib
import json
import fresh_tomatoes
import media


#movie data is created via an api call. The api provides the poster
#title infomation and the plot. The youtube link needs to be provided
#individually hence the list of tuples.
MOVIE_DATA = [("tt0470752", "https://www.youtube.com/watch?v=XYGzRB4Pnq8"),
              ("tt0137523", "https://www.youtube.com/watch?v=SUXWAEX2jlg"),
              ("tt0246578", "https://www.youtube.com/watch?v=fA3DZa6bifE"),
              ("tt0096283", "https://www.youtube.com/watch?v=92a7Hj0ijLs"),
              ("tt0180093", "https://www.youtube.com/watch?v=0nU7dC9bIDg"),
              ("tt0409459", "https://www.youtube.com/watch?v=PVjA0y78_EQ")]

MOVIES = []
#Iterate through the list of tuples and create the movies

for i in MOVIE_DATA:
    url = "http://www.omdbapi.com/?i="+i[0]
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    movie = media.Movie(data['Title'],
                        data['Plot'],
                        data['Poster'],
                        i[1])
    #created movies are pushed onto the above movie list.
    MOVIES.append(movie)

fresh_tomatoes.open_movies_page(MOVIES)
