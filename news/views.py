from django.shortcuts import render
from django.http import Http404
from .models import Question


# Create your views here.

def detail(request, question_id):
    
    try:
        question= Question.objects.get(pk= question_id)
        
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    
    return render(request, 'polls/details.html', {'question': question})

def index(request):
    
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    
    templates= loader.get_template('polls/index.html')
    context= {
        'latest_question_list': latest_question_list,
    }
    
    return HttpResponse(templates.render(context, request))


def results(request, question_id):
    response= 'You are looking at the results of question %s. '
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)
