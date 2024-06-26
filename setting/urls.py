from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from client.views import ClientDetailView,ClientCreateView,ClientListView
from boos.views import AdminCreateView, AdminDetailView,AdminListView
from books.views import BooksCreateView, BooksDetailView,BookListView
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/',admin.site.urls),
   path('client/', ClientCreateView.as_view(), name='client-create'),
   path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
   path('boss/', AdminCreateView.as_view(), name='Boss'),
   path('boos/<int:pk>/', AdminDetailView.as_view(), name='Boss'),
   path('books/',BooksCreateView.as_view(), name='Books'),
   path('books/<int:pk>/', BooksDetailView.as_view(), name='Books'),
   path('books/all/', BookListView.as_view(), name="Books"),
   path('boos/all/', AdminListView.as_view(), name="Boss"),
   path('client/all/',ClientListView.as_view(), name="client-get"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)