class   Facotory:
    def __intt__(self , material , zips ,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

        def show (self):
            print("Material:", self.material)
            print("zips" ,self.zips)
            print("pockets" , self.pockets)
            
    obj = Facotory("Leather" , 2 ,4 )
    obj.show()
