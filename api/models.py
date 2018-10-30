import uuid

from django.db import models


class Skill(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,
                            editable=False,
                            unique=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    importance = models.FloatField()
    level = models.FloatField()

    @property
    def normalized_name(self):
        return " ".join(self.name.lower().split())

    @property
    def scope(self):
        return


class Job(models.Model):
    title = models.CharField(unique=True, max_length=100)
    location = models.CharField(max_length=100)
    title_id = models.UUIDField(default=uuid.uuid4,
                                editable=False,
                                unique=True)
    skills = models.ManyToManyField(Skill)

    @property
    def normalized_title(self):
        return " ".join(self.title.lower().split())
