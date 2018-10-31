from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Job, Skill


@receiver(pre_save, sender=Job)
def set_title_id(sender, instance=None, created=False, **kwargs):
    if created:
        find_job = instance.find_match_closest_job()
        instance.title_id = find_job['uuid']


@receiver(post_save, sender=Job)
def get_skill(sender, instance=None, created=False, **kwargs):
    if created:
        skills = instance.find_related_skills()
        for skill in skills:
            name = skill['skill_name']
            description = skill['description']
            importance = skill['importance']
            level = skill['level']
            new_skill = Skill.objects.create(name=name,
                                             description=description,
                                             importance=importance,
                                             level=level)
            new_skill.save()
            instance.skills = new_skill
            instance.save()


