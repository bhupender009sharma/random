from django.db import models

# Create your models here.


class Customers(models.Model):
	# id=models.BigAutoField(primary_key=True)
	user_id = models.CharField(max_length=32,blank=True)
	name = models.CharField(max_length=100,blank=True)
	mobile = models.CharField(max_length=10,blank=True)
	address = models.CharField(max_length=300,blank=True)
	pincode = models.CharField(max_length=6,blank=True)

	customer_type = (('individual', 'individual'),
	                 ('professional', 'professional'),)
	type_of_customer = models.CharField(max_length=100, choices=customer_type, default='individual')

	is_active =models.BooleanField(default=True)
	is_archived = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Customers"

	def __str__(self):
		return self.user_id


class DistributionRequired(models.Model):

	customers = models.ForeignKey(Customers, on_delete=models.CASCADE)

	milk_type = (('cow', 'cow'), ('buffalo', 'buffalo'),)
	type_of_milk = models.CharField(max_length=100, choices=milk_type,default='cow')

	price = models.FloatField(blank=True)

	unit_type = (('litre', 'litre'), ('kilogram', 'kilogram'),)
	unit = models.CharField(max_length=100, choices=unit_type,default='litre')

	delivery_type = (('morning', 'morning'), ('evening', 'evening'),)
	time_of_delivery = models.CharField(max_length=100, choices=delivery_type,default='morning')

	class Meta:
		verbose_name_plural = "DistributionRequired"

	def __str_(self) -> str:
		return super().__str__()


class DailyDistribution(models.Model):
	customers = models.ForeignKey(Customers, on_delete=models.CASCADE)

	time_type = (('morning', 'morning'), ('evening', 'evening'),)
	time_period = models.CharField(max_length=100,choices= time_type,default='morning')

	quantity =models.FloatField()
	delivered= models.DateField()

	class Meta:
		verbose_name_plural ="DailyDistribution"

	def __str__(self) -> str:
	    return super().__str__()
