from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='auteur')
	title = models.CharField(max_length=200, verbose_name='titre')
	text = models.TextField(verbose_name='texte')
	created_date = models.DateTimeField(default=timezone.now, verbose_name='date de creation')
	published_date = models.DateTimeField(blank=True, null=True, verbose_name='date de publication')
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
# Create your models here.
