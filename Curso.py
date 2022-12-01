#cursos:id,nombre, creditos, añosdeestudio
#Necesitamos.
#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro

class Curso:
    def __init__(self,id,nombre,creditos,años_de_estudio):
        self.id=id
        self.nombre=nombre
        self.credits=creditos
        self.años_est=años_de_estudio
    def fichaCurso(self):
        print('--------------------------------------------------------------------------')
        print(f'ID curso: {self.id}\nNombre del curso: {self.nombre}\nTotal de créditos: {self.credits} créditos\nAños de duración: {self.años_est} años')
        print('--------------------------------------------------------------------------')

curso1=Curso(1,'DAM',120,2)
curso2=Curso(2,'DAW',120,2)
curso3=Curso(3,'DAM & DAW',250,3)
cursos=[curso1,curso2,curso3]
for c in cursos:
    c.fichaCurso()