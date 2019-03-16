# -*- coding: utf-8 -*-


from django.db import models


# Create your models here.

class Param(models.Model):
    name = models.CharField(unique=True, max_length=20)
    default_value = models.IntegerField(default=0)

    def __str__(self):
        return self.name


QUESTION_CHOICES = (
    ('начало', 'Начальный'),
    ('обычный', 'Обычный'),
    ('конец', 'Конечный')
)


class Question(models.Model):
    type = models.CharField(max_length=10, choices=QUESTION_CHOICES, default=QUESTION_CHOICES[1][0])
    name = models.TextField(unique=True)

    def __str__(self):
        return '%s - %s' % (self.type, self.name)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question_answers', null=False, blank=False,
                                 on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.question, self.text)

    class Meta:
        unique_together = (('question', 'text'),)


# частные случае опции - риск и успех из дока
class Option(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_options')
    name = models.CharField(max_length=100)
    bottom_line = models.FloatField()
    upper_line = models.FloatField()
    question_to = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = (('answer', 'name'), ('answer', 'bottom_line', 'upper_line'),)

    def __str__(self):
        return '%s - %s - [%s ; %s]' % (self.answer, self.name, str(self.bottom_line), str(self.upper_line))


class OptionParam(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='option_params')
    param = models.ForeignKey(Param, on_delete=models.CASCADE, related_name='param_options')
    value_to_add = models.FloatField()

    def __str__(self):
        return '%s - %s' % (self.option, self.param)

    class Meta:
        unique_together = (('option', 'param'),)


class Result(models.Model):
    session_key = models.TextField()
    param = models.ForeignKey(Param, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    class Meta:
        unique_together = (('session_key', 'param'),)
