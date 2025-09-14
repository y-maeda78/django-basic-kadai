from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.views.generic import DetailView

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product                 # Modelを定義して表示する
    # template_name = "list.html"     # Templateの名前を「list」に変更する
    paginate_by = 3                 # ページネーション ３オブジェクトずつ表示する

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
    model = Product
    fields = '__all__'
