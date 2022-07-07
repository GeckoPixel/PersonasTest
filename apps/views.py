from django.views.generic.base import TemplateView
from .models import Profile
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from django.utils import timezone

class ProfileView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Perfiles"
        context['profiles'] = Profile.objects.all()
        return context

class ProfileCreate(TemplateView):
    template_name = 'create.html'

    def get(self, request,  *args, **kwargs):
        kwargs["title"] = "Crear Perfil"
        kwargs["form"] = PostForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            print(request.POST)
            form = PostForm(request.POST)
            
            if form.is_valid():
                post = form.save(commit=False)
                post.created_at = timezone.now()
                post.save()
                return redirect('home')
            

class ProfileEdit(TemplateView):
    template_name = 'edit.html'

    def get(self, request, pk=None,  *args, **kwargs):
        post = get_object_or_404(Profile, id=pk)
        kwargs["title"] = "Editar Perfil"
        kwargs['profiles'] = post
        kwargs["form"] = PostForm(instance=post)
        return super().get(request, pk=pk, *args, **kwargs)
    
    def post(self, request, pk=None, *args, **kwargs):
        print(request.POST)
        post = Profile.objects.get(id=pk)
        form = PostForm(request.POST, instance=post)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.now()
            post.save()
        else:
            print(form.errors)

        return redirect('home')

class ProfileDelete(TemplateView):
    template_name = 'delete.html'
    def get(self, request, pk=None, *args, **kwargs):
        post = Profile.objects.get(id=pk).delete()
        return redirect('home')


# Create your views here.
