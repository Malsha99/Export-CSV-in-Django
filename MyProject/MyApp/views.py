# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Post
from .forms import FormatForm
from .admin import PostResource
from django.http import HttpResponse

class PostsListView(ListView,FormView):
    model = Post
    template_name = 'Posts/main.html'
    form_class = FormatForm

    def post(self, request, **kwargs) :
        qs = self.get_queryset()
        dataset = PostResource().export(qs)

        format = request.POST.get('format')

        if format == 'csv':
            ds = dataset.csv
        else:
            ds = dataset.csv


        response = HttpResponse(ds, content_type=f"{format}")
        response['Content-Disposition'] = f"attachment; filename=Dataset.csv"
        return response



