from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name']='shubham'
    return render(request,'django_session/setsession.html')