from django.shortcuts import get_object_or_404, redirect, render
from .forms import DiscForm
from .models import Disc

def home(request):
    discs = Disc.objects.all()
    context = {'discs': discs}
    return render(request, 'discography/home.html', context)

def show_disc(request, id):
    disc = get_object_or_404(Disc, pk=id)
    context = {'disc': disc}
    return render(request, 'discography/disc.html', context)

def create_disc(request):
    if request.method == 'GET':
        context = {'form': DiscForm()}
        return render(request, 'discography/disc_form.html', context)
    elif request.method == 'POST':
        form = DiscForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discography')
        else:
            return render(request, 'discography/disc_form.html', {'form': form})

def edit_disc(request, id):
    disc = get_object_or_404(Disc, pk=id)

    if request.method == 'GET':
        context = {'form': DiscForm(instance=disc), 'id': id}
        return render(request,'discography/disc_form.html',context)
    
    elif request.method == 'POST':
        form = DiscForm(request.POST, instance=disc)
        if form.is_valid():
            form.save()
            return redirect(f'/disc/show/{id}')
        else:
            return render(request,'discography/disc_form.html',{'form':form})
        
def delete_disc(request, id):
    disc = get_object_or_404(Disc, pk=id)
    context = {'disc': disc}    
    
    if request.method == 'GET':
        return render(request, 'discography/disc_confirm_delete.html',context)
    elif request.method == 'POST':
        disc.delete()
        return redirect('discography')