from django.db import models
from enum import Enum

class VoteValue(Enum):
    PRO="PRO"
    CON="CON"

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def possible_votes(self):
        return [VoteValue.PRO, VoteValue.CON]

    def result(self):
        result_map = {}
        for tag in VoteValue:
            result_map[tag] = 0
            for vote in self.vote_set.all:
                if tag == vote.tag:
                    result_map[tag] = result_map[tag] + 1
        return result_map

    def count(self):
        sum = 0

        for vote in self.vote_set.all():
            print ('fachri:' + str(type(vote.value)))
            print ('fachri:' + str(vote.value))
            if vote.value == VoteValue.PRO.name:
                sum = sum + 1

            if vote.value == VoteValue.CON.name:
                sum = sum - 1

        return sum



class Vote(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    value       = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in VoteValue])

    def __str(self):
        return self.value


