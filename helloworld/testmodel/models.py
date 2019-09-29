from django.db import models

# Create your models here.

class Test(models.Model):
	name = models.CharField(max_length = 20)

class Contact(models.Model):
	name = models.CharField(max_length = 200)
	age = models.IntegerField(default = 0)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	contact = models.ForeignKey('Contact',on_delete=models.CASCADE,)
	name = models.CharField(max_length = 200)
	def __unicode__(self):
		return self.name

class Employee(models.Model):
	first_name = models.CharField(db_column='FIRST_NAME', primary_key=True,max_length=20)  # Field name made lowercase.
	last_name = models.CharField(db_column='LAST_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
	age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
	sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
	income = models.FloatField(db_column='INCOME', blank=True, null=True)  # Field name made lowercase.

	def query_by_age(self):
		return self.income

	class Meta:
		managed = False
		db_table = 'employee'