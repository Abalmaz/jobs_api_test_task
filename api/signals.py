import requests
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Job, Skill


@receiver(pre_save, sender=Job)
def set_title_id(sender, instance=None, created=False, **kwargs):
    if created:
        find_job = instance.find_match_closest_job()
        instance.title_id = find_job['uuid']


# @receiver(post_save, sender=Job)
# def get_skill(sender, instance=None, created=False, **kwargs):
#     if created:
#         url = 'http://api.dataatwork.org/v1/jobs/{}/related_skills'.\
#               format(instance.title_id)
#         response = requests.get(url)
#         skills = response.json()
#         skill_list = skills['skills']
#         # Skill.objects.create(**skill_list)


