from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class existdoc(models.Model):
	docindex=models.IntegerField(default=-1)
	raw_path=models.CharField(max_length=200)
	result_path=models.CharField(max_length=200)
	def __str__(self):
		return str([docindex,raw_path,result_path])