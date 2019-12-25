from django import forms
from django.forms import ModelForm

from .models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')

        # Метод save уже определен и сохраняет модель Meta.model


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question')


