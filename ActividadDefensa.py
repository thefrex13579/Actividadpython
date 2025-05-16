from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, nombre, autor, codigo):
        self.nombre = nombre
        self.autor = autor
        self.codigo = codigo

    @abstractmethod
    def mostrar_info(self):
        pass

    @abstractmethod
    def tiempo_prestamo(self):
        pass

    @abstractmethod
    def clasificar(self):
        pass

class Libro(MaterialBiblioteca):
    def __init__(self, nombre, autor, codigo, editorial, genero):
        super().__init__(nombre, autor, codigo)
        self.editorial = editorial
        self.genero = genero

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} creado por {self.autor}")

    def tiempo_prestamo(self):
        return 15

    def clasificar(self):
        print(f"El libro {self.nombre} pertenece al genero {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, nombre, autor, codigo, numero, empresa):
        super().__init__(nombre, autor, codigo)
        self.numero = numero
        self.empresa = empresa

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Numero: {self.numero} creado por la empresa {self.empresa}")

    def tiempo_prestamo(self):
        return 7

    def clasificar(self):
        print(f"Seccion de revistas - {self.nombre} N#{self.numero}")

class Tesis(MaterialBiblioteca):
    def __init__(self, nombre, autor, codigo, universidad, carrera):
        super().__init__(nombre, autor, codigo)
        self.universidad = universidad
        self.carrera = carrera

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} creado por {self.autor} de la universidad {self.universidad}")

    def tiempo_prestamo(self):
        return 4

    def clasificar(self):
        print(f"Seccion de tesis - {self.nombre} de la carrera {self.carrera}")

class BibliotecaDigital():
    def __init__(self):
        self.catalogo = {}

    def agregar_material(self, material: MaterialBiblioteca) -> None:
        self.catalogo[material.codigo] = material

    def mostrar_catalogo(self):
        for mat in self.catalogo.values():
            mat.mostrar_info()

    def prestar_material(self, codigo):
        if codigo not in self.catalogo:
            print("Material no encontrado en el catálogo.")
            return
        mat = self.catalogo[codigo]
        dias = mat.tiempo_prestamo()
        if dias > 0:
            print(f"Puede prestar '{mat.nombre}' por {dias} días.")
        else:
            print(f"'{mat.nombre}' sólo está disponible para consulta en sala.")

    def clasificar_material(self, codigo):
        if codigo not in self.catalogo:
            print("Material no encontrado.")
            return
        mat = self.catalogo[codigo]
        print(f"{mat.nombre} -> ", end="")
        mat.clasificar()

if __name__ == "__main__":
    biblioteca = BibliotecaDigital()

    # Crear instancias de cada tipo
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", "L001", "L001", "L001")
    revista = Revista("National Geographic", "Varios", "R001", "R001" , "R001")
    tesis = Tesis("Deep Learning Avanzado", "Ana Pérez", "T001", "Doctorado", "Doctorado")

    # Agregar al catálogo
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(tesis)

    # Mostrar catálogo e interactuar
    biblioteca.mostrar_catalogo()
    biblioteca.prestar_material("L001")
    biblioteca.prestar_material("T001")
    biblioteca.clasificar_material("R001")

