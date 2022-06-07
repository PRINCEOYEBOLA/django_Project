from customers.models import Product
#activate the python interactive shell using 'python manage.py shell'
python manage.py shell
#import the Product model as a module from the customers.models
from customers.models import Product
#check for all products alredy added to the Product Model.
Product.objects.all()
#add a new item to the Product Model
x = Product(product_name = "Bournvita", product_price = "1000", product_maker = "Cardbury", product_country = "Nigeria")
#Check the existence of the item name
x.product_name
#Check the existence of the item price
x.product_price
#save the new added item to the Product Model in the database
x.save()
#Change the price of the just added item
x.product_price = "2000"
#Check the change in the price
x.product_price
#save the new price
x.save()
#comfirm the change is stored in the database
x.product_price
#comfirm the item is stored in the database
#Filter the items in the database using their names
Products.objects.filter(product_name)
Product.objects.filter(product_name = "Cross")
Product.objects.filter(product_name = "Cement")
Product.objects.filter(product_name = "Tyre")
Product.objects.filter(product_name = "Iphone 12")

#Filter the items in the database using price
Product.objects.filter(product_price = "5000")
#Filter the first item in the database of the same price
Product.objects.filter(product_price = "5000").first()
#Filter the last item in the database of the same price
Product.objects.filter(product_price = "5000").last()
