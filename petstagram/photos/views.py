from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'

    def get_success_url(self):
        return reverse_lazy("details-photo", kwargs={'pk': self.object.pk})


class PhotoDetailsView(DetailView):
    model = Photo
    pk_url_kwarg = 'photo_id'
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
    pk_url_kwarg = 'photo_id'
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy("details-photo", kwargs={'pk': self.object.pk})



