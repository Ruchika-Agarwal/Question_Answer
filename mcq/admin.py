from django.contrib import admin

from .models import Question_Set, Question, Options
# Register your models here.

admin.site.register(Question_Set)
admin.site.register(Question)
admin.site.register(Options)

'''
from django.contrib import admin

from .models import Question


class ChoiceInline(admin.StackedInline):
    model = Options
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'image']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


class QuestAdmin(admin.StackedInline):
    model = Question


class QuestionSetAdmin(admin.ModelAdmin):
    fields = ['section']
    inlines = [QuestAdmin]


admin.site.register(Question_Set, QuestionSetAdmin)
'''