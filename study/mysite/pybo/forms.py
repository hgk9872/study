from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question      # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content'] # field는 사용할 속성
        labels = {           # labels은 그 속성에 대한 라벨(제목)
            'content' : '답변내용',
        }