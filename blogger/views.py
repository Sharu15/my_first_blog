from django.shortcuts import render,HttpResponse,get_object_or_404
from blogger.models import BlogPost,Comment
from django.utils import timezone

def home(request):
	posts=BlogPost.objects.all()
	# for post in posts:
	# 	print(posts)
	# print(type(posts))
	return render(request,"home.html",{"posts":posts})

def post_page(request,post_id):
	mypost=BlogPost.objects.get(pk=post_id)	
	comments=Comment.objects.filter(post=mypost)
	context={"post":mypost,"comments":comments}
	return render(request,"post.html",context)

# Create your views here.


def post_list(request):
    posts = BlogPost.objects.filter(date_published=timezone.now()).order_by('date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})    

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})    