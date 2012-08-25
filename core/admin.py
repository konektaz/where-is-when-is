# -*- coding: utf-8 -*-

from django.contrib import admin

from models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)
