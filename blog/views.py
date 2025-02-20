from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Category,Tags
from .forms import PostForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 


def post_list(request, category_id=None ,taguser_id=None):
    categories = Category.objects.all()

    # Fetch tags (Assuming the Tags model is related to Post model)
    tags = Tags.objects.all()

    if category_id:
        category = Category.objects.get(id=category_id)
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()

    if taguser_id:
        tag = User.objects.get(id=taguser_id)
        print(tag)
        posts = posts.filter(taguser=tag)   

    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'tags': tags})


# def post_list(request):
#      posts = Post.objects.filter().order_by('published_date')
#      return render(request, './blog/post_list.html', {"posts":posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_deatail.html', {'post': post})



def post_new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        thambelimage= request.FILES.get('thambelimage')
        category_id = request.POST.get('category')
        taguser_ids = request.POST.getlist('taguser')  # Tag users ko multiple select karna
        print(thambelimage)
        category = Category.objects.get(id=category_id)  # Category ko fetch karte hain

        post = Post(
            title=title,
            text=text,
            image=image,
            category=category,
            author=request.user,
            thambelimage=thambelimage
        )
        post.save()

        # Tag users ko save karna (Many-to-many relationship)
        for tag_user_id in taguser_ids:
            user = User.objects.get(id=tag_user_id)
            post.taguser.add(user)

        post.save()  # Save post after adding tag users

        return redirect('post_detail', pk=post.pk)

    else:
        categories = Category.objects.all()
        users = User.objects.all()  # All users to tag in the post
        return render(request, 'blog/post_edit.html', {'categories': categories, 'users': users})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":     
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def  user_login(request):
    if request.method == "GET":
        return render(request,'blog/login.html',)
    if request.method=="POST":
        print("post method call ho rhah")
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("username",username)
        print("password",password)
        user = authenticate(request, username=username, password=password)
        print ("user",user)
        if user:

                login( request,user)
                msg="userlogin ho rha,"

                posts = Post.objects.filter().order_by('published_date')
                return render(request, './blog/post_list.html', {"posts":posts,"msg":msg})

                # return redirect('post_list')
        else:
            msg="apka id paasword galat h,"
            return render(request,'blog/login.html',{"msg":msg})
def singup(request): 
    if request.method =="GET":
        print("get function call ho rha h")

        return render (request,'blog/singup.html',) 
    
    if request.method=="POST":
        print("post function call ho rha h")

        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email") 
        confirm_password=request.POST.get("confirm_password")
        print("username",username)
        print(email)
        print(password)
        print(confirm_password)

    if password != confirm_password:
        messages.error( request,"password match nhi ho rha h")
        return render (request,'blog/singup.html',) 

    else:
        user=User.objects.create_user(username=username, password=password,email=email)
        print ("username",username)
        print("password",password)
        print("email",email )
    
        
        return  redirect("login")
def userlogout(request):
    logout(request)
    msg="user logout sussfully"
    return redirect('post_list')




# 



        


   
   
   
   
   
   




# Create your views here.C:\Users\H
# Create your views here.C:\Users\HP\djangogirls\templates\blog\post_list.htmlC:\Users\HP\djangogirls\templates\blog\post_list.html