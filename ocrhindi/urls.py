from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home,output,gentemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('output/', output,name='output'),
    path('gentemplate/',gentemplate ,name='gentemplate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
