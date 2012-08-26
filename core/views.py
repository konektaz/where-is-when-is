# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from forms import FeedbackForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def feedback(request):

    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()

        # TODO: Add message (django.contrib.messages)

        return redirect('/')

    return render(request, 'feedback.html', {'form': form})
