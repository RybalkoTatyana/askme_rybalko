from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.


def index(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "index.html", {'questions': content})


questions = [
    {
        "title": f"Title {i}",
        "text": f"this is text for {i}"
    } for i in range(100)
]

answers = [
    {
        "text": f"this is answer number {i}"
    } for i in range(10)
]


def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {'questions': content})


def tag(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "tag.html", {'questions': content})


def question(request):
    paginator = Paginator(answers, 4)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "question.html", {'answers': content})


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "signup.html", {})


def settings(request):
    return render(request, "settings.html", {})
