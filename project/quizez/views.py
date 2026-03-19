from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse


# Create your views here.
class QuizListView(ListView):
    model = Quiz
    template_name = 'quizez/index.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizez/single-post.html', {'obj' : quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    question = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        question.append({str(q): answers})
    return JsonResponse({
        'data': question,
        # 'time': quiz.time,
    })
