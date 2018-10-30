import requests
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Job, Skill


@receiver(pre_save, sender=Job)
def set_title_id(sender, instance=None, created=False, **kwargs):
    if created:
        url = 'http://api.dataatwork.org/v1/jobs/autocomplete'
        params = {'begins_with': instance.title}
        response = requests.get(url, params=params)
        job_api = response.json()[0]
        instance.title_id = job_api['uuid']


@receiver(post_save, sender=Job)
def get_skill(sender, instance=None, created=False, **kwargs):
    if created:
        url='http://api.dataatwork.org/v1/jobs/{}/related_skills'.\
            format(instance.title_id)
        response = requests.get(url)
        skills = response.json()
