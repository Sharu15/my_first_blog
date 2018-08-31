from django.shortcuts import render,HttpResponse
from blogger.models import BlogPost,Comment

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
    return render(request, 'blog/post_list.html', {})