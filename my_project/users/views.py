from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import ListView


# Create your views here.
def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# search users
class UserListView(ListView):
    model = User
    template_name = 'users/user-list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = User.objects.filter(Q(username__icontains=query))
        return results
