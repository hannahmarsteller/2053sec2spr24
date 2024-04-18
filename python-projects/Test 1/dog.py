class Dog:

    def __init__(self, name, trick, breed, hungry):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = hungry

    def __str__(self):
        return self.name + ' : ' + self.breed
    
    def speak(self):
        return "Woof"

    def feed(self):
        if self.hungry == "True":
            self.hungry == "False"
        elif self.hungry == "False":
            self.hungry == "False"

            
        def get_name(self):
            return self.name
    
    def get_breed(self):
        return self.breed
    
    def get_trick(self):
        return self.trick
    
    def isHungry(self):
        return self.hungry
    
    def change_trick(self):
        if self.trick == "high-five":
            self.trick == "fetch"
        