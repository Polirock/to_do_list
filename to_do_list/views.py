from django.shortcuts import render, redirect

from to_do_list.forms import ToDoForm
from to_do_list.models import ToDo




def main(request):
    form = ToDoForm()
    to_dos = ToDo.objects.all()
    return render(request, 'main.html', {'form': form, 'to_dos': to_dos})



def create_to_do(request):
    form = ToDoForm(request.POST)
    if form.is_valid():
        to_do = ToDo(task = form.cleaned_data['task'], units = form.cleaned_data['units'])
        to_do.save()
    return redirect('/')