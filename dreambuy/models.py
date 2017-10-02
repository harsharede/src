from django.db import models
from django.contrib.auth.models import Permission, User

import datetime

# Create your models here.


# class Category(models.Model):
#     category = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.category



def prdtcode():
    import datetime
    nums =[1,2,3,4,5,6,7,8,9,0]
    alphs = ['a','b','c','d','e','f','g','h','i','j']

    now = datetime.datetime.now()
    datestr = str(now.year)
    if now.month < 10:
        datestr += '0'
    datestr += str(now.month)
    if now.day < 10:
        datestr += '0'
    datestr += str(now.day)
    if now.hour < 10:
        datestr += '0'
    datestr += str(now.hour)
    if now.minute < 10:
        datestr += '0'
    datestr += str(now.minute)
    datestrc =''
    # print (datestr)
    for i in  (datestr):
        datestrc += (alphs[int(i)-1])
    return (datestrc)


class Product(models.Model):
    Product_id = models.CharField(max_length=50,unique=True,blank=False,default=prdtcode)
    user = models.ForeignKey(User, default=1)
    # Product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=50,unique=True,blank=False)
    Product_brand = models.CharField(max_length=250,blank=False)
    Product_year = models.CharField(max_length=250)
    Product_price = models.IntegerField(blank=False)
    Product_image = models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_image1 = models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_image2= models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_image3 = models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_image4 = models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_image5 = models.CharField(max_length=25000000, default='http://www.freeiconspng.com/uploads/no-image-icon-15.png')
    Product_details = models.CharField(max_length=11250)
    Product_bids = models.IntegerField(default=0)
    Product_each_bid_cost = models.IntegerField(default=500)
    Product_MAX_bid = models.IntegerField(default=0)
    Product_bid_percent = models.IntegerField(default=0)
    #
    #
    # # def _max_bids(self):
    # #     mbids = int(self.Product_price/self.Product_each_bid_cost)
    # #     return mbids
    # # Product_max_bids = property(_max_bids)
    #
    # Product_max_bids = 10
    #
    # # def _bids_remaining(self):
    # #     bids_remaining = int(self.Product_max_bids - self.Product_bids)
    # #     return bids_remaining
    # # Product_bids_remaining = property(_bids_remaining)
    # Product_bids_remaining = 10
    # # def _bids_percent(self):
    # #     bids_percent = int(self.Product_bids/self.Product_max_bids)
    # #     return bids_percent
    # # Product_bids_percent = property(_bids_percent)
    #
    #
    # # def _max_bids(self):
    # #     if self.Product_bids_remaining > 6:
    # #         Product_MAX_bids = 6
    # #     else:
    # #         Product_MAX_bids = self.Product_bids_remaining
    # #     return Product_MAX_bids
    # #
    # # Product_MAX_bids = property(_max_bids)
    #
    # Product_MAX_bids = 10



    def __str__(self):
        return self.Product_brand + ' - ' + self.Product_name + ' - ' + str(self.Product_price)

class userbids(models.Model):
    Product_id = models.IntegerField()
    Product_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1)
    userid = models.IntegerField(default=1)
    bid_time = models.CharField(max_length=250)
    bid_count = models.IntegerField()
    pymnt_status = models.CharField(max_length=10, default=1)
    cur_prdt_bid_price = models.IntegerField(default=500)
    purpose = models.CharField(max_length=10, default=1)
    payment_request_id = models.CharField(max_length=10, default=1)
