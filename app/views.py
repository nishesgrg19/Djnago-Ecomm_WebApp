from django.shortcuts import redirect, render
from app.models import Customer,Cart,Product,OrderPlace
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class Productview(View):
    def get(self,request):
        topwear=Product.objects.filter(category='TW')
        bottomwear=Product.objects.filter(category="BW")
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear})
class Product_detail(View):
    def get(self,request,id):
        product_d=Product.objects.get(id=id)
        item_in_cart=False
        if request.user.is_authenticated:
            item_in_cart=Cart.objects.filter(Q(author=request.user) & Q (product=id)).exists()
        else:
            pass
        return render(request,'app/productdetail.html',{'pd':product_d,'item_cart':item_in_cart})
def fashion(request,data):
    if data=='TW' or data=='BW':
        product=Product.objects.filter(category=data)
    return render(request,'app/fashion.html',{'product':product})
@login_required
def add_to_cart(request):
    product=Cart.objects.filter(author_id=request.user.id)
    amount=0
    totalamount=0
    shipping=70.0
    if product:
        for item in product:
                tempamount= item.quantity * item.product.discount
                amount += tempamount
                totalamount=amount+shipping
        return render(request, 'app/addtocart.html',{'product':product,'total':totalamount,'amount':amount})
    else:
        return render(request,'app/emptycart.html')

@login_required    
def cart(request,id):
    product=id     
    Cart.objects.create(author_id=request.user.id,product_id=product,quantity=1)
    return redirect('add-to-cart')
def remove_cart(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect('add-to-cart')
    
    

def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def profile(request):
    if request.method=='GET':
        
        return render(request, 'app/profile.html',{'active':'btn-primary'})
    else:
       name= request.POST['name']
       city=request.POST['city']
       state=request.POST['state']
       zip=request.POST['zip']
       Customer.objects.create(name=name,state=state,city=city,zipcode=zip,author_id=request.user.id)
       messages.success(request,'Successfully added your informatiom !!!')
       return redirect('profile')
       
       
       

        

def address(request):
    if request.method=='GET':
        info=Customer.objects.all()
        return render(request, 'app/address.html',{'active':'btn-primary','info':info})
    
        

def orders(request):
    order=OrderPlace.objects.filter(author=request.user)
    return render(request, 'app/orders.html',{'order':order})

def change_password(request):
    if request.method=="GET":
        return render(request, 'app/changepassword.html')
    else:
        oldpassword=request.POST['oldpassword']
        npassword=request.POST['npassword']
        cpassword=request.POST['cpassword']
        if npassword==cpassword:
            user=authenticate(request,username=request.user.username,password=oldpassword)
            if user is not None:
                user.set_password(npassword)
                user.save()
                messages.success(request,'Succesfully your password has been changed')
                return redirect('changepassword')
            else:
                messages.warning(request,'Incorrect old password')
                return redirect('changepassword')
        else:
            messages.warning(request,'Enter your both message correctly')
            return redirect('changepassword')
            
            

def mobile(request,data=None):
    if data==None:
        mobile=Product.objects.filter(category='M')
       
    elif data=='apple' or data=='samsung':
        mobile=Product.objects.filter(category='M').filter(brand=data)
    return render(request,'app/mobile.html',{'mobile':mobile})
def laptop(request,data=None):
    if data == None:
        laptop=Product.objects.filter(category='L')
    elif data=='dell' or data=='acer':
        laptop=Product.objects.filter(category='L').filter(brand=data)
    return render(request,'app/laptop.html',{'laptop':laptop})
        


def sign_out(request):
    logout(request)
    messages.success(request,'successfully loggedOut')
    return redirect('login')
        

def customerregistration(request):
    if request.method=="GET":
        return render(request, 'app/customerregistration.html')
    else:
       username=request.POST['username']
       email= request.POST['email']
       password=request.POST['password']
       cpassword=request.POST['cpassword']
       if username=="" or email=='':
           messages.warning(request,'Fill up the form completly')
           return redirect('customerregistration')
       else:
            if password==cpassword:
                User.objects.create_user(username=username,password=password,email=email)
                messages.success(request,'Congratulations Successfully registered')
                return redirect('customerregistration')
            else:
                messages.warning(request,'PLZZ FILL THE FORM CORRECTLY !!')
                return redirect('customerregistration')
@login_required
def checkout(request):
    if request.method=='GET':
        cart=Cart.objects.filter(author=request.user)
        address=Customer.objects.filter(author=request.user)
        amount=0
        totalamount=0
        shipping=70.0
        if cart:
            for item in cart:
                tempamount= item.quantity * item.product.discount
                amount += tempamount
                totalamount=amount+shipping
            return render(request, 'app/checkout.html',{'customer':address,'cart':cart,'amount':amount,'total':totalamount})
        else:
            return redirect('checkout')
    else:
        id=request.POST['chooseid']
        user=request.user.id
        customer=Customer.objects.get(id=id)
        cart=Cart.objects.filter(author_id=request.user.id)
        for item in cart:
            OrderPlace.objects.create(author_id=user,customer=customer,product_id=item.product.id,quantity=item.quantity)
            item.delete()
            return redirect('orders')
 
def loggin(request):
    if request.method=='GET':
        form=AuthenticationForm()
        return render(request,'app/sign-in.html',{'form':form})
    else:
        next_url=request.GET.get('next')
        username=request.POST['username']
        password=request.POST['password']
        User=authenticate(request,username=username,password=password)
        if User is not None:
            login(request,User)
            if next_url is not None:
                return redirect(next_url)
            else:
                return redirect('home')
            
        else:
            messages.warning(request,'Your username was invalid')
            return redirect('login')
def forget(request):
    if request.method=='GET':
        return render(request,'app/forget.html')
    else:
        emailv=request.POST['email']
        
        send_meesg(email=emailv)
        return redirect('forget')
  
def send_meesg(email):  
    send_mail(
        'E-mail Verification UPDATE',
        'Verification completed',
        'nishesgrg18@gmail.com',
        [email],
        fail_silently=False,
            )
        
        
