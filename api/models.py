import difflib
import uuid

import requests
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
        return round(0.4*(self.importance*2) + 0.6 * self.level, 2)


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

    def find_job(self):
        url = 'http://api.dataatwork.org/v1/jobs/autocomplete'
        params = {'begins_with': self.title}
        response = requests.get(url, params=params)
        return response.json()

    def find_match_closest_job(self):
        job_list = self.find_job()
        list_for_matches = []
        for job in job_list:
            list_for_matches.append(job['normalized_job_title'])
        match_job = difflib.get_close_matches(self.normalized_title,
                                              list_for_matches)[0]
        matches_job = next(job for job in job_list if
                           job['normalized_job_title'] == match_job)
        return matches_job
