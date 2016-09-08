import media
import fresh_tomatoes

#create several instance of the movie object
me_before_you=media.Movie("Me before you","A girl with a disabled guy",
                          "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                          "https://www.youtube.com/watch?v=Eh993__rOxA")

sausage_party=media.Movie("Sausage Party", "An adult level cartoon.",
                          "https://upload.wikimedia.org/wikipedia/en/e/e4/Sausage_Party.png",
                          "https://www.youtube.com/watch?v=9VoNgLnjzVg")

our_times=media.Movie("Our Times","A story of first love.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f3/Our_Times%2C_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=0HGiG9z2m74")

the_shawshank_redemption=media.Movie("The Shawshank Redemption","A story about hope.",
                                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                     "https://www.youtube.com/watch?v=6hB3S9bIaco")
the_martian=media.Movie("The Martian","A story about how a person survive alone at Mars",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                        "https://www.youtube.com/watch?v=ej3ioOneTy8")

#use the open_movie_page() function in fresh_tomates.py to create our movie website

movies=[me_before_you,sausage_party,our_times,the_shawshank_redemption,the_martian]

fresh_tomatoes.open_movies_page(movies)
