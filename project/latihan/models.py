from django.db import models
from django.utils.text import slugify
import random

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=255)
    body  = models.TextField()
    category = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)

class Quiz(models.Model):
    text = models.TextField(blank=True)
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


