from django.shortcuts import render
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(self, question_id):
    res = "You're looking at the results of question %s"
    return HttpResponse(res % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")


def index(request):
    return HttpResponse("h4lo world~~~")
