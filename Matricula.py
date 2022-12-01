#matricula:idmatricula, fechamatricula, idalumno, idcurso
#Necesitamos.
#mostrar la ficha del curso
#mostrar la ficha de alumno
#alumno1 se matricula en un curso
#alumno2 se matricula en dos cursos
#mostrar los datos de matrículo
#reto*:método que muestra las mátriculas realizadas en mi centro
from Actividad27.Alumno import Alumno
from Actividad27.Curso import Curso


class Matricula:
    def __init__(self,id_matricula,id_curso,id_alumno,precio_matricula):
        self.id_matricula=id_matricula
        self.id_curso=id_curso
        self.id_alumno=id_alumno
        self.precio_matricula=precio_matricula
    def infoMatricula(self):
        print(f'Alumno: {self.id_alumno}\nCurso: {self.id_curso}\nPrecio total matrícula {self.precio_matricula}€')

#crear un pedido

cursillo1=Curso(1,'DAM',120,2)
cursillo2=Curso(2,'DAW',120,2)
cursillo3=Curso(3,'DAM & DAW',250,3)
alumnillo1=Alumno('A1','Martina','martinarockera@gmail.com')
alumnillo2=Alumno('A2','Carlos Manuel','eltrolldelgaming@gmail.com')
alumnillo3=Alumno('A3','Miguel','miguelperezsanchez@hotmail.com')

matricula1=Matricula(1,cursillo1,alumnillo1,2500)
matricula2=Matricula(2,cursillo2,alumnillo2,2500)
matricula3=Matricula(3,cursillo3,alumnillo3,3500)

matriculas=[matricula1,matricula2,matricula3]
for m in matriculas:
    m.infoMatricula()