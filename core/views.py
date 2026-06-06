from django.shortcuts import render, get_object_or_404
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


def project(request, id):
    project=get_object_or_404(Projects,id=id)
    
    context={
        'project': project
    }
    return render(request, 'core/project.html', context)

def uidesign(request, id):
    ui=get_object_or_404(UiDesign,id=id)
    
    context={
        'ui': ui
    }
    return render(request, 'core/ui_designe.html', context)