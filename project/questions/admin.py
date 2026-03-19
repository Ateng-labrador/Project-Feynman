from django.contrib import admin
from .models import Question, Answer, Solution

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer

class SolutionInline(admin.StackedInline):
    model = Solution
    max_num = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, SolutionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Solution)
