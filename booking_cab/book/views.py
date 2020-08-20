from django.shortcuts import render,redirect
from book.models import Book
from book.forms import BookForm
from authenticate import Authentication
# Create your views here.
#@Authentication.valid_user
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

    book=Book.objects.raw("select * from book limit 4 offset %s",[offset])
    pageItem=len(book)
    return render(request,"book/index.html",{'book':book,'page':page,'pageItem':pageItem})

#Authentication.valid_user
def search(request):
    print(request.POST['search'])
    book=Book.objects.get(email=request.POST['search'])
    return render(request,"book/search.html",{'book':book})

#@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=BookForm(request.POST)
        form.save()
        return redirect("/book")
    else:
        form=BookForm()
    return render(request,"book/create.html",{'form':form})

#@Authentication.valid_user_where_id
def update(request,id):
    book=Book.objects.get(book_id=id)
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        form.save()
        return redirect("/book")
    else:
        form=BookForm(instance=book)
    return render(request,"book/edit.html",{'form':form})

#@Authentication.valid_user_where_id
def delete(request,id):
    book=Book.objects.get(book_id=id)
    book.delete()
    return redirect("/book")
