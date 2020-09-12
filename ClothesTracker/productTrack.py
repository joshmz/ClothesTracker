#COMMENTED OUT PYTHON MATH OPERATIONS TO USE SQL GENERATED COLUMNS INSTEAD

#INITIALISE TABLES
import sqlite3
connection = sqlite3.connect('Clothes_Tracker.db')
cursor = connection.cursor()

#APPAREL TABLE
cursor.execute("""CREATE TABLE IF NOT EXISTS Apparel(
                Name text,
                Retail integer,
                Resale integer,
                Profit integer AS (Resale-Retail)
                )""");

#SNEAKER TABLE
cursor.execute("""CREATE TABLE IF NOT EXISTS Shoes(
                Name text,
                Retail integer,
                Resale integer,
                Profit integer AS (Resale-Retail),
                Size integer,
                USSize real AS (Size - 0.5)
                )""");
                #US Size = UK Size - 0.5

# Parent Class
class Apparel():

    #Class attributes
    numberOfClothes = 0
    clothes = []

    def __init__(self, name, retail, resale): #dunder instantiation
        self.name = name
        self.retail = retail
        self.resale = resale
        # self.profit = (self.resale - self.retail)

        Apparel.numberOfClothes += 1
        Apparel.clothes.append(self.name)

    # def getProfit(self):
    #     return self.profit

    @classmethod #Decorator
    def howMany(cls): #Reference the class
        return (f"There are {cls.numberOfClothes} clothes in your list: {cls.clothes}")

    def addApparel(self):
        cursor.execute("INSERT INTO Apparel VALUES (?, ?, ?)", (self.name,self.retail,self.resale))
        connection.commit()
        connection.close()


class Sneakers(Apparel): #Child class of Apparel
    def __init__(self,name,retail,resale,size):
        super().__init__(name,retail,resale) #reference super class
        self.size = size #UK

    def addSneaker(self):
        cursor.execute("INSERT INTO Shoes VALUES (?, ?, ?, ?)", (self.name,self.retail,self.resale,self.size))
        connection.commit()
        connection.close()


    # def convertUS(self):
    #     usSize = self.size - 0.5
    #     return usSize
