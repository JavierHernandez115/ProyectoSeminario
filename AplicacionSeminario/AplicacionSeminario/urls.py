"""
URL configuration for AplicacionSeminario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'direcciones', DireccionViewSet)
router.register(r'personas_fisicas', PersonaFisicaViewSet)
router.register(r'personas_morales', PersonaMoralViewSet)
router.register(r'personas_fisicas_direcciones', PersonaFisicaDireccionViewSet)
router.register(r'personas_morales_direcciones', PersonaMoralDireccionViewSet)
router.register(r'benefactores', BenefactorViewSet)
router.register(r'voluntarios', VoluntarioViewSet)
router.register(r'mcos', MCOViewSet)
router.register(r'personas_fisicas_mcos', PersonaFisicaMCOViewSet)
router.register(r'personas_morales_mcos', PersonaMoralMCOViewSet)
router.register(r'donativos', DonativoViewSet)
router.register(r'donativos_entregados', DonativoEntregadoViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)
router.register(r'beneficiarios_personas_fisicas', BeneficiarioPersonaFisicaViewSet)
router.register(r'beneficiarios_personas_morales', BeneficiarioPersonaMoralViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'subcategorias', SubcategoriaViewSet)
router.register(r'datos_bancarios', DatosBancariosViewSet)
router.register(r'gastos', GastosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
