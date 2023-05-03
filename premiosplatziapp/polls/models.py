from django.db import models

# Create your models here.


class Question(models.Model):
    # La creación de un id no es necesaria, porque se genera por default
    # Todo lo que termina en field es porque va a definir un atributo
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choices(models.Model):
    # En caso de eliminar la pregunta, también se eliminan sus respuestas en cascada
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
