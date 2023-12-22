# WEB
from django.shortcuts import render, redirect

# LOCAL
from .models import Project
from .utils import text_to_html


def redirect_to_main(request):
    return redirect('/projects/')


def projects(request) -> render:
    context = {'publications': [], 'active': 'projects'}
    for project in Project.objects.all():
        context['publications'].append({'title': project.title,
                                        'description': project.description,
                                        'date': project.pubdate,
                                        'pic': project.pic})
    context['publications'] *= 3
    return render(request, 'homescreen/hp.html', context=context)


def info(request) -> render:
    with open('MyCV/apps/homescreen/aboutme.txt', 'r', encoding='utf-8') as text:
        text = text.read()
    text = [text_to_html(txt) for txt in text.split('\n\n')]
    context = {'aboutme': zip(text, [x for x in range(len(text))])}
    return render(request, f'homescreen/aboutme.html', context=context)


def render_cv(request) -> render:
    return render(request, 'homescreen/cv.html', context={})
