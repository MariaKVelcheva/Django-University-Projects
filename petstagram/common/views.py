from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView, CreateView
from pyperclip import copy

from petstagram.common.forms import CommentForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo


class HomePageView(ListView):
    model = Photo
    form_class = CommentForm
    context_object_name = 'photos'
    template_name = 'common/home-page.html'


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
