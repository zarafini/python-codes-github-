class Dogs:
    def __init__(self, breed, color):
        self.breed= breed
        self.color= color

ob1= Dogs("golden retriever", "golden")
ob2= Dogs("Dalmatian", "black and white")

print("Olie is a", ob1.breed)
print("Olie's color is", ob1.color)
print("Gaby is a", ob2.breed)
print("Gaby's color is", ob2.color)