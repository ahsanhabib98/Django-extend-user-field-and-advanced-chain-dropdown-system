from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class District(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class SubDistrict(models.Model):
	name = models.CharField(max_length=100)
	district = models.ForeignKey(District, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Union(models.Model):
	name = models.CharField(max_length=100)
	subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Village(models.Model):
	name = models.CharField(max_length=100)
	union = models.ForeignKey(Union, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Profile(models.Model):
	gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dis_pro = models.BooleanField(default=False)
	subdis_pro = models.BooleanField(default=False)
	uni_pro = models.BooleanField(default=False)
	vil_pro = models.BooleanField(default=False)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
	subdistrict = models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True)
	union = models.ForeignKey(Union, on_delete=models.SET_NULL, null=True)
	village = models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)
	photo = models.ImageField(upload_to='profile_image', blank=True)
	name = models.CharField(max_length=100)
	father_name = models.CharField(max_length=100)
	mother_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	birthdate = models.DateField()
	nid = models.IntegerField()
	bith_certification_no = models.IntegerField()
	sex = models.CharField(max_length=10, choices=gender_choice)
	is_user = models.BooleanField(default=False)
	is_editor = models.BooleanField(default=False)

	def __str__(self):
		return self.name