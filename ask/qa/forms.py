from django import forms
from django.forms import ModelForm

from .models import Question, Answer, User


class AskForm(ModelForm):
    #author = forms.CharField(disabled=True)

    class Meta:
        model = Question
        fields = ('title', 'text', 'author')
        # Метод save уже определен и сохраняет модель Meta.model
'''


class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок вопроса', max_length=250)
    text = forms.CharField(label='Вопрос', widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError(
                u'Title is empty', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(
                u'Text is empty', code='validation_error')
        return text

    def save(self):
        if self._user.is_anonymous:
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question
'''

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question', 'author')



class SignupForm(ModelForm):
    username = forms.CharField(max_length=180)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

