from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  # Проверка пользователя
from django.views.generic.edit import CreateView

from datetime import datetime, timedelta

from .models import Question
from .forms import AskForm, AnswerForm, SignupForm


# Create your views here.


def paginate(request, lst):
    # get limit
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    # if limit is too high, normalize it
    if limit > 100:
        limit = 10

    paginator = Paginator(lst, limit)

    # get current page
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page, limit


@require_GET
def index(request, *args, **kwargs):
    question_list = Question.objects.new()
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'index.html', context)


def popular(request, *args, **kwargs):
    # list of questions in desc order by rating
    question_list = Question.objects.popular()
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'popular.html', context)


def question(request, pk):
    q = get_object_or_404(Question, id=pk)
    answer_list = q.answer_set.all().order_by('-id')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.author = request.user
        if form.is_valid():
            form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('')
    else:
        form = AnswerForm(initial={'question': q.id, 'author': request.user.id})
    context = {
        'question': q,
        'answers': answer_list,
        'form': form,
    }
    return render(request, 'question.html', context)


def AskAdd(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        # form.author = request.user
        if form.is_valid():
            ask = form.save()
            url = ask.get_url()
            return HttpResponseRedirect(url)
        else:
            return HttpResponse()
    else:
        form = AskForm(initial={'author': request.user.id})
    return render(request, 'ask.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

    form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form,
                                                        'user': request.user,
                                                        'session': request.session})


