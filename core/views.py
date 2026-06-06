from django.shortcuts import render
from .models import Projects,UiDesign,Logo, Poster

# Create your views here.
def index(request):
    
    project=Projects.objects.all()
    uidesign=UiDesign.objects.all()
    logo=Logo.objects.all()
    poster=Poster.objects.all()
    
    context={
        'project':project,
        'uidesign':uidesign,
        'logo':logo,
        'poster': poster,
    }
    return render(request, 'core/index.html',context)


def project(request):
    return render(request, 'core/project.html')

