from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = 'my_portfolio'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_projects/', views.add_projects, name='add_projects'),
    path('projects/', views.projects, name='projects'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    