from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse, response
from .models import Customers, DailyDistribution,DistributionRequired
from .forms import AddCustomer, MilkDistribution,  UpdateCustomer
from django.views import View
from django.core.serializers import serialize
import json

# Create your views here.


def home(response):
    return HttpResponse("Hello World Home Page")

class Customer(View):
    form= AddCustomer()
    def post(self,response,*args,**kwargs):
        
        form = AddCustomer(response.POST)
        render(response,'milk/customers.html',{"form":form})
        if form.is_valid:
            
            user_id= form["user_id"]
            name = form["name"]
            mobile = form["mobile"]
            address = form["address"]
            pincode = form["pincode"]
            type_of_customer = form["type_of_customer"]
            
            cus=Customers(user_id=user_id,
                          name=name,
                          mobile=mobile,
                          address=address,
                          pincode=pincode,
                          type_of_customer=type_of_customer,
                          is_active=True)
            cus.save()
            responseBody = [{"message": "Customer successfully added.",
                 "errors":[],}]
            
            #data = list(Customers.objects.values())
            return JsonResponse({'Response Body':responseBody},status=201)
        
       
        return render(response,'milk/customers.html',{"form":form})
    
    def get(self,response,*args,**kwargs):
        data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer'))
        return JsonResponse({'Response Body':data},status=200)


def customers(response):

    if response.method=="POST":
        if response.POST.get("add"):
            form = AddCustomer(response.POST)

            if form.is_valid: 

                form.save()
                responseBody = [{"message": "Customer successfully added."}]
                
                #data = list(Customers.objects.values())
                #data = list(Customers.objects.filter(is_archived=False).values('user_id','name','mobile','address','pincode','type_of_customer'))
                
                data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer','id'))

                return JsonResponse({'message':responseBody, 'Response Body':data},status=201)
            # qs = Customers.objects.all()
                #qs_json = serializers.serialize('json', qs)
                #return HttpResponse(qs_json,status=201)
            else:
                message= form.errors.as_json()
                qs = Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer')
                list_qs = list(qs)
                data = json.dumps(list_qs)
                return JsonResponse({'message':message, 'Response Body':data},status=201)    
    else:
        form = AddCustomer()

        #List Customers
        #qs = Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer')
        #qs_json = serializers.serialize('json', qs)
        #return HttpResponse(qs_json,status=201)

        return render(response,'milk/customers.html',{"form":form},status=200)


def archived(response):
    data= list(Customers.objects.filter(is_archived=True).values())
    
    return JsonResponse({'Response Body':data},status=200)  

def update(response,id):
    cus = Customers.objects.get(id=id)
    form = UpdateCustomer(instance=cus)
    if response.method=="POST":
        form = UpdateCustomer(response.POST or None ,instance=cus)
        if form.is_valid():
            form.save()
            
            responseBody = [{"message": "Customer successfully updated."}]
            data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer','id'))
            return JsonResponse({'message':responseBody, 'Response Body':data},status=200)
        else:
            message= form.errors.as_json()
            responseBody = [{"message": "Customer Not updated."}]
            data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer'))
            return JsonResponse({'message':message, 'Response Body':data},status=201)
    else:
        return render(response,'milk/updateCustomer.html',{"form":form})

def archive(response,id):
    cus = Customers.objects.get(id=id)
    cus.is_archived = True
    cus.save()
    responseBody = [{"message": "Customer successfully archived."}]
    data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer'))
    return JsonResponse({'message':responseBody, 'Response Body':data},status=200)
    
def unarchive(response,id):
    cus = Customers.objects.get(id=id)
    cus.is_archived = False
    cus.save()
    responseBody = [{"message": "Customer is successfully marked as active."}]
    data = list(Customers.objects.values('user_id','name','mobile','address','pincode','type_of_customer'))
    return JsonResponse({'message':responseBody, 'Response Body':data},status=200)
    
def milk(response,id):
    cus = Customers.objects.get(id=id)
    if response.method=="POST":
        if response.POST.get("save"):
            form = MilkDistribution(response.POST)

            if form.is_valid: 

                form.save()

                data = list(cus.item_set.values('type_of_milk','price','unit','time_of_delivery'))
                responseBody = [{"message": "Milk details successfully added."}]
            
                return JsonResponse({'message':responseBody, 'Response Body':data},status=200)           
            
            else:
                message= form.errors.as_json()
                data = list(cus.item_set.values('type_of_milk','price','unit','time_of_delivery'))
                responseBody = [{"message": "Milk details successfully added."}]
                
                return JsonResponse({'message':message, 'Response Body':data},status=200)    
   
    else:
        form = MilkDistribution()
   
        return render(response,'milk/milk.html',{"form":form},status=200)

