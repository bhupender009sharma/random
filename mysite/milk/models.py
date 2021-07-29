from django.db import models

# Create your models here.
class Customers(models.Model):
	#id=models.BigAutoField(primary_key=True)
	user_id = models.CharField(max_length=32)
	name = models.CharField(max_length=100)
	mobile = models.CharField(max_length=10)
	addres = models.CharField(max_length=300)
	pincode = models.CharField(max_length=6)

	customer_type =(('individual','individual'),('professional','professional'),)
	type_of_customer = models.CharField(max_length=100, choices = customer_type)

class DistributionRequired(models.Model):

	customers= models.ForeignKey(Customers,on_delete = models.CASCADE )
	
	milk_type = (('cow','cow'),('buffalo','buffalo'),)
	type_of_milk = models.CharField(max_length=100,choices = milk_type)
	
	price = models.FloatField()
	
	unit_type = (('litre','litre'),('kilogram','kilogram'),)
	unit = models.CharField(max_length=100, choices = unit_type)

	delivery_type = (('morning','morning'),('evening','evening'),)
	time_of_delivery = models.CharField(max_length=100, choices = delivery_type)

class DailyDistribution(models.Model):
	customers =models.ForeignKey(Customers,on_delete = models.CASCADE )


        time_type=(('morning','morning'),('evening','evening'),)
        time_period = models.CharField(max_length=100,choices=time_type)

        quantity =models.FloatField()
        delivered= models.DateField()

        class Meta:
            verbose_name_plural ="DailyDistribution"

        def __str__(self) -> str:
            return super().__str__()

