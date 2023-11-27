class Direccion:
  def _init_(self, calle_atributo, ciudad_atributo, codigo_postal_atributo, pais_atributo):
      self.calle = calle_atributo
      self.ciudad = ciudad_atributo
      self.codigo_postal = codigo_postal_atributo
      self.pais = pais_atributo

class Persona:
  def _init_(self, nombre_atributo, apellidos_atributo, cc_atributo):
      self.nombre = nombre_atributo
      self.apellidos = apellidos_atributo
      self.cc = cc_atributo
      self.direccion = Direccion()

class Estudiante(Persona):
  def _init_(self, nombre_atributo, apellidos_atributo, cc_atributo, id_estudiante_atributo):
      self.nombre = nombre_atributo
      self.apellidos = apellidos_atributo
      self.cc = cc_atributo
      self.id_estudiante = id_estudiante_atributo

class Profesor(Persona):
  def _init_(self, nombre_atributo, apellidos_atributo, cc_atributo, oficina_atributo):
      self.nombre = nombre_atributo
      self.apellidos = apellidos_atributo
      self.cc = cc_atributo
      self.oficina = oficina_atributo

personas = []

estudiante1 = Estudiante("Nicolas", "Giraldo", "123456789", "E001")
estudiante2 = Estudiante("Valentina", "Ospina", "987654321", "E002")

personas.append(estudiante1)
personas.append(estudiante2)

profesor1 = Profesor("Carlos", "Lopez", "111222333", "Oficina 101")
profesor2 = Profesor("Ana", "Martinez", "444555666", "Oficina 202")

personas.append(profesor1)
personas.append(profesor2)

for persona in personas:
    if type(persona) is Estudiante:
        print(f"Estudiante: {persona.nombre} {persona.apellidos}, ID: {persona.id_estudiante}")
    elif type(persona) is Profesor:
        print(f"Profesor: {persona.nombre} {persona.apellidos}, Oficina: {persona.oficina}")
    else:
        print(f"Persona: {persona.nombre} {persona.apellidos}")