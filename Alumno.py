#alumno:id, nombre, email
#Necesitamos.
#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro

class Alumno:
    def __init__(self,id,nombre,email):
        self.id=id
        self.nombre=nombre
        self.email=email
    def fichaAlumno(self):
        print('--------------------------------------------------------------------------')
        print(f'ID Alumno: {self.id}\nNombre del alumno: {self.nombre}\nCorreo electónico del alumno: {self.email}')
        print('--------------------------------------------------------------------------')

alumno1=Alumno('A1','Martina','martinarockera@gmail.com')
alumno2=Alumno('A2','Carlos Manuel','eltrolldelgaming@gmail.com')
alumno3=Alumno('A3','Miguel','miguelperezsanchez@hotmail.com')
alumnoslist=[alumno1,alumno2,alumno3]
for al in alumnoslist:
    al.fichaAlumno()