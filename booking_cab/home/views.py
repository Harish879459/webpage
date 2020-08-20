from django.shortcuts import render,redirect
from cab.models import Cab
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    cab=Cab.objects.all()
    return render(request,'home/index.html' ,{'cab':cab})

def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})

def login(request):

    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']

       return redirect("/user")
    return render(request,"home/login.html")


def logout(request):
    request.session.clear()
    return redirect("/login")