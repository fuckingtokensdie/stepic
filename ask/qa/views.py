from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from models import Question, Answer


def main(request):
    all_questions = Question.object.order_by('-added_at')
    paginator = Paginator(all_questions, 10)
    page = request.GET.get('page', 1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'qa/main.html', {'questions': questions})


def popular(request):
    all_questions = Question.object.order_by('-rating')
    paginator = Paginator(all_questions, 10)
    page = request.GET.get('page', 1)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'qa/main.html', {'questions': questions})


def question(request, question_id):
    return HttpResponse('OK')

def test(request, *args, **kwargs):
    return HttpResponse('OK')
