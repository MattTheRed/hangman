from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import string
import json

class GameUser(User):
    class Meta:
        proxy = True

    @property
    def wins(self):
        return Game.objects.filter(user=self, outcome="WIN").count()

    @property
    def losses(self):
        return Game.objects.filter(user=self, outcome="LOSS").count()

    def get_or_create_latest_game(self):
        try:
            return Game.objects.filter(user=self).order_by("-pk")[0]
        except:
            return Game.objects.create(user=self)

    @property
    def current_game(self):
        return self.get_or_create_latest_game()



class Word(models.Model):
    word = models.CharField(max_length=255)

    def __unicode__(self):
        return self.word

class Game(models.Model):
    user = models.ForeignKey(GameUser)
    word = models.ForeignKey(Word)
    OUTCOME_CHOICES = (
        ('WIN', 'Win'),
        ('LOSS', 'Loss')
    )
    outcome = models.CharField(max_length=4, choices=OUTCOME_CHOICES)

    alphabet = list(string.ascii_uppercase)

    @property
    def incorrect_guess_count(self):
        return Guess.objects.filter(game=self, is_correct=False).count()

    @property
    def remaining_letters(self):
        letter_list = []
        for letter in self.alphabet:
            if letter in self.guesses_list:
                letter_list.append({"letter": letter, "is_guessed": False})
            else:
                letter_list.append({"letter": letter, "is_guessed": True})
        return letter_list

    @property
    def display_word(self):
        letter_list = list(self.word.word.upper())
        guesses_list = self.guesses_list
        out_list = []
        for letter in letter_list:
            if letter in guesses_list:
                out_list.append(letter)
            else:
                out_list.append(" ")
        return out_list

    @property
    def is_winner(self):
        return " " not in self.display_word

    @property
    def json(self):
        data = {}
        data["score"] = {
            "wins": self.user.wins,
            "losses": self.user.losses,
        }
        data["current_game"] = {
            "incorrect_guess_count": self.incorrect_guess_count,
            "outcome": self.outcome,
            "remaining_letters": self.remaining_letters,
            "guesses": self.guesses_list,
            "display_word": self.word.word if self.outcome == "LOSS" else self.display_word,
        }

        return json.dumps(data)

    @property
    def guesses(self):
        return Guess.objects.filter(game=self)

    @property
    def guesses_list(self):
        return [guess.letter for guess in self.guesses]

    def make_guess(self, letter):
        letter = letter.upper()
        if Guess.objects.filter(game=self, letter=letter).count() < 1:
            if self.incorrect_guess_count < 10:
                is_correct = True if letter in self.word.word.upper() else False
                Guess.objects.create(game=self, letter=letter, is_correct=is_correct)
                if self.is_winner:
                    self.outcome = "WIN"
                    self.save()
                else:
                    if self.incorrect_guess_count == 10:
                        self.outcome = "LOSS"
                        self.save()
            else:
                self.outcome = "LOSS"
                self.save()

    def __unicode__(self):
        return self.word.word

    def save(self, *args, **kwargs):
        if not self.pk:
            self.word = Word.objects.all().order_by("?")[0]
        super(Game, self).save(*args, **kwargs)

class Guess(models.Model):
    game = models.ForeignKey(Game)
    is_correct = models.BooleanField(default=False)
    letter = models.CharField(max_length=1)
