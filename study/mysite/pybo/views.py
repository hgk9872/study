from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    question_list = Question.objects.order_by('-create_date')
    page = request.GET.get('page', '1') # 페이지
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 할당
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question} # key, value
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) # 임시저장
            answer.create_date = timezone.now()
            answer.question = question # 
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장하여 question 객체 리턴
            question.create_date = timezone.now() # 'subject', 'content'는 form에서 등록 (Meta를 통해)
            question.save() # 실제로 저장 (객체 생성)
            return redirect('pybo:index') # 데이터(질문 객체) 저장 후, 홈으로 돌아가기
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)