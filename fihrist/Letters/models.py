from django.db import models

class letters_uz(models.Model):
	id = models.IntegerField(primary_key=True)
	letter = models.CharField(max_length=5)


#letters_uz.objects.raw('sql')



