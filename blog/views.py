from django.views import generic
from django.shortcuts import render
from .models import Posts

class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'post_detail.html'


def index(request):
    # posts = [
    #     {'title': 'www', 'content': '222', 'author': 'www', 'slug': 'fff'}
    # ]
    dict_ = {'insert_me': 'Я из views'}
    posts = Posts.objects.all()
    context = {'post_list': posts, 'hello': 'WORLD'}


    

    return render(
        request, 
        'index.html', 
        context=context
    )
    
