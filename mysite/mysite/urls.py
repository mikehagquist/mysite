from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('polls/', include('polls.urls')), #Comment due to weird free teir aws url
    path('stringsomedays/', include('stringsomedays.urls')),
    path('admin/', admin.site.urls),
    #path('', include('polls.urls')),
]