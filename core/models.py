# -*- coding: utf-8 -*-

from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return "%s <%s>" % (self.name, self.email)
