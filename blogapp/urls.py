
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from blogapp import views
urlpatterns = [
    path('', views.index,name='index'),
    #re_path('detail/(?P<post_id>[0-9]+)/', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)