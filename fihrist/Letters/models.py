from django.db import models

class letters_uz(models.Model):
	id = models.IntegerField(primary_key=True)
	letter = models.CharField(max_length=5)

	def __srt__(self):
		return self.letter

#letters_uz.objects.raw('sql')



