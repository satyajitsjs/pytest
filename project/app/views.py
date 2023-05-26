from django.shortcuts import render,redirect
from .models import user,post,like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_list(request):
    posts = post.objects.all()
    user = request.user  # Retrieve user object

    return render(request, 'post_list.html', {'posts': posts, 'user': user})


def post_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        description = request.POST['description']
        try:
            post.objects.filter(title=title).update(title=title,content=content,description=description)
            ob = post.objects.all()
            return redirect('/dashboard',{'posts':ob})
        except Exception as e:
            return render(request,'post_edit.html',{'output':'invalid '+str(e)})
    return render(request, 'post_edit.html')



def dashboard(request):
    if request.method == "POST":
        btn = request.POST['btn']            
        if btn == "Edit":
            title = request.POST['title']
            try:
                ob = post.objects.filter(title=title)
                return render(request,"post_edit.html",{'posts':ob})
            except Exception as e:
                return render(request,"dashboard.html",{'posts':"invalid "+str(e)})

        
        if btn == "Delete":
            title = request.POST['title']
            try:
                ob = post.objects.filter(title=title).delete()
                ob = post.objects.all()
                return redirect (request,'dashboard.html' ,{'posts':ob})
            except Exception as e:
                return render(request,"dashboard.html",{"users":"invalid "+str(e)})
    
    posts = post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})


def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        content = request.POST['content']
        ob = post.objects.create(title=title,description=description,content=content)
        ob.save;
        return render(request,'create_post.html',{'output':'Post created Successfully'})
    return render(request,'create_post.html')
    



# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)

#         if user is not None :
#             if user.is_superuser:
#                 login(request, user)
#                 return redirect('/dashboard')  # Redirect to the dashboard page for superuser
#             else :
#                 return redirect('/list')
#         else:
#             error_message = 'Invalid username or password.'
#             return render(request, 'login.html', {'output': error_message})
#     else:
#         return render(request, 'login.html')



def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            ob = user.objects.get(email=email,password=password)
            request.session['email'] = ob.email
            request.session['password'] = ob.password
            if ob.email == "admin@gmail.com":
                return redirect('/dashboard')
            else:
                return redirect('/list')
        except Exception as e:
            return render(request,'login.html',{'output':'invalid '+str(e)})
    return render (request,"login.html")


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        ob = user.objects.create(Name=name,email=email,password=password)
        ob.save;
        return render(request,"signup.html" , {'output':'Register Successfully'})
    return render(request,"signup.html" )