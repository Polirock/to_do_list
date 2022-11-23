from django.forms import ModelForm

from to_do_list.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['task', 'units']