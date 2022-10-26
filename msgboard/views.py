from django.shortcuts import render
from .models import Message
#from .forms import MessageForm

# Create your views here.
"""if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = MessageForm() = > 'form': form,"""

def board(request):

    messages = Message.objects.order_by('-date')
    return render(request, 'msgboard/board.html', {'messages': messages, })
