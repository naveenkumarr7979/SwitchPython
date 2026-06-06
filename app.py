MENU_PROPMT="\nEnter 'a' to add a movie , 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit : "
movies=[]
#first program edited
def add_movie():
    title =input("Enter movie title: ")
    director = input("Enter director: ")
    year = input("Enter year: ")
    movies.append({"title":title,"director":director,"year":year})

def show_movies():
    for moive in movies:
        print(moive)

def find_movie():
    search_title=input("Enter movie title: ")
    for movie in movies:
        if movie['title'] == search_title:
            print(movie)
user_options={  #first class function impl
    "a":add_movie,
    "l":show_movies,
    "f":find_movie
}

def menu():
    selection=input(MENU_PROPMT)
    while selection !='q':
        if selection in user_options:
            selected_option=user_options[selection]
            selected_option()
        else:
            print('unknown command. please try again')

        selection = input(MENU_PROPMT)

menu()
