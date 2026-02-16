from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import BaseFormView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def get_success_url(self):
        return reverse_lazy("details-photo", kwargs={'pk': self.object.pk})


class PhotoDetailsView(BaseFormView, DetailView):
    model = Photo
    form_class = CommentForm
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = self.object.comments.all()
        likes = self.object.likes.all()

        context['comments'] = comments
        context['likes'] = likes

        return context


class PhotoEditView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy("details-photo", kwargs={'pk': self.object.pk})



