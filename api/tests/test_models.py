from django.test import TestCase

from api.models import Skill, Job


class SkillModelTest(TestCase):
    def setUp(self):
        self.skill1 = Skill.objects.create(name='Time Management',
                                           description="managing one's own time"
                                                       "and the time of others",
                                           importance=3.94,
                                           level=4.91)

        self.skill2 = Skill.objects.create(name='  ActivE    LearninG ',
                                           description="tests skill",
                                           importance=3.88,
                                           level=4)

    def test_name_max_length(self):
        max_length = self.skill1._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_normalized_name(self):
        skill1 = Skill.objects.get(id=1)
        skill2 = Skill.objects.get(id=2)
        self.assertEquals("time management", skill1.normalized_name)
        self.assertEquals("active learning", skill2.normalized_name)

    def test_scope_correct_value(self):
        skill1 = Skill.objects.get(id=1)
        skill2 = Skill.objects.get(id=2)
        self.assertEquals(6.1, skill1.scope)
        self.assertEquals(5.5, skill2.scope)


class JobModelTest(TestCase):
    def setUp(self):
        self.job1 = Job.objects.create(title='Software Engineer',
                                       location='New York',
                                       title_id=
                                       "6b0b1cc3de799472d984e6346b929e51")
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

    def test_find_job_is_correct(self):
        job = Job.objects.get(id=1)
        result = job.find_job()
        self.assertEquals(3, len(result))

    def test_find_match_closest_job_is_correct(self):
        job = Job.objects.get(id=1)
        result = job.find_match_closest_job()
        self.assertEquals("software engineer", result['normalized_job_title'])

    def test_find_related_skills(self):
        job = Job.objects.get(id=1)
        result = job.find_related_skills()
        self.assertEquals(119, len(result))

