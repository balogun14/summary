from django.shortcuts import render, redirect
from .models import SummaryNotes
from .forms import NoteForm
# Create your views here.

def index(request):
    notes = SummaryNotes.objects.order_by('-date_added')
    context = {'notes': notes}
    return render(request, 'summarynotes/index.html', context)


def vrform(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        
        if form.is_valid():
            new_req = SummaryNotes(title=request.POST['title'], comment=request.POST['comment'], author=request.POST['author'])
            new_req.save()
            return redirect('index')
    else:
        form = NoteForm()
    context = {'form': form}
    return render(request, 'summarynotes/vrform.html', context)