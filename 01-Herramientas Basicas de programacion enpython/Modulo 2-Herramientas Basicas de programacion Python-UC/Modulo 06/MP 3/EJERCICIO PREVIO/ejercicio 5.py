dic_ingred = {
    'Tomate':            5,
    'Lechuga':           2,
    'Hamburguesa':      10,
    'Carne':             1,
    'Espárragos':        8,
    'Pan':              10,
    'Papa':              5,
    'Cebolla':          12
}

valores=(dic_ingred.values())
print(valores)



dic_recetas = {
    'HamburguesaCasera':    ['Hamburguesa', 'Tomate',       'Pan'     ],
    'PastelDeCarne':        ['Carne',       'Papa',         'Cebolla' ],
    'EnsaladaEspecial':     ['Lechuga',     'Espárragos',   'Tomate'  ]
}


solicitud=input("ingrese la receta para cocinar: ")

if solicitud in dic_recetas:

    print("si se encuentra la receta")
    #toma la receta, revisa los ingredientes y lo compara con los ingredientes si es que esta, si no esta no se puede preparar
    Ingredientes=dic_recetas[solicitud ]
    for recorreIng in Ingredientes:
        if recorreIng in dic_ingred:
            NExistencias=dic_ingred[recorreIng]
            if NExistencias > 0:
                print("si existen el ingredientes", recorreIng,"con ",NExistencias,"existencias, se descuenta 1")
                NExistenciasAct=NExistencias-1
                print("se actualiza el ingredientes", recorreIng, "con ", NExistenciasAct,"existencias")
            else:
                print("no hay stock para ",recorreIng)
        else:
            print("stop")
else:
    print("no se puede")


