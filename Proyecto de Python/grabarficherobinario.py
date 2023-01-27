import pickle

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
frutas.values()

fichero = open("fichero.pckl", "wb")
pickle.dump(frutas, fichero)
fichero.close

fichero2 = open("fichero.pckl", "rb")
dato = pickle.load(fichero2)
print(dato)
dato.values()

