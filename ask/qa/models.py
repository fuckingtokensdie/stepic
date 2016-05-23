from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


#class QuestionManager(models.Manager):
#        def new():
#                pass
#        def popular():
#                pass

class Question(models.Model):
    # objects = QuestionManager()
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_likes', blank=True)

    def url(self):
        return reverse('qa:question', kwargs={'question_id': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
