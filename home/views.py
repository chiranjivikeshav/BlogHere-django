from django.shortcuts import render,redirect ,HttpResponse
from home.models import Contact
from bloghere.models import Post
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home/home.html")
def about(request):
    return render(request,"home/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        content =request.POST['content']
        phone=request.POST['phone']
        email=request.POST['email']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")
def search(request):
    query=request.GET['query']
    if query=="":
        return redirect('home')
    if len(query)>30:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
def signUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')
        if len(username)>11:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username only contains letter and number")
            return redirect('home')
        answers = User.objects.filter(username=username)
        if answers:
            messages.error(request, "Username allready exist")
            return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")

def userLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("blogHome")
        else:
            messages.error(request, "Your Username Or Password may be wrong")
            return redirect("home")

    return HttpResponse("404- Not found")
def userLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def writeBlog(request):
    if request.method=="POST":
        auther=request.POST['authername']
        content =request.POST['blogcontent']
        title=request.POST['blogtitle']
        slug=request.POST['slugtext']
        thumbnail=request.POST['filename']
        if len(auther)<2 or len(slug)<3 or len(content)<10 or len(title)<4:
            messages.error(request, "Please write the blog in order manner")
        else:
            blogcontents=Post.objects.create(auther=auther, content=content, title=title,slug=slug,thumbnail=thumbnail)
            blogcontents.save()
            messages.success(request, "Your blog has been successfuly saved")
    return redirect('/')