from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()
    
    # for board in boards:
    #     boards_names.append(board.name)更新前的试图
    
    # response_html = '<br>'.join(boards_names)
    
    return render(request,'home.html',{'boards':boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})