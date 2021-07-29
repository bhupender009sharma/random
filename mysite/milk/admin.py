from django.contrib import admin
from .models import Customers,DistributionRequired,DailyDistribution
# Register your models here.
admin.site.register(Customers)
admin.site.register(DistributionRequired)
admin.site.register(DailyDistribution)

