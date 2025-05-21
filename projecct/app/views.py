from django.shortcuts import render, get_object_or_404
from .models import MyModel, Posts
from .forms import MyModelForm
 
# Create your views here.
def app(request):
    return render(request, 'app.html')

def users(request):
    users = MyModel.objects.all
    return render(request, 'users.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(MyModel,pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def user_posts(request):
    return render(request, 'posts.html')

def user_post_view(request):
    posts = None
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            my_model = form.cleaned_data['my_model']
            posts = Posts.objects.filter(my_models = my_model)

    return render(request, 'posts.html', {'form': form, 'posts': posts})