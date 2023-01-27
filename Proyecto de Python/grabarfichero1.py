fichero = open("fichero_para_grabar.txt","wt")

texto_del_fichero ="Hola, esta es la linea que vamos a grabar en el fichero de texto"

fichero.write(texto_del_fichero)

fichero.close()