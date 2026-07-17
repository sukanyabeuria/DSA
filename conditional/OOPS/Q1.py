class   Facotory:
    def _intt_(self , material , zips ,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

        def show (self):
            print("Material:", self.material)
            print("zips" ,self.zips)
            print("pockets" , self.pockets)
            