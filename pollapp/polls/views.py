# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")


def detail(request, question_id):
    return HttpResponse("You looking at question %s." % question_id)


def results(request, question_id):
    response = "You looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You voting on question %s." % question_id)
