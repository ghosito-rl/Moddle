from coches import cochesBD

class App():
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("... ! Oprima cualquier tecla para continuar ¡ ...")

    def terminarSistema(self):
        input("... ::: ! Gracias por usar nuestro sistema ¡ ::: ...")

    def opcionInvalida(self):
        input("... Opcion invalida oprima cualquier tecla para continuar...")

    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\n\t... ! Accion realizada con exito ¡ ...")
        else:
            input("\n\t... ! Esta accion no pudo realizarse ¡ ...")

    def menu_acciones(self,tipo):
        return input(f"\n\t\t ::: Menu de {tipo} ::: \n\t1.- Insertar\n\t2.- Eliminar\n\t3.- Actualizar\n\t4.- Consultar\n\t5.- Salir\n\tElige una opcion: ").strip()

    def datos_coche(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ... Ingresar los datos del {tipo}")
        cochesito={}
        cochesito['marca'] = input("Marca : ").upper().strip()
        cochesito['color'] = input("Color : ").upper().strip()
        cochesito['modelo'] = int(input("Modelo : "))
        cochesito['velocidad'] = int(input("Velocidad (km/h) : "))
        cochesito['potencia'] = int(input("Potencia (hp) : "))
        cochesito['asientos'] = int(input("# Asientos : "))
        return cochesito

    def menu_coches(self):
        opc=True

        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case '1':
                    cochesito=self.datos_coche("Coche")
                    coches1=cochesBD.CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta=coches1.insertar()
                    self.respuesta_sql(respuesta)
                    del coches1

                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a eliminar: ").strip()
                    respuesta=cochesBD.CochesBD.eliminar(id)
                    self.respuesta_sql(respuesta)

                case '3':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coche("Coche")
                    coches1=cochesBD.CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta=coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1

                case '4':
                    self.borrarPantalla()
                    registros=cochesBD.CochesBD.consultar()
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tCoche #: {num_coche}\n\t\tID: {fila[0]}\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]}\n\t\tVelocidad: {fila[4]}\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("... No se encontro informacion en la BD ...")
                        self.esperarTecla()

                case '5':
                    opc=False

                case _:
                    self.opcionInvalida()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu principal ::: \n\t1.- Coches\n\t2.- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminarSistema()
                    opcion=False
                case _:
                    self.opcionInvalida()


if __name__=="__main__":
    app=App()
