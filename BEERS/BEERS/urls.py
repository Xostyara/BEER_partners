# urls.py
from rest_framework.routers import DefaultRouter
from beer_menu.views import ContactsViewSet, TypeBeerViewSet, ProviderViewSet, ManufacturerViewSet, BeerViewSet
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions

router = DefaultRouter()

router.register('api/v1/contact', ContactsViewSet, basename='contact')
router.register('api/v1/type_beer', TypeBeerViewSet, basename='type_beer')
router.register('api/v1/provider', ProviderViewSet, basename='provider')
router.register('api/v1/manufacturer', ManufacturerViewSet,  basename='manufacturer')
router.register('api/v1/beer', BeerViewSet, basename='beer')

urlpatterns = [
    path('', include(router.urls)),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Cats API",
      default_version='v1',
      description="Документация для проекта BEERS",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="xostyara@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
] 