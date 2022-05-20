from django.shortcuts import redirect, render
from .forms import PageForm
from .models import Page

# Create your views here.

def page_list(request):
    object_list = Page.objects.all()
    return render(request, 'blog/page_list.html', {'object_list': object_list})

def page_detail(request, page_id):
    object_detail = Page.objects.get(id=page_id)
    return render(request, 'blog/page_detail.html', {'object_detail': object_detail})

def page_create(request):
    if request.method == 'POST': 
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-list')
    else:
        form = PageForm()
    return render(request, 'blog/page_create.html', {'form':form})

def page_update(request, page_id):
    update = Page.objects.get(id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=update.id)
    else:
        form = PageForm(instance= update)
    return render(request, 'blog/page_create.html', {'form':form})

def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'blog/page_confirm.html', {'object' : object})
