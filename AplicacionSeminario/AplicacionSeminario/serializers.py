from rest_framework import serializers
from .models import *

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class PersonaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaFisica
        fields = '__all__'

class PersonaMoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMoral
        fields = '__all__'

class PersonaFisicaDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaFisicaDireccion
        fields = '__all__'

class PersonaMoralDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMoralDireccion
        fields = '__all__'

class BenefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefactor
        fields = '__all__'

class BenefactorPersonaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefactorPersonaFisica
        fields = '__all__'

class BenefactorPersonaMoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefactorPersonaMoral
        fields = '__all__'

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = '__all__'

class MCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCO
        fields = '__all__'

class PersonaFisicaMCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaFisicaMCO
        fields = '__all__'

class PersonaMoralMCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMoralMCO
        fields = '__all__'

class DonativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donativo
        fields = '__all__'

class DonativoEntregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonativoEntregado
        fields = '__all__'

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = '__all__'

class BeneficiarioPersonaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiarioPersonaFisica
        fields = '__all__'

class BeneficiarioPersonaMoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiarioPersonaMoral
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class DatosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosBancarios
        fields = '__all__'

class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = '__all__'
