from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('project/<int:id>', project, name='project'),
    path('uidesign/<int:id>', uidesign, name='uidesign'),
    
]

    