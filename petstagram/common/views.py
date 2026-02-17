from django.shortcuts import redirect, resolve_url, render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import BaseFormView
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo


class HomePageView(BaseFormView, ListView):
    model = Photo
    context_object_name = "photos"
    template_name = 'common/home-page.html'
    form_class = SearchForm
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["comment_form"] = CommentForm()
        context["search_form"] = SearchForm()

        query_dict = self.request.GET.copy()
        query_dict.pop("page", None)
        context["query_string"] = query_dict.urlencode()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("pet_name")

        if query:
            queryset = queryset.filter(tagged_pets__name__icontains=query)

        return queryset


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url("details-photo", photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def add_comment(request, photo_id):
    photo = Photo.objects.get(id=photo_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")

