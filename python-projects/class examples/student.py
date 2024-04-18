class student:

    def __init__(self, lname, fname, id, energy_level):
        self.lname = lname
        self.fname = fname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return f"{self.lname}  :  {self.id}"
    
    