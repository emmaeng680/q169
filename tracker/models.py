from django.db import models
from django.contrib.auth.models import User

class QuestionCollection(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    collection = models.ForeignKey(QuestionCollection, on_delete=models.CASCADE, related_name='topics')
    
    class Meta:
        unique_together = ('name', 'collection')
        
    def __str__(self):
        return f"{self.name} ({self.collection.name})"

class Question(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    collections = models.ManyToManyField(QuestionCollection, related_name='questions')  # This is the new field
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions', null=True)
    
    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)
    review_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('user', 'question')