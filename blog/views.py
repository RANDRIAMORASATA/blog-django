from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os
from blog.forms.ContactForm import ContactForm
from blog.forms.CreateNewPostForm import CreateNewPostForm
from blog.models import Category, Tag, Comments, Post, Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello World !</h1>")

def index(request):
    # categories = ["Informatiques", "Marketing", "Langues", "Digital"]
    # for name in categories:
    #     category = Category()
    #     category.name = name
    #     category.description = f"Description de la category : {name}"
    #     category.save()

    # tags = ["web", "front", "back", "Digital"]
    # for name in tags :
    #     tag = Tag()
    #     tag.name = name
    #     tag.description = f"Voici le tag {name}"
    #     tag.save()

        
    title = "Hello world !"
    posts_list= Post.objects.all()
    print ("------",os.getcwd())
    paginator = Paginator(posts_list,8)
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)
    except :
        posts = paginator.page(1)
   
    return render(
        request, "blog/index.html", 
        {'title': title, 'posts': posts})

def post(request):
    title = "New post !"
    content = '<p>Votre new post</p>'
    return render(request, 'blog/post.html', {'title': title, 'content': content})

def single_post(request, slug):
    # print(type(slug))
    # print(request.GET)
    # print(request.POST)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/single_post.html',{'post': post})

def contact(request):
    if request.method == 'POST':
    #traitement des données
        
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message est envoyé avec succès")
            return redirect('contact')
    else:
         form = ContactForm()
   
    return render(request, "blog/contact.html", {'form' : form})

@login_required
def dashboard_post(request):
    #posts_list= Post.objects.all().order_by('createdAt')
    posts_list= Post.objects.filter(author=request.user).order_by('createdAt')
    paginator = Paginator(posts_list,8)
    page = request.GET.get('page',1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)
    except :
        posts = paginator.page(1)
    return render(request, "blog/dashboard/post_index.html", {'posts': posts})

@login_required
def dashboard_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/dashboard/post_view.html',{'post': post})

@login_required
def dashboard_post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        form = CreateNewPostForm(request.POST, request.FILES ,instance=post)
        old_image = post.image
        if form.is_valid():  
            if request.FILES.get('image'):  # Replace 'image' with the actual field name
                if old_image and os.path.isfile(os.path.join(settings.MEDIA_ROOT, old_image.name)):
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_image.name))
            form.save()
            messages.success(request, "Votre post est modifié avec succès")
            return redirect('dashboard_post_edit', slug=post.slug)
            return redirect('dashboard_post_edit',  slug=post.slug)  # Redirection vers la liste des posts
    else:
        form = CreateNewPostForm(instance=post)

    return render(request, 'blog/dashboard/post_new.html', {'form': form, 'post': post})

@login_required
def dashboard_post_new(request):
     if request.method == 'POST':
        #traitement des données     
        form = CreateNewPostForm(request.POST,  request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Votre post est enregistrée avec succès")
            return redirect('dashboard_post_new')
     else:
        form = CreateNewPostForm()

        return render(request, 'blog/dashboard/post_new.html',{'form': form})

@login_required  
def dashboard_post_delete(request, slug):
         post = get_object_or_404(Post, slug=slug)
         if post.author != request.user:
                messages.success(request, "Vous n etes pas accès à supprimer ce post !") 
                return redirect('dashboard_post')
         if request.method == 'POST':
                if request.POST.get('_method') == 'DELETE':
                        if post.image:
                            image_path = post.image.path
                            if os.path.exists(image_path):
                                os.remove(image_path)       
                        post.delete()
                        messages.success(request, "Votre post est suprimée avec succès") 
                return redirect('dashboard_post')   
         return redirect('dashboard_post')