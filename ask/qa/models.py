from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField(default="")
    added_at = models.DateField(default=timezone.now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author", on_delete=models.SET_DEFAULT, default="", null=True)
    likes = models.ManyToManyField(User, related_name="question_like_user")
    
    def __str__(self):
        return self.title
    
    def get_url(self):
        return "/question/{}/".format(self.pk) 

    #class Meta:
    #    db_table = 'Questions'
    #    ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField(default=timezone.now())
    question = models.ForeignKey(Question, default="", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="", null=True)

    def __str__(self):
        return self.text

    def get_url(self):
        return "/question/{}/#answer_{}".format(self.question, self.id)
