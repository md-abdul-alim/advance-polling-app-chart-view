from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Question, Choice
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.http.response import JsonResponse

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html',context)

def detail(request,id):
    try:
        question = Question.objects.get(pk=id)
        context = {
            'question':question
        }
    except  Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html', context)

def results(request,id):
    question = get_object_or_404(Question, pk=id)
    context = {
        'question':question
    }
    return render(request,'polls/results.html',context)

def vote(request,id):
    question = get_object_or_404(Question,pk=id)

    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except  (KeyError, Choice.DoesNotExist):
        context = {
            'question':question,
            'error_messages':"You didn't select a choice."
        }
        return render(request,'polls/detail.html', context)
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #Always return an HttpResponseredirect after successfully dealing with POST data. This prevents data form besing posted
        # twice if a user hits the back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

def resultsData(request, id):
    votedata = []

    question = Question.objects.get(id=id)
    votes= question.choice_set.all()

    for i in votes:
        votedata.append({i.choice_text:i.votes})

    #print(votedata)
    return JsonResponse(votedata, safe=False)