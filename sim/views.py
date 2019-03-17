# -*- coding: utf-8 -*-


import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from sim.models import Question, Answer, Result, Param, Option


def base(request):
    if not request.session.session_key:
        request.session.save()
    for param in Param.objects.all():
        result, created = Result.objects.get_or_create(session_key=request.session.session_key, param=param)
        result.value = param.default_value
        result.save()
    return HttpResponseRedirect(
        reverse('sim:question', args=(Question.objects.get(type='начало').id,)))


def question(request, q_id):
    question = Question.objects.get(id=q_id)
    question_answers = question.question_answers.all()
    results = Result.objects.filter(
        session_key=request.session.session_key)
    response = render(request, 'sim/question.html',
                      {'answers': question_answers, 'results': results, 'end': question.type == 'конец'})
    # if request.method == 'POST':
    #     answer = Answer.objects.get(question=question, text=request.POST['choice'])
    #     random_value = random.random()
    #     print(random_value)
    #     print(answer.answer_options.all())
    #     option = answer.answer_options.get(bottom_line__lte=random_value, upper_line__gt=random_value)
    #     params = option.option_params.all()
    #     for param in params:
    #         result = Result.objects.get(session_key=request.session.session_key, param=param.param)
    #         result.value += param.value_to_add
    #         print(param.value_to_add)
    #         result.save()
    #
    #     response = HttpResponseRedirect('%s?opt=%s' % (reverse('sim:question', args=(option.question_to.id,)),
    #                                                    str(option.id))) if question.type != 'конец' else render(request,
    #                                                                                                             'sim/results.html',
    #                                                                                                             {
    #                                                                                                                 'results': Result.objects.filter(
    #                                                                                                                     session_key=request.session.session_key),
    #                                                                                                                 'option': option})
    return response


def ajax_save(request):
    question = Question.objects.get(name=request.GET['question'])
    answer = Answer.objects.get(question=question, text=request.GET['choice'])
    random_value = random.random()
    print(random_value)
    print(answer.answer_options.all())
    option = answer.answer_options.get(bottom_line__lte=random_value, upper_line__gt=random_value)
    params = option.option_params.all()
    params_result = {}
    for param in params:
        result = Result.objects.get(session_key=request.session.session_key, param=param.param)
        result.value += param.value_to_add
        print(param.value_to_add)
        result.save()
        value_to_add = '+%s' % (int(param.value_to_add)) if param.value_to_add >= 0 else int(param.value_to_add)
        params_result[param.param.name] = (int(result.value), value_to_add)
    print(params_result)

    next = reverse('sim:question', args=(option.question_to_id,)) if option.question_to_id else reverse(
        'sim:results')
    data = {'points': render_to_string('sim/points.html', {'option': option, 'results': params_result}),
            'jump': next}
    return JsonResponse(data)


def results(request):
    return render(request,
                  'sim/results.html',
                  {
                      'results': Result.objects.filter(
                          session_key=request.session.session_key),
                  })
