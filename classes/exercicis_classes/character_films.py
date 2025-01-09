import character
class character_films(character):
    num_of_films = None
    first_film = None
    alive_at_the_end = None

    #constructor
    def __init__(self,edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birthyear,num_of_films,first_film,alive_at_end):
        super().__init__(edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birthyear)
        self.num_of_films = num_of_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_end

    @num_of_films.setter
    def  num_of_films(self, num):
        self.num_of_films = num   

    @first_film.setter
    def  first_film(self, first_film):
        self.first_film = first_film  
    @alive_at_the_end.setter
    def  alive_at_the_end(self, alive_at_the_end):
        self.alive_at_the_end = alive_at_the_end     