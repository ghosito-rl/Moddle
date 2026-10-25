from estudiantes import estudiante

class App:
    def __init__(self):
        self.main()
    
       
    def borrarPantalla(self):
          print("\033c")
    
        
    def esperarTecla(self):
          input("... ¡Oprima cualquier tecla para continuar! ...")
          
    
    def terminar(self):
           input(".... :::: !GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! ::::.... ")
           
    
    def opcionInvalida(self):
           input("\n\t .... ¡Opcion invalidad oprima cualquier tecla para continuar !....")
    
    
    def menu_acciones(self,tipo):
             print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
             opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Regresar \n \t\tElige una Opcion: ").strip()
             return opcion
         
    
    def respuesta_sql(self,respuesta):
            if respuesta:
                input("\n\t...¡Accion Realizada con Exito!...")
            else:
                input("\n\t...¡Esta Accion no pudo realizarse en este momento!...")
       
    
    def datos_estudiante(self,tipo):
            self.borrarPantalla()
            print(f"\n\t ...Ingresar los datos del {tipo}")
            estudiantito={}
            estudiantito['nombre']=input("Nombre: ").upper().strip()
            estudiantito['nota']=input("Nota (Calificacion): ").strip()
            return estudiantito
        
    
    def menu_estudiantes(self):
            opc=True
            while opc:
             self.borrarPantalla()
             opc=self.menu_acciones("Estudiantes")
             match opc:
                case '1':
                  estudiantito=self.datos_estudiante("Estudiante")
                  estudiante1=estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])                   
                  respuesta=estudiante1.insertar()
                  self.respuesta_sql(respuesta)
                  del estudiante1
                  
                case '2':
                  self.borrarPantalla()
                  id=input("Ingrese el ID del estudiante a eliminar: ").strip()                 
                  respuesta=estudiante.Estudiantes.eliminar(id)
                  self.respuesta_sql(respuesta)
                case '3':
                 self.borrarPantalla()
                 id=input("Ingrese el ID del estudiante a actualizar: ").strip()
                 estudiantito=self.datos_estudiante("Estudiante")
                 estudiante1=estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])                   
                 respuesta=estudiante1.actualizar(id)
                 self.respuesta_sql(respuesta)
                 del estudiante1
                case '4':
                  self.borrarPantalla()
                  registros=estudiante.Estudiantes.consultar()
                  num_estudiante=1
                  if len(registros)>0:
                    for fila in registros:
                      print(f"\n\Estudiante #: {num_estudiante}\n\t\tID: {fila[0]}\n\t\tNombre: {fila[1]}\n\t\tNota (Calificacion): {fila[2]}")
                      num_estudiante+=1
                      self.esperarTecla()
                  else:
                      print("...¡No se encontro informacion en la BD!...") 
                      self.esperarTecla()   
                case '5':
                 pass
                case _:
                 self.opcionInvalida()
               
    
    def main(self):
            opcion=True
            while opcion:
                self.borrarPantalla()
                opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1.- Estudiantes\n\t2.- Salir\n\tElige una opcion: ").lower().strip()
                match opcion:
                    case '1':
                        self.borrarPantalla()
                        self.menu_estudiantes()
                        self.esperarTecla()
                    case '2':
                        self.borrarPantalla()  
                        self.terminar() 
                        opcion=False 
                    case _:
                        self.opcionInvalida()
    
if __name__=="__main__":
    app=App()