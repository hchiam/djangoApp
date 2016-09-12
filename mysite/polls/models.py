from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


# Create your models here.


@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    # fields (i.e. database column names):
    question_text = models.CharField(max_length=200) # question (character field), with required argument max_length
    pub_date = models.DateTimeField('date published') # publication date (date time field), renamed as 'date published' using the optional first-positional argument for Field
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    # fields (i.e. database column names):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # each choice is associated with a question
    # (ForeignKey is for defining a database relationship)
    choice_text = models.CharField(max_length=200) # text of the choice (character field)
    votes = models.IntegerField(default=0) # vote tally (integer field)
    def __str__(self):
        return self.choice_text

