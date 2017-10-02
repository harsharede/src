import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product, userbids
from django.http import Http404, HttpResponseRedirect
from .forms import UserForm
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProdctsSerializer
from django.http import Http404
from django.core import serializers
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .payment import mk_pymt, pymt_status

def get_Product_list(request):
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        prodcts_list = list(Product.objects.all())
        data = serializers.serialize('json', list(prodcts_list), fields=('Product_id','Product_name'))
        # serializer = ProdctsSerializer(prodcts_list, many = True)
        return HttpResponse(data, content_type='application/json')

# def index(request):
#     if not request.user.is_authenticated():
#         return render(request, 'dreambuy/login.html')
#     else:
#         prdt = Product.objects.all()
#         context = {'prdt': prdt}
#         return render(request,"dreambuy/index.html",context)

def index(request):
    prdt = Product.objects.all().order_by('Product_bid_percent').reverse()
    updateMAX_bid()
    updaterank()
    context = {'prdt': prdt}
    return render(request, "dreambuy/index.html", context)

def FAQs(request):
    return render(request, 'dreambuy/FAQs.html',{})

# def detail(request, prdt_id):
#     if not request.user.is_authenticated():
#         return render(request, 'dreambuy/login.html')
#     else:
#         user = request.user
#         prdt = get_object_or_404(Product, Product_id = prdt_id)
#         return render(request, 'dreambuy/details.html', {'prdt': prdt, 'user': user})

def detail(request, prdt_id):
    user = request.user
    prdt = get_object_or_404(Product, Product_id = prdt_id)
    resonse = render(request, 'dreambuy/details.html', {'prdt': prdt})
    return render(request, 'dreambuy/details.html', {'prdt': prdt})

def updateMAX_bid ():
    from . import tests
    idslist = tests.select_task_by_priority()
    for prdt_id in idslist.keys():
        # print(prdt_id)
        try:
            cur_prdt = Product.objects.get(Product_id=prdt_id)
            cur_prdt.Product_MAX_bid = int(cur_prdt.Product_price/500)
            cur_prdt.save()
        except Exception as e:
            print(e)

def updaterank ():
    from . import tests
    idslist = tests.select_task_by_priority()
    for prdt_id in idslist.keys():
        print(prdt_id)
        try:
            cur_prdt = Product.objects.get(Product_id=prdt_id)
            cur_prdt.Product_bid_percent = int((cur_prdt.Product_bids / cur_prdt.Product_MAX_bid)*100)
            cur_prdt.save()
        except Exception as e:
            print(e)

def place_bid(request, prdt_id):
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        if prdt_id:
            if request.method == "POST":
                cur_prdt = Product.objects.get(Product_id=prdt_id)
                cur_prdt_bid_price = cur_prdt.Product_each_bid_cost
                cur_bids = cur_prdt.Product_bids
                cur_palced = int(request.POST.get("quote_bids"))
                cur_bids += cur_palced
                cur_prdt.Product_bids = cur_bids
                user = request.user
                print(user.id)
                purpose = str(prdt_id) + '_' + str(cur_palced) + '_' + str(cur_prdt_bid_price)
                # userbids.objects.create(Product_name=cur_prdt.Product_name,
                #                     Product_id=prdt_id,
                #                     user=user,
                #                     bid_time=str(datetime.datetime.now()),
                #                     bid_count=cur_palced,
                #                     cur_prdt_bid_price = cur_prdt_bid_price,
                #                     pymnt_status='started',
                #                     userid = user.id,
                #                         purpose=purpose)
                cur_prdt.save()
                amt = int(cur_palced)* cur_prdt_bid_price
                purpose = str(prdt_id)+'_'+str(cur_palced)+'_'+str(cur_prdt_bid_price)
                rurl = 'http://34.230.248.248:8000/dreambuy/pymnt/'
                response = mk_pymt(amt=10, purpose=purpose, usr='test1', mblnum='', mlid='', rurl=rurl)
                # print (response)
                pymntpth = response['payment_request']['longurl']
                # print (pymntpth)
                prdt = get_object_or_404(Product, Product_id=prdt_id)
                # return render(request, 'dreambuy/details.html', {'prdt': prdt, 'user': user})
                return HttpResponseRedirect(pymntpth)
        else:
            return HttpResponse("""<h1>Error while placing your bid. Please try again.</h1><a href='dreambuy/index.html'>back</a>""")


def user_bids(request):
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        user = request.user
        user_bids_list = userbids.objects.filter(user=user)
        context = {'user_bids_list': user_bids_list}
        return render(request,"dreambuy/profile.html",context)


def form_request_view(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST.get("quote_bids"))
        prdt = request.POST.get("Product_id")
        user = request.user
        return render(request,'dreambuy/details.html', {'prdt': prdt, 'user': user})

def Api_detail(request, prdt_id=1):
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        prodcts_list = list(Product.objects.get(Product_id=prdt_id))
        data = serializers.serialize('json', list(prodcts_list), fields=('Product_id','Product_name'))
        return HttpResponse(data, content_type='application/json')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    context = {
        "form": form,
    }
    return render(request, 'dreambuy/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'dreambuy/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dreambuy/login.html', {'error_message': 'Invalid login'})
    return render(request, 'dreambuy/login.html', )

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'dreambuy/login.html', context)

def pymnt_success(request):
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        user = request.user
        context = {'user': user}
        return render(request,"dreambuy/pymnt_sucess.html",context)


def pymnt(request):
    # print(request)
    if not request.user.is_authenticated():
        return render(request, 'dreambuy/login.html')
    else:
        str_request = str(request)
        strt = str_request.find("&payment_request_id=")
        payment_request_id = str_request[strt+len('&payment_request_id='):-2]
        response = pymt_status(payment_request_id)
        context = {}
        print(response)
        prdt_id =int(response[0][:1])
        print('prdt_id',prdt_id)
        cur_prdt = Product.objects.get(Product_id=prdt_id)
        cur_prdt_bid_price = cur_prdt.Product_each_bid_cost
        # cur_bids = cur_prdt.Product_bids
        cur_palced = int(response[0][2:3])
        print("cur_palced",cur_palced)
        # cur_bids += cur_palced
        # cur_prdt.Product_bids = cur_bids
        user = request.user
        print(user.id)
        purpose = str(prdt_id) + '_' + str(cur_palced) + '_' + str(cur_prdt_bid_price)
        userbids.objects.create(Product_name=cur_prdt.Product_name,
                                Product_id=prdt_id,
                                user=user,
                                bid_time=str(datetime.datetime.now()),
                                bid_count=cur_palced,
                                cur_prdt_bid_price=cur_prdt_bid_price,
                                pymnt_status='started',
                                userid=user.id,
                                purpose=purpose,
                                payment_request_id=payment_request_id)
        if response[1]!= 'Credit':
            cur_bids = cur_prdt.Product_bids
            cur_bids -= cur_palced
            cur_prdt.Product_bids = cur_bids
            cur_prdt.save()
        return render(request, "dreambuy/pymnt_sucess.html", context)
