from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm
from .models import Project


# Create your views here.

def index(request):
    now = timezone.now()

    return render(request, 'my_portfolio/index.html', {'now':now})

@login_required
def add_projects(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_portfolio:projects')
        
    else:
        form = PortfolioForm()

    context = {
        'form':form,
    }
    return render(request, 'my_portfolio/add_projects.html', context)

def projects(request):
    projects = Project.objects.order_by('-date_added')
    context ={
        'projects':projects
    }
    return render(request, 'my_portfolio/projects.html', context)

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('my_portfolio:projects')
    context = {
        'project':project
    }
    return render(request, 'my_portfolio/delete_project.html', context)

@login_required
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=project )
        if form.is_valid():
            form.save()
            return redirect('my_portfolio:projects')
        
    else:
        form = PortfolioForm(instance=project)

    context = {
        'form':form,
        'project':project
    }
    return render(request, 'my_portfolio/update_project.html', context)






