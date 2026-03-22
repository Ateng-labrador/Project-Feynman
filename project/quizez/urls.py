from django.urls import path

from .views import(
    QuizListView,
    quiz_view,
    quiz_data_view,
    categoryPost
)

# tambahkan index baru

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<int:pk>/', quiz_view, name='quiz-view'),
    path('<int:pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('category/<slug:categoryInput>/', categoryPost)
]

