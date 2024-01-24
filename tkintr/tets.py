import pickle

print("The data that were stored in file are: ")

fileobject =open("mybinary.dat", "r+")

objectvar= pickle.load (fileobject)

fileobject.close ()

print(objectvar)