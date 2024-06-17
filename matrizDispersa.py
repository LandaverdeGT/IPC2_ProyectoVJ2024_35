import os
from listaCabecera import ListaCabecera
from nodoCabecera import NodoCabecera
from nodoCelda import NodoCelda

data = ''
class MatrizDispersa():
    def __init__(self):
        self.filas = ListaCabecera("fila")
        self.columnas = ListaCabecera("columna")

    def insertar(self, x, y, dato):
        # Se crea el nodo de la celda a agregar
        nuevo = NodoCelda(x, y, dato)
        # 1. Se busca si ya existe la cabecera de la s filas o columnas de la matriz
        celda_x = self.filas.obtenerCabecera(x)
        celda_y = self.columnas.obtenerCabecera(y)

        #2. Comprobamos si la cabecera de la fila X existe
        if celda_x == None:
            #Si no existe entonces se crea una nueva cabecera fila en la posicion X
            celda_x = NodoCabecera(x)
            self.filas.insertarNodoCabecera(celda_x)

        #2. Comprobamos si la cabecera de la columna Y existe
        if celda_y == None:
            #Si no existe entonces se crea una nueva cabecera columna en la posicion Y
            celda_y = NodoCabecera(y)
            self.columnas.insertarNodoCabecera(celda_y)

        #3. Procedemos a insertar una nueva celda a la matriz
        #3.1 INSERTAR UNA NUEVA CELDA EN LA FILA
        #3.1.1. Comprobamos que la celda X no este apuntando hacia ningun nodo interno (acceso)
        if celda_x.acceso == None:
            celda_x.acceso = nuevo
        #3.1.2. Si ya existe un nodo interno en la fila, entonces se procede a insertar la celda en la fila
        else:
            #3.1.2.1 Si la columa del nuevo nodo es menor a la columna del primer nodo interno
            if nuevo.y < celda_x.acceso.y:
                #NUEVO -> ACCESO
                nuevo.derecha = celda_x.acceso
                #NUEVO <- ACCESO
                celda_x.acceso.izquierda = nuevo
                #FILAX -> NUEVO
                celda_x.acceso = nuevo
            #3.1.2.2 Si la columna del nuevo nodo es mayor a la columna del ultimo nodo interno
            else:
                #VAMOS A RECORRER DE IZQUIERDA A DERECHA LA FILA
                actual = celda_x.acceso
                while actual != None:
                    #Si la columna del nuevo nodo es menor a la columna del nodo actual
                    if nuevo.y < actual.y:
                        #NUEVO -> ACTUAL
                        nuevo.derecha = actual
                        #NUEVO <- ACTUAL
                        nuevo.izquierda = actual.izquierda
                        #ACTUAL <- NUEVO
                        actual.izquierda.derecha = nuevo
                        #ACTUAL -> NUEVO
                        actual.izquierda = nuevo
                        break
                    #SI LA POSICION EN X y Y DEL NUEVO NODO ES IGUAL A LA POSICION EN X y Y DEL NODO ACTUAL
                    elif nuevo.x == actual.x and nuevo.y == actual.y:
                        #SI QUEREMOS SOBREESCRIBIR EL DATO
                        #actual.dato = dato
                        #SI NO QUEREMOS SOBREESCRIBIR EL DATO ENTONCES NO SE HACE NADA
                        break
                    #SI LA POSICION EN Y DEL NUEVO NODO ES MAYOT A LA POSICION EN Y DEL ULTIMO NODO
                    else:
                        #SI EL NODO ACTUAL SU .DERECHA ES NULL ENTONCES SE INSERTA EL NUEVO NODO AL FINAL DE LA FILA
                        if actual.derecha == None:
                            #ACTUAL -> NUEVO
                            actual.derecha = nuevo
                            #NUEVO <- ACTUAL
                            nuevo.izquierda = actual
                            break
                        #SI EL NODO ACTUAL TIENE UN NODO DERECHA (OSEA NO ES EL ULTIMO NODO DE LA FILA)
                        else:
                            #AVANZAMOS AL SIGUIENTE NODO
                            actual = actual.derecha

        #3.2 INSERTAR UNA NUEVA CELDA EN LA COLUMNA
        #3.2.1. Comprobamos que la celda Y no este apuntando hacia ningun nodo interno (acceso)
        if celda_y.acceso == None:
            celda_y.acceso = nuevo
        #3.2.2. Si ya existe un nodo interno en la columna, entonces se procede a insertar la celda en la columna
        else:
            #SI LA FILA DEL NUEVO NODO ES MENOR A LA FILA DEL NODO ACCESO
            if nuevo.x < celda_y.acceso.x:
                #NUEVO -> ACCESO
                nuevo.abajo = celda_y.acceso
                #NUEVO <- ACCESO
                celda_y.acceso.arriba = nuevo
                #FILAY -> NUEVO
                celda_y.acceso = nuevo
            #INSERTAMOS EL NUEVO NODO EN LA COLUMNA (MOVIMIENTO DE ARRIBA HACIA ABAJO)
            else:
                actual2 = celda_y.acceso
                while actual2 != None:
                    #SI LA POSICION EN X DEL NUEVO NODO ES MENOR A LA POSICION EN X DEL NODO ACTUAL
                    if nuevo.x < actual2.x:
                        #NUEVO -> ACTUAL2
                        nuevo.abajo = actual2
                        #ACTUAL2.ARRIBA <- NUEVO
                        nuevo.arriba = actual2.arriba
                        #ACTUAL2.ARRIBA -> NUEVO
                        actual2.arriba.abajo = nuevo
                        #NUEVO <- ACTUAL2
                        actual2.arriba = nuevo
                        break
                    #SI LA POSICION EN X y Y DEL NUEVO NODO ES IGUAL A LA POSICION EN X y Y DEL NODO ACTUAL
                    elif nuevo.x == actual2.x and nuevo.y == actual2.y:
                        #SI QUEREMOS SOBREESCRIBIR EL DATO
                        #actual2.dato = dato
                        #SI NO QUEREMOS SOBREESCRIBIR EL DATO ENTONCES NO SE HACE NADA
                        break
                    #SI LA POSICION EN X DEL NUEVO NODO ES MAYOR A LA POSICION EN X DEL ULTIMO NODO
                    else:
                        #SI EL NODO ACTUAL2 SU .ABAJO ES NULL ENTONCES SE INSERTA EL NUEVO NODO AL FINAL DE LA COLUMNA
                        if actual2.abajo == None:
                            #ACTUAL2 -> NUEVO
                            actual2.abajo = nuevo
                            #NUEVO <- ACTUAL2
                            nuevo.arriba = actual2
                            break
                        #SI EL NODO ACTUAL2 TIENE UN NODO ABAJO (OSEA NO ES EL ULTIMO NODO DE LA COLUMNA)
                        else:
                            #AVANZAMOS AL SIGUIENTE NODO
                            actual2 = actual2.abajo

    def recorridoFilas(self, fila):
        print('--------------Recorrido por fila------------------')
        inicio = self.filas.obtenerCabecera(fila)
        if inicio == None:
            print('La fila no existe')
            return 
        
        actual = inicio.acceso
        while actual != None:
            print(f'{str(actual.x)}, {str(actual.y)} = {str(actual.dato)}')
            actual = actual.derecha

    # -- RECORRIDO POR COLUMNAS
    def recorridoColumnas(self, columna):
        global data
        print('--------------Recorrido por columna------------------')
        inicio = self.columnas.obtenerCabecera(columna)
        if inicio == None:
            print('La columna no existe')
            return None
        
        actual = inicio.acceso
        while actual != None:
            print(f'{str(actual.x)}, {str(actual.y)} = {str(actual.dato)}')
            data = str(actual.dato)
            actual = actual.abajo 
        return data

    # -- BUSCAR UN NODO ESPECIFICO DE LA MATRIZ
    def buscar(self, x, y):
        actual = self.filas.obtenerCabecera(x).acceso
        while actual != None:
            if actual.y == y:
                return actual.dato
            actual = actual.derecha
        return None

    def graphics(self):
        archivo = open('reportedot/matrizDispersa.dot', 'w')
        codigodot = '''digraph G {
graph [pad=\"0.5\", nodesep=\"1\", ranksep=\"1\"];
label=\"Matriz Dispersa\"
node [shape=box, height=0.8];\n'''
        
        filaActual = self.filas.primero
        idFila = ''
        conexionesFilas = ''
        nodosInteriores = ''
        direccionInteriores = ''
        while(filaActual != None):
            primero = True
            actual = filaActual.acceso
            idFila += '\tFila'+str(actual.x)+'[style=\"filled\" label = \"'+str(filaActual.id)+'\" fillcolor="white" group = 0];\n'
            if filaActual.siguiente != None:
                conexionesFilas += '\tFila'+str(actual.x)+' -> Fila'+str(filaActual.siguiente.acceso.x)+';\n'
            direccionInteriores += '\t{ rank = same; Fila'+str(actual.x)+'; '
            while actual != None:
                nodosInteriores += '\tNodoF'+str(actual.x)+"_C"+str(actual.y)+'[style=\"filled\" label = \"'+str(actual.dato)+'\" group = '+str(actual.y)+'];\n'
                direccionInteriores += 'NodoF'+str(actual.x)+"_C"+str(actual.y)+'; '
                if primero == True:
                    nodosInteriores += '\tFila'+str(actual.x)+' -> NodoF'+str(actual.x)+"_C"+str(actual.y)+'[dir=""];\n'
                    if actual.derecha != None:
                        nodosInteriores += '\tNodoF'+str(actual.x)+"_C"+str(actual.y)+' -> NodoF'+str(actual.derecha.x)+"_C"+str(actual.derecha.y)+';\n'
                    primero = False
                else:
                    if actual.derecha != None:
                        nodosInteriores += '\tNodoF'+str(actual.x)+"_C"+str(actual.y)+' -> NodoF'+str(actual.derecha.x)+"_C"+str(actual.derecha.y)+';\n'
                actual = actual.derecha
            filaActual = filaActual.siguiente
            direccionInteriores += '}\n'

        codigodot += idFila + '''
edge[dir="both"];
'''+conexionesFilas+'''
edge[dir="both"]
'''
        columnaActual = self.columnas.primero
        idColumna = ''
        conexionesColumnas = ''
        direccionInteriores2 = '\t{rank = same; '
        while columnaActual != None:
            primero = True
            actual = columnaActual.acceso
            idColumna += '\tColumna'+str(actual.y)+'[style=\"filled\" label = \"'+str(actual.y)+'\" fillcolor="white" group = '+str(actual.y)+'];\n'
            direccionInteriores2 += 'Columna'+str(actual.y)+'; '
            if(columnaActual.siguiente != None):
                conexionesColumnas += 'Columna'+str(actual.y)+' -> Columna'+str(columnaActual.siguiente.acceso.y)+';\n'
            while actual != None:
                if primero == True:
                    codigodot += 'Columna'+str(actual.y)+' -> NodoF'+str(actual.x)+"_C"+str(actual.y)+'[dir=""];\n'
                    if actual.abajo != None:
                        codigodot += 'NodoF'+str(actual.x)+"_C"+str(actual.y)+' -> NodoF'+str(actual.abajo.x)+"_C"+str(actual.abajo.y)+';\n'
                    primero = False
                else:
                    if actual.abajo != None:
                        codigodot += 'NodoF'+str(actual.x)+"_C"+str(actual.y)+' -> NodoF'+str(actual.abajo.x)+"_C"+str(actual.abajo.y)+';\n'
                actual = actual.abajo
            columnaActual = columnaActual.siguiente
        codigodot += idColumna 
        codigodot += conexionesColumnas + '\n'
        codigodot += direccionInteriores2 + '}\n'
        codigodot += nodosInteriores
        codigodot += direccionInteriores
        codigodot += '\n}'

        archivo.write(codigodot)
        archivo.close()

        ruta_dot = 'reportedot/matrizDispersa.dot'
        ruta_svg = 'reportes/matrizDispersa.svg'

        comando = 'dot -Tsvg '+ruta_dot+' -o '+ruta_svg
        os.system(comando)

        ruta = os.path.abspath(ruta_svg)
        os.startfile(ruta)