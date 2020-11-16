from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	student = 1
	mentor = 2
	instructor = 3

	roles = (
		(student, 'Student'),
		(mentor, 'Mentor'),
		(instructor, 'Instructor')
		)

	role = models.PositiveSmallIntegerField(choices = roles, null = True, blank = True)
	pronouns = models.CharField(max_length = 15)
	team = models.ForeignKey('Team', null = True, on_delete = models.SET_NULL)
	buddy = models.ManyToManyField("self", blank=True)

class Team(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name