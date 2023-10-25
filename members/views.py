from django.shortcuts import render,redirect
from .models import Users , Blogs

def index(request):
  return render(request,"index.html")

def login(request):
    return render(request, 'login.html',{"message":""})

def register(request):
  return render(request,"register.html",{"message":""})

def profile(request,id):
    user = Users.objects.get(id=id)
    blogs = Blogs.objects.filter(byid=id)
    context = {
        "user":{"id":user.id,
        "name":user.name,
        "age":user.age,
        "email":user.email,
        "phone":user.phone},
        "blogs":blogs
    }
    return render(request,"profile.html",context)
    
def create_blog(request,name,id):
    return render(request,"create_blog.html",{"id":id,"name":name})

def insert_blog(request,name,id):
  if request.method == 'POST':
        heading = request.POST["heading"]
        content = request.POST["content"]
        blog = Blogs(heading=heading,content=content,byid=id ,byuser=name )
        blog.save()
  return redirect("/")

def all_blogs(request):
  context = Blogs.objects.all().values()
  return render(request,"all_blogs.html",{"context":context})

def registeruser(request):
    if request.method == 'POST':
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]

        # Check if the email already exists
        if Users.objects.filter(email=email).exists():
            return render(request, "register.html",{"message":"Email Already Exist"})
        
        context = {
            "name": name,
            "age": age,
            "email": email,
            "password": password,
            "phone": phone,
        }
        dbname = Users(name=name, age=age, email=email, password=password, phone=phone)
        dbname.save()
        user = Users.objects.get(email=email,password=password)
        return redirect(f"profile/{user.id}")
    else:
        return render(request, "register.html",{"message":"Internal Error"})

def checkuser(request):
   if request.method =="POST":
      email = request.POST["email"]
      password = request.POST["password"]
      if Users.objects.filter(email=email).filter(password=password).exists():
         user = Users.objects.get(email=email,password=password)
         return redirect(f"profile/{user.id}")
      return render(request,"login.html",{"message":"Wrong Credentials"})
      
   

    

















def all_users(request):
  databaseUsers  = Users.objects.all().values()
  context = {
    "users":databaseUsers,
  }
  return render(request,"all_users.html",context)

def details(request , id):
  user = Users.objects.get(id=id)
  context = {
    "user" : user
  }
  return render(request,"details.html",context)

def checkLogin(request):
   if request.method == 'POST':
      name = request.POST["name"]
      email = request.POST["email"]
      password = request.POST['password']
      db = Users.objects.filter(email=email).values()
      if db.password == password:
         return render(request,"profile.html",{"name":name,"email":email,"password":password})
      return render(request,"login.html")

