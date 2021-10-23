# #! /usr/bin/python3


#Guardamos en una variable la proxima id disponible
ultima_id = 0


#creamos una clase Nota, que represente una nota en el anotador. Debe tener Texto y etiquetas y se puede buscar por texto. 
class Nota:

#Crear el metodo iniciador. que inicie con la nota con un texto y opcionalmete, con etiquetas separadas por espacios. 
    def __init__(self, texto, etiquetas=''):
        self.texto = texto
        self.etiquetas = etiquetas
        self.fecha_creacion = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id

#Crear un metodo que determine si la nota coincide con el filtro de busqueda. Retorna True o False. 
    def coincide(self, filtro):
        if filtro in self.texto or filtro in self.etiquetas:
            return True
        else:
            return False




