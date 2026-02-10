from django.views.generic import TemplateView, ListView

from petstagram.photos.models import Photo


class HomePageView(ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'common/home-page.html'






