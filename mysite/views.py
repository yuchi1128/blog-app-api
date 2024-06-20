from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm


def index(request):
    objs = Article.objects.all()[:3]
    context = {
        'titele': 'Really Site',
        'articles': objs,
    }

    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name = 'mysite/login.html'

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            


