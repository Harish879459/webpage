from django.shortcuts import render,redirect
from cab.models import Cab
from cab.forms import CabForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
def index(request):
    print(request.method)
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

    cab=Cab.objects.raw("select * from cab limit 4 offset %s",[offset])
    pageItem=len(cab)
    return render(request,"cab/index.html",{'cab':cab,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=CabForm(request.POST,request.FILES)
        form.save()
        return redirect("/cab")
    else:
        form=CabForm()
    return render(request,"cab/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    cab=Cab.objects.get(cab_id=id)
    if request.method=="POST":
        form=CabForm(request.POST,request.FILES,instance=cab)
        form.save()
        return redirect("/cab")
    else:
        form=CabForm(instance=cab)
    return render(request,"cab/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    cab=Cab.objects.get(cab_id=id)
    cab.delete()
    return redirect("/cab")