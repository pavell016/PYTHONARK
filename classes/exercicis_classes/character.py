class character:
    edited = None
    name  = None
    created  = None
    gender  = None
    skin_color  = None
    hair_color  = None
    height  = None
    eye_color  = None
    mass  = None
    homeworld  = None
    birth_year  = None

    #constructor
    def __init__(self,edited,name,created,gender,skin_color,hair_color,height,eye_color,mass,homeworld,birthyear):
        self.edited = edited
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birthyear
    @property
    def getcharacterInfo(self):
        return ("nom:"+self.name+" gender:"+self.gender+" homeworld: "+self.homeworld+" birth_year:"+self.birth_year)
        
        