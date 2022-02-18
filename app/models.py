
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=   (
        ('CHB','Chabhail'),
        ('BDH','Boudha'),
        ('THL','Thali'),
        ('JRP','Jorpati'),
        ('CHK','Chakrapath'),
        ('GOK','Gokarna'),
        ('MUL','Mulpani'),
        ('GTH','Gothatar'),
        ('BHK','Bhaktapur'),)

class Customer(models.Model):
    name=models.CharField(max_length=40)
    state=models.CharField(max_length=3,choices=CATEGORY_CHOICES)
    city=models.CharField(max_length=70)
    zipcode=models.IntegerField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','MOBILE'),('L','Laptop'),('TW','TopWear'),('BW','BottomWear'),
)
    
class Product(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.IntegerField()
    discount=models.IntegerField()
    description=models.TextField()
    brand=models.CharField(max_length=40)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    image=models.ImageField(upload_to='productimg')
    def __str__(self):
        return str(self.id)
class Cart(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self) :
        return str(self.id)
CATEGORY_CHOICES=(
    ('Accepted','Accepted'),('Packed','Packed'),('On the Way','On the Way'),('Delivered','Delivered'),('Cl','Cancel')
)
class OrderPlace(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateField(auto_now=True)
    status=models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='Pending')
    def __str__(self) :
        return str(self.id)