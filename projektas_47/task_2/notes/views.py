from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# Užrašų sąrašas
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})

# Užrašo kūrimas
def notes_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create.html', {'form': form})

# Užrašo redagavimas
def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit.html', {'form': form, 'note': note})

# Užrašo ištrynimas
def notes_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes/delete.html', {'note': note})