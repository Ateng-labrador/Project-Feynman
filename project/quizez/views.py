from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse


# Create your views here.
class QuizListView(ListView):
    model = Quiz
    template_name = 'quizez/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Quiz.objects.values_list('topic', flat=True).distinct()
        return context


def categoryPost(request, categoryInput):
    posts = Quiz.objects.filter(topic=categoryInput)
    categories = Quiz.objects.values_list('topic', flat=True).distinct()
    context = {
        'categories' : categories,
        'posts' : posts
    }
    return render(request, 'quizez/category.html', context)

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizez/single-post.html', {'obj' : quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    question = []
    for q in quiz.get_questions():
        answers = []
        solution = []
        for a in q.get_answers():
            answers.append(a.text)
        for s in q.solution_set.all():
            solution.append(s.text)
        question.append({str(q): answers,
                         "solution" : solution})
    return JsonResponse({
        'data': question,
        # 'time': quiz.time,
    })
