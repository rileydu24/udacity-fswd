import media as me
import fresh_tomatoes as ft


prison_break = me.TVShow(
    "Prison Break",
    "Brothers breaking out of prison",
    "https://goo.gl/ND6CmD",
    "https://www.youtube.com/watch?v=x9T-9fZn_oA",
    "Paul Scheuring", 80)

toy_story = me.Media(
    "Toy story",
    "Stories with toys",
    "https://goo.gl/c4EaUH",
    "https://www.youtube.com/watch?v=ZZv1vki4ou4",
    "John Lasseter")

avatar = me.Media(
    "Avatar",
    "A marine on an alien planet",
    "https://goo.gl/3g480a",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "James Cameron")

school_of_rock = me.Media(
    "School of Rock",
    "Rock band at school",
    "https://goo.gl/5lUJn8",
    "https://www.youtube.com/watch?v=oP7kExN8LFA",
    "Richard Linklater")

the_wind_rises = me.ForeignMovies(
    "The Wine Rises",
    "A look at the life of Jiro Horikoshi",
    "https://goo.gl/CSb8pO",
    "https://www.youtube.com/watch?v=imtdgdGOB6Q",
    "Hayao Miyazaki",
    "Japan")

princess_mononoke = me.ForeignMovies(
    "Princess Mononoke",
    "A tale of pricess Mononoke",
    "https://goo.gl/ReMyvw",
    "https://www.youtube.com/watch?v=4OiMOHRDs14",
    "Hayao Miyazaki",
    "Japan")

arriety = me.ForeignMovies(
    "The Secret World of Arriety",
    "A little human beings",
    "https://goo.gl/iO17L5",
    "https://www.youtube.com/watch?v=VlMe7PavaRQ",
    "Hayao Miyazaki",
    "Japan")

listOfMovies = [
    prison_break, toy_story, avatar, school_of_rock,
    the_wind_rises, arriety]

ft.open_movies_page(listOfMovies)
