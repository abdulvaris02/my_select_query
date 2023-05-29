
class MySelectQuery():
    def __init__(self, x):
        self.x = x
    
    def where(self, column_name, criteria):
        lst = [x for x in self.x.split("\n") if criteria in x.split(",")]
        return lst 
