from django.shortcuts import render""", redirect"""
from .models import Message
from .forms import MessageForm

# Create your views here.


def board(request):
    messages = Message.objects.order_by('-date')
    """if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = MessageForm() = > 'form': form,""" 
    return render(request, 'msgboard/board.html', {'messages': messages, })
