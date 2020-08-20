from django.shortcuts import redirect
from user.models import User
from django.contrib import messages
#class where authentication is done
class Authentication:
    def valid_user(function):
        def wrap(request):
            print(request)
            try:
                User.objects.get(email=request.session['email'], password = request.session['password'])

                return function(request)
            except:

                messages.warning(request,'Please enter valid email and password')
            return redirect('/login')
        return wrap

    def valid_user_where_id(function):0

        def wrap(request,id):
             try:
                User.objects.get(email=request.session['email'], password = request.session['password'])
                return function(request,id)
             except:
                messages.warning(request,'Please enter valid email and password')
                return redirect('/login')
        return wrap

