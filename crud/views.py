from django.shortcuts import render, redirect
from .forms import Insertagenda
from .models import agenda



# Create your views here.

#Create
def create(request):
    form = Insertagenda(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read')
    
    return render(request,'cadastro.html',{'form': form})

#Read
def read(request):
    contact = agenda.objects.all().order_by('-nome')
    return render(request,'listar.html', {'contact': contact})


# Delete
def delete(request, id):
    contact = agenda.objects.get(id=id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('read')
    
    return render(request, 'confirm.html', {'contact': contact})


#Update
def update(request, id):
    atual = agenda.objects.get(id=id)
    form = Insertagenda(request.POST or None, instance=atual)
    
    if form.is_valid():
        form.save()
        return redirect('read')
    
    return render(request, 'cadastro.html', {'form': form, 'atual': atual})