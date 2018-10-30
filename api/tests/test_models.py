from django.test import TestCase

from api.models import Skill, Job


class SkillModelTest(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(name='Time Management',
                                           description="managing one's own time"
                                                       "and the time of others",
                                           importance=3.5,
                                           level=6)

        self.skill2 = Skill.objects.create(name='  ActivE    LearninG ',
                                           description="tests skill",
                                           importance=6.5,
                                           level=1)

    def test_name_max_length(self):
        max_length = self.skill1._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_normalized_name(self):
        skill1 = Skill.objects.get(id=1)
        skill2 = Skill.objects.get(id=2)
        self.assertEquals("time management", skill1.normalized_name)
        self.assertEquals("active learning", skill2.normalized_name)


class JobModelTest(TestCase):
    def setUp(self):
        self.job1 = Job.objects.create(title='Software Engineer',
                                       location='New York')
        self.job2 = Job.objects.create(title=' SoftWare   ARCHITECT  ',
                                       location='Los Angles')

    def test_title_max_length(self):
        max_length = self.job1._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_location_max_length(self):
        max_length = self.job1._meta.get_field('location').max_length
        self.assertEquals(max_length, 100)

    def test_normalized_title(self):
        job1 = Job.objects.get(id=1)
        job2 = Job.objects.get(id=2)
        self.assertEquals("software engineer", job1.normalized_title)
        self.assertEquals("software architect", job2.normalized_title)
