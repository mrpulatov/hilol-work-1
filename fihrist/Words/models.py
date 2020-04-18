from django.db import models



class words_uz(models.Model):
	id = models.IntegerField(primary_key=True)
	word = models.CharField(max_length=100)
	letter_id = models.IntegerField()
