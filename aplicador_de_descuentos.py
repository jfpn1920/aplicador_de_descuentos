import random
ids = []
nombres = []
descripciones = []
categorias = []
precios = []
descuentos = []
valores_descuento = []
precios_finales = []
estados = []
observaciones = []
#--------------------------------------------#
#--|menu_principal_aplicador_de_descuentos|--#
#--------------------------------------------#
while True:
    print("menu principal aplicador de descuentos")
    print("1) crear producto")
    print("2) editar producto")
    print("3) eliminar producto")
    print("4) buscar producto")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_producto|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_producto = 1
        else:
            id_producto = ids[-1] + 1
        nombre = input("nombre del producto: ")
        descripcion = input("descripción: ")
        categoria = input("categoría: ")
        precio = float(input("precio original: "))
        descuento = float(input("porcentaje de descuento: "))
        estado = input("estado (disponible o no disponible): ")
        observacion = input("observación: ")
        valor_descuento = precio * (descuento / 100)
        precio_final = precio - valor_descuento
        ids.append(id_producto)
        nombres.append(nombre)
        descripciones.append(descripcion)
        categorias.append(categoria)
        precios.append(precio)
        descuentos.append(descuento)
        valores_descuento.append(valor_descuento)
        precios_finales.append(precio_final)
        estados.append(estado)
        observaciones.append(observacion)
        print("producto registrado correctamente.")
        print("id:", id_producto)
        print("valor del descuento: $", format(valor_descuento, ".2f"))
        print("precio final: $", format(precio_final, ".2f"))
    #---------------------#
    #--|editar_producto|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("editar producto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${precios_finales[i]:.2f}")
            id_buscar = int(input("ingrese la id del producto: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | ${precios[posicion]:.2f}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                precios[posicion] = float(input("nuevo precio: "))
                descuentos[posicion] = float(input("nuevo descuento (%): "))
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                valores_descuento[posicion] = precios[posicion] * (descuentos[posicion] / 100)
                precios_finales[posicion] = precios[posicion] - valores_descuento[posicion]
                print("producto actualizado correctamente.")
                print("nuevo valor del descuento: $", format(valores_descuento[posicion], ".2f"))
                print("nuevo precio final: $", format(precios_finales[posicion], ".2f"))
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_producto|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("eliminar producto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${precios_finales[i]:.2f}")
            id_buscar = int(input("ingrese la id del producto: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del producto")
                print(f"{ids[posicion]} | {nombres[posicion]} | ${precios_finales[posicion]:.2f}")
                respuesta = input("¿desea eliminar este producto? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    categorias.pop(posicion)
                    precios.pop(posicion)
                    descuentos.pop(posicion)
                    valores_descuento.pop(posicion)
                    precios_finales.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("producto eliminado correctamente.")
                else:
                    print("el producto no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_producto|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            print("buscar producto")
            id_buscar = int(input("ingrese la id del producto: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("precio original: $", format(precios[posicion], ".2f"))
                print("descuento:", descuentos[posicion], "%")
                print("valor del descuento: $", format(valores_descuento[posicion], ".2f"))
                print("precio final: $", format(precios_finales[posicion], ".2f"))
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen productos registrados.")
        else:
            disponibles = 0
            no_disponibles = 0
            total_original = 0
            total_final = 0
            ahorro_total = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | ${precios[i]:.2f} | {descuentos[i]}% | ${precios_finales[i]:.2f}")
                total_original += precios[i]
                total_final += precios_finales[i]
                ahorro_total += valores_descuento[i]
                if estados[i].lower() == "disponible":
                    disponibles += 1
                else:
                    no_disponibles += 1
            print("estadísticas aplicador de descuentos")
            print("cantidad de productos:", len(ids))
            print("productos disponibles:", disponibles)
            print("productos no disponibles:", no_disponibles)
            print("valor total sin descuento: $", format(total_original, ".2f"))
            print("valor total con descuento: $", format(total_final, ".2f"))
            print("ahorro total generado: $", format(ahorro_total, ".2f"))
            posicion = random.randint(0, len(ids) - 1)
            print("producto seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("precio original: $", format(precios[posicion], ".2f"))
            print("descuento:", descuentos[posicion], "%")
            print("valor del descuento: $", format(valores_descuento[posicion], ".2f"))
            print("precio final: $", format(precios_finales[posicion], ".2f"))
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aplicador de descuentos.")
        break
    else:
        print("opción no válida.")