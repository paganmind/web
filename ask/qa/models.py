from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class NewQuestionManager(models.Manager):
    def get_queryset(self):
        return super(NewQuestionManager, self).get_queryset().order_by('-addet_at')


class PopularQuestionManager(models.Manager):
    def get_queryset(self):
        return super(PopularQuestionManager, self).get_queryset().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    added_at = models.DateTimeField()
    rating = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, null=True, related_name='users_like')

    new = NewQuestionManager()
    popular = PopularQuestionManager()

    def __unicode__(self):
        return '(%s) %s' % (self.title, self.added_at)



class Answer(models.Model):
    text = models.TextField(null=False, blank=False)
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, null=False)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return '%s' % self.added_at
