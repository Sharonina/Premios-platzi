import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    # La creación de un id no es necesaria, porque se genera por default
    # Todo lo que termina en field es porque va a definir un atributo
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Ayuda a que nos de el texto de las preguntas y no un 'object'
    def __str__(self) -> str:
        return self.question_text

    # Método personalizado
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # En caso de eliminar la pregunta, también se eliminan sus respuestas en cascada
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
