from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'store/store.html',context)

#def login(request):
#    context = {}
#    return render(request, 'store/login.html',context)

#def signup(request):
#    context = {}
#    return render(request, 'store/signup.html',context)


