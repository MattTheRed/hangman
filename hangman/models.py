from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class GameUser(User):
    class Meta:
        proxy = True

    @property
    def wins(self):
        return Game.objects.filter(user=self, outcome="WIN").count()

    @property
    def losses(self):
        return Game.objects.filter(user=self, outcome="LOSS").count()


class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word

class Game(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    guess_count = models.PositiveSmallIntegerField(default=0)
    OUTCOME_CHOICES = (
        ('WIN', 'Win'),
        ('LOSS', 'Loss')
    )
    outcome = models.CharField(max_length=4, choices=OUTCOME_CHOICES)

    def save(self, *args, **kwargs):
        self.word = Word.objects.all().order_by("?")[0]
        super(Game, self).save(*args, **kwargs)
