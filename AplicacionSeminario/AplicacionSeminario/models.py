from django.db import models

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    no_ext = models.IntegerField()
    no_int = models.IntegerField()
    colonia = models.CharField(max_length=50)
    cp = models.IntegerField()
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class PersonaFisica(models.Model):
    id_persona_fisica = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)

class PersonaMoral(models.Model):
    id_persona_moral = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    representante = models.CharField(max_length=50)

class PersonaFisicaDireccion(models.Model):
    id_persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class PersonaMoralDireccion(models.Model):
    id_persona_moral = models.ForeignKey(PersonaMoral, on_delete=models.CASCADE)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Benefactor(models.Model):
    id_benefactor = models.AutoField(primary_key=True)
    registro = models.DateTimeField(auto_now_add=True)

class BenefactorPersonaFisica(models.Model):
    id_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    id_persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)

class BenefactorPersonaMoral(models.Model):
    id_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    id_persona_moral = models.ForeignKey(PersonaMoral, on_delete=models.CASCADE)

class Voluntario(models.Model):
    id_voluntario = models.AutoField(primary_key=True)
    id_persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)

class MCO(models.Model):
    id_mco = models.AutoField(primary_key=True)
    contacto = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    ppal = models.CharField(max_length=1)

class PersonaFisicaMCO(models.Model):
    id_persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)
    id_mco = models.ForeignKey(MCO, on_delete=models.CASCADE)

class PersonaMoralMCO(models.Model):
    id_persona_moral = models.ForeignKey(PersonaMoral, on_delete=models.CASCADE)
    id_mco = models.ForeignKey(MCO, on_delete=models.CASCADE)

class Donativo(models.Model):
    id_donativo = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    id_categoria = models.IntegerField()
    id_subcategoria = models.IntegerField()
    id_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add=True)

class DonativoEntregado(models.Model):
    id_donativo_entregado = models.AutoField(primary_key=True)
    id_donativo = models.ForeignKey(Donativo, on_delete=models.CASCADE)
    id_beneficiario = models.IntegerField()

class Beneficiario(models.Model):
    id_beneficiario = models.AutoField(primary_key=True)
    registro = models.DateTimeField(auto_now_add=True)

class BeneficiarioPersonaFisica(models.Model):
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    id_persona_fisica = models.ForeignKey(PersonaFisica, on_delete=models.CASCADE)

class BeneficiarioPersonaMoral(models.Model):
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    id_persona_moral = models.ForeignKey(PersonaMoral, on_delete=models.CASCADE)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Subcategoria(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)

class DatosBancarios(models.Model):
    id_datos_bancarios = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=50)
    nombre_dueno = models.CharField(max_length=50)
    
    banco = models.CharField(max_length=50)

class Gastos(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
