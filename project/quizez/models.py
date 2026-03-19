from django.db import models
import random
# page for make exam post

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    diffcluty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return self.question_set.all()[:self.number_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'
