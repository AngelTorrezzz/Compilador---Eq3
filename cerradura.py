
    # Ejemplo de entrada: ['I1', [ ["E'", ['E', '•', '$'] ], ["E", ['E', '•', '+', 'T'] ] ] ]
    #
    #           conjuntoI[0]: "I1" -- Número del conjunto I
    #           conjuntoI[1]: [ ["E'", ['E', '•', '$'] ], ["E", ['E', '•', '+', 'T'] ] ] -- Conjunto de reglas de producción de I
    #               conjunto[1][0]: ["E'", ['E', '•', '$'] ] -- Regla de producción en posición 0
    #                   conjunto[1][0][0]: "E'" -- Base de la regla 0
    #                   conjunto[1][0][1]: ['E', '•', '$'] -- Producciones de la regla 0
    #                       conjunto[1][0][1][0]: 'E'   }
    #                       ...                         } -- Producción 0, ..., 2 de la regla 0
    #                       conjunto[1][0][1][2]: '$'   }
    #               conjunto[1][1]: ["E", ['E', '•', '+', 'T'] ] -- Regla de producción en posición 1
    #                   conjunto[1][1][0]: "E" -- Base de la regla 1
    #                   conjunto[1][1][1]: ['E', '•', '+', 'T'] -- Producciones de la regla 1
    #                       conjunto[1][1][1][0]: 'E'   }
    #                       ...                         } -- Producción 0, ..., 3 de la regla 1
    #                       conjunto[1][1][1][3]: 'T'   }

# Recibe la tupla del conjunto I y la tupla de reglas usadas en todo el programa. Devuelve una lista únicamente con las reglas de producción resultantes
def cerradura(conjuntoI, reglas):
    lista_I = list(conjuntoI)
    lista_r = list(reglas)
    nueva_I = lista_I[1]    # Se crea la nueva lista I solo con las reglas de producción
    for elemento in nueva_I:        # Se recorren las reglas de la lista nueva

        j = 0
        for i in range(0, len(elemento[1])):    # Se recorre la lista de producciones de cada regla
            if elemento[1][i] == '•':           # Si una producción es el símbolo •
                j = i                           # devuelve la posición siguiente a tal símbolo
                break

        simbNT = ''                                 # Por defecto se asume un símbolo vacío
        if j < len(elemento[1])-1:                  # Si aún se puede aumentar el índice obtenido
            simbNT = elemento[1][j+1]               # Se saca el primer símbolo tras el •
        
        for regla in lista_r:              # Para cada regla en la lista
            if regla[0] == simbNT:                  # Se comparan el símbolo tras el • y la base de la regla, y si son iguales...
                nv_regla = ["", []]
                nv_regla[0] = regla[0]
                for simbolo in regla[1]:
                    nv_regla[1].append(simbolo)
                # Se crea una nueva regla tomando como base la regla ya existente
                nv_regla[1].insert(0, '•')             # Se inserta el símbolo • al inicio de las producciones
                if not(nv_regla in nueva_I):
                    nueva_I.append(nv_regla)            # Y se agrega a la nueva lista de reglas

    return nueva_I


'''

#_____________________________________________________
#   Ejecución del código
#   Comentar cuando se implemente
#_____________________________________________________

#   Uso el ejemplo de las diapositivas 32 y 33 para probar, supongo que las de la 34 funcionan también
reglas_prod = [('E', ['E', '+', 'T']), ('E', ['T']), ('T', ['T', '*', 'F']), ('T', ['F']), ('F', ['(', 'E', ')']), ('F', ['id'])]   # Reglas de producción
conjuntoParaI0 = ['I0', [ ["E'", ['•', 'E', '$'] ] ] ]                                                                              # [E'->• E $]
conjuntoParaI1 = ['I0', [ ["E'", ['E', '•', '$'] ], ["E", ['E', '•', '+', 'T'] ] ] ]                                                # [E'->• E $], [E->E • + T]
conjuntoParaI2 = ['I0', [ ["E", ['T', '•'] ], ["T", ['T', '•', '*', 'F'] ] ] ]                                                      # [E->T •], [T->T • * F]
conjuntoParaI3 = ['I0', [ ["T", ['F', '•'] ] ] ]                                                                                    # [T->F •]
conjuntoParaI4 = ['I0', [ ["F", ['(', '•', 'E', ')'] ] ] ]                                                                          # [F->( • E )]
conjuntoParaI5 = ['I0', [ ["F", ['id', '•'] ] ] ]                                                                                   # [F->id •]

result = cerradura(conjuntoParaI0, reglas_prod)
print ("\ncerradura(I0):", result)
print ("cerradura(I1):", cerradura(conjuntoParaI1, reglas_prod))
print ("cerradura(I2):", cerradura(conjuntoParaI2, reglas_prod))
print ("cerradura(I3):", cerradura(conjuntoParaI3, reglas_prod))
print ("cerradura(I4):", cerradura(conjuntoParaI4, reglas_prod))
print ("cerradura(I5):", cerradura(conjuntoParaI5, reglas_prod))


'''