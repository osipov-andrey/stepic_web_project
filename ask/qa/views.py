from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from .models import Question
from django.core.paginator import Paginator, EmptyPage


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


def test(request, *args, **kwargs):
    return HttpResponse("OK")


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
    answer_list = q.answer_set.all().order_by('-added_at')
    context = {
        'question': q,
        'answers': answer_list,
    }
    return render(request, 'question.html', context)



