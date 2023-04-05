from django.shortcuts import render,redirect,HttpResponse
from bloghere.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def blogHome(request):
    if request.method=="GET":
        allPosts= Post.objects.all()
        context={'allPosts': allPosts}
        return render(request, "blog/blogHome.html", context)
    if request.method=="POST":
        author=request.POST['authername']
        content =request.POST['blogcontent']
        title=request.POST['blogtitle']
        slug=request.POST['slugtext']
        thumbnail=request.FILES.get('filename')
        if  len(author)<4:
            messages.error(request, "Please write complete name of auther")
        elif  len(slug)<3:
            messages.error(request, "Please write slug in more then 3 charecter ")
        elif  len(content)<10:
            messages.error(request, "Please write content briefly")
        elif  len(title)<4:
            messages.error(request, "Please write complete title of blog")
        elif  thumbnail==None:
            messages.error(request, "Please Choose Image file")
        else:
            blogcontents=Post.objects.create(author=author, content=content, title=title,slug=slug,image=thumbnail)
            blogcontents.save()
            messages.success(request, "Your blog has been successfuly saved")
        return redirect('http://127.0.0.1:8000/bloghere')

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogPost.html", context)