from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns=[
	path('',views.home,name='home'),
	path("",views.home,name="home"),
    path("customers/",views.customers,name="customers"),          #for GET
    path("customers/archived/",views.archived,name="archived"),
    path("customers/<int:id>",views.update,name="update"),
    path("customers/<int:id>/archive/",views.archive,name="archive"),
    path("customers/<int:id>/active/",views.unarchive,name="unarchive"),
    path("customers/<int:id>/milk",views.milk,name="milk"),
]

