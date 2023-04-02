from django.db import models

# Using the API we populate with planets orbiting planets and their data.
class Planet(models.Model):
	''' 
	Basic planet model. Mass and volumetric values could be numerical types.
	'''
	name 					= models.CharField(max_length=200, primary_key = True)
	mass_value 				= models.CharField(max_length=20, verbose_name="Mass base", blank=True)
	mass_exponent 			= models.CharField(max_length=20, verbose_name="Mass exponent", blank=True)
	volume_value 			= models.CharField(max_length=20, verbose_name="Volume base", blank=True)
	volume_exponent		 	= models.CharField(max_length=20, verbose_name="Volume exponent", blank=True)
	gravity_constant 		= models.FloatField(verbose_name="Gravity constant")
	orbiting 				= models.CharField(max_length=200, verbose_name="Orbiting", blank=True)

	def save(self, *args, **kwargs):
		self.name = self.name.lower()
		return super(Planet, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name
	