from rest_framework import viewsets
from .models import *
from .serializers import *

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class PersonaFisicaViewSet(viewsets.ModelViewSet):
    queryset = PersonaFisica.objects.all()
    serializer_class = PersonaFisicaSerializer

class PersonaMoralViewSet(viewsets.ModelViewSet):
    queryset = PersonaMoral.objects.all()
    serializer_class = PersonaMoralSerializer

class PersonaFisicaDireccionViewSet(viewsets.ModelViewSet):
    queryset = PersonaFisicaDireccion.objects.all()
    serializer_class = PersonaFisicaDireccionSerializer

class PersonaMoralDireccionViewSet(viewsets.ModelViewSet):
    queryset = PersonaMoralDireccion.objects.all()
    serializer_class = PersonaMoralDireccionSerializer

class BenefactorViewSet(viewsets.ModelViewSet):
    queryset = Benefactor.objects.all()
    serializer_class = BenefactorSerializer

class BenefactorPersonaFisicaViewSet(viewsets.ModelViewSet):
    queryset = BenefactorPersonaFisica.objects.all()
    serializer_class = BenefactorPersonaFisicaSerializer

class BenefactorPersonaMoralViewSet(viewsets.ModelViewSet):
    queryset = BenefactorPersonaMoral.objects.all()
    serializer_class = BenefactorPersonaMoralSerializer

class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

class MCOViewSet(viewsets.ModelViewSet):
    queryset = MCO.objects.all()
    serializer_class = MCOSerializer

class PersonaFisicaMCOViewSet(viewsets.ModelViewSet):
    queryset = PersonaFisicaMCO.objects.all()
    serializer_class = PersonaFisicaMCOSerializer

class PersonaMoralMCOViewSet(viewsets.ModelViewSet):
    queryset = PersonaMoralMCO.objects.all()
    serializer_class = PersonaMoralMCOSerializer

class DonativoViewSet(viewsets.ModelViewSet):
    queryset = Donativo.objects.all()
    serializer_class = DonativoSerializer

class DonativoEntregadoViewSet(viewsets.ModelViewSet):
    queryset = DonativoEntregado.objects.all()
    serializer_class = DonativoEntregadoSerializer

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer

class BeneficiarioPersonaFisicaViewSet(viewsets.ModelViewSet):
    queryset = BeneficiarioPersonaFisica.objects.all()
    serializer_class = BeneficiarioPersonaFisicaSerializer

class BeneficiarioPersonaMoralViewSet(viewsets.ModelViewSet):
    queryset = BeneficiarioPersonaMoral.objects.all()
    serializer_class = BeneficiarioPersonaMoralSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubcategoriaViewSet(viewsets.ModelViewSet):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

class DatosBancariosViewSet(viewsets.ModelViewSet):
    queryset = DatosBancarios.objects.all()
    serializer_class = DatosBancariosSerializer

class GastosViewSet(viewsets.ModelViewSet):
    queryset = Gastos.objects.all()
    serializer_class = GastosSerializer
