from django.contrib import admin

# Register your models here.

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'added_at', 'rating', 'author')
    list_display_links = ('title', 'text')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
