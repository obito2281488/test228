from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from admin_site.form import CategoryCreateForm
from base.models import Category


class CategoryCreate(View):
    def get(self, request):
        form = CategoryCreateForm()
        return render(request, 'admin/create.html', context={'form': form})

    def post(self, request):
        print(request.FILES)
        form = CategoryCreateForm(request.POST, request.FILES)

        if form.is_valid():
            category = Category()
            category.title = request.POST.get('title')
            category.description = request.POST.get('description')
            category.image = request.FILES.get('image')
            category.is_visible = self.is_visible(request.POST.get('is_visible'))
            category.save()

            return redirect(reverse('categories'))
        return render(request, 'admin/create.html', context={'form': form})

    def is_visible(self, visible):
        if visible == 'on':
            return True
        return False


def categories(request):
    categories = Category.objects.filter(is_visible=True).all()

    return render(request, 'admin/categories.html', context={'categories': categories})