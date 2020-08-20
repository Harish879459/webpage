from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
def index(request):
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    customers=Customer.objects.raw("select * from customer limit 4 offset %s",[offset])
    pageItem=len(customers)
    return render(request,"customer/index.html",{'customers':customers,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=CustomerForm(request.POST)
        form.save()
        return redirect("/customer")
    else:
        form=CustomerForm()
    return render(request,"customer/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    customer=Customer.objects.get(customer_id=id)
    if request.method=="POST":
        form=CustomerForm(request.POST,instance=customer)
        form.save()
        return redirect("/customer")
    else:
        form=CustomerForm(instance=customer)
    return render(request,"customer/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    customer=Customer.objects.get(customer_id=id)
    customer.delete()
    return redirect("/customer")