from django.shortcuts import render
from django.views import generic
from .models import Art
from django.urls import reverse_lazy

# Create your views here.
class IndexView(generic.ListView):
    template_name = "artGallery/index.html"
    context_object_name = "list_of_art_names"

    def get_queryset(self):
        return Art.objects.order_by("estimated_evaluation")


class DetailView(generic.DetailView):
    model = Art
    template_name = "artGallery/detail.html"


class CreateArt(generic.CreateView):
    model = Art
    template_name = "artGallery/create.html"
    fields = "__all__"


class UpdateArt(generic.UpdateView):
    model = Art
    template_name = "artGallery/create.html"
    fields = "__all__"


class DeleteArt(generic.DeleteView):
    model = Art
    template_name = "artGallery/delete.html"
    success_url = reverse_lazy("artGallery:index")