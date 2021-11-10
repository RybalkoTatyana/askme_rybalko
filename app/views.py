from django.shortcuts import render
from app.models import Questions, Tags, Answers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


questions = Questions.objects.all()
tags = Tags.objects.all()
answers = Answers.objects.all()
num_questions = Questions.objects.all().count()

context = {
    'num_questions': num_questions,
    'questions': questions,
    'tags': tags,
    'answers': answers,
}

popular_members = [
    {'name': 'Queen Victoria'},
    {'name': 'Vladimir Putin'},
    {'name': 'Interesting Person'},
    {'name': 'Roose'},
    {'name': 'Dr.House'},
]

tags = [
    {'name': 'TechnoPark',
     'priority': 'high'},
    {'name': 'C++',
     'priority': 'medium'},
    {'name': 'Google',
     'priority': 'low'},
    {'name': 'BMSTU',
     'priority': 'high'},
    {'name': 'Home',
     'priority': 'medium'},
    {'name': 'Walk',
     'priority': 'low'},
    {'name': 'Dragon',
     'priority': 'very high'},
]


def paginate(objects_list, request, per_page=4):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return page_obj


def index(request):
    return render(request, 'index.html',
                  {'page': paginate(Questions.objects.all(), request),
                   'popular_members': popular_members,
                   'popular_tags': tags,
                   'context': context})


def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {'page': paginate(Questions.objects.all(), request),
                                        'popular_members': popular_members,
                                        'popular_tags': tags,
                                        'context': context})


def tag(request, tag_name):
    return render(request, "tag.html", {'page': paginate(Questions.objects.all(), request),
                                        'popular_members': popular_members,
                                        'popular_tags': tags,
                                        'tag_name': tag_name,
                                        'context': context})


def question(request, pk):
    return render(request, "question.html", {'page': paginate(Answers.objects.all(), request),
                                             'popular_members': popular_members,
                                             'popular_tags': tags,
                                             'context': context,
                                             'question': Questions.objects.get(id=pk)
                                             })


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "signup.html", {})


def settings(request):
    return render(request, "settings.html", {})
