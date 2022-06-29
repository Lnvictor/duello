from django.db import models

from duello.custom_auth.models import Users


class Cage(models.Model):
    creator = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=500, null=True)
    participants = models.ManyToManyField(Users, related_name='participants')

    def __repr__(self):
        return f"{self.creator}_{self.title}"

    def __str__(self):
        return f"{self.creator}_{self.title}"


class Question(models.Model):
    creator = models.ForeignKey(Users, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=30, null=False, blank=False, default="Unamed")
    description = models.CharField(max_length=500, null=False, blank=False, default="")
    cages = models.ManyToManyField(Cage)

    def __repr__(self):
        return f"{self.creator}_{self.title}"

    def __str__(self):
        return f"{self.creator}_{self.title}"


class Answer(models.Model):
    content = models.CharField(max_length=500, null=False, blank=False, default="")
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
