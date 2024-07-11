
flag=True
listaProductos=[]
while flag:
    print("")
    with open('test.txt.txt', 'w', encoding='utf-8') as test:
        test.write("forting")


with open('Achivo_nuevo.txt','w', encoding='utf-8') as archivo:
        archivo.write("\tCódigo    |    nombre  |   cantidad    |   precio     \n")
        for producto in listaProductos:
            archivo.write(f"{producto}\n")
        print("Se creo correctamente")







