from django.views.generic import TemplateView, CreateView, UpdateView, DetailView


class PhotoAddView(TemplateView):
    template_name = 'photos/photo-add-page.html'


class PhotoDetailsView(TemplateView):
    template_name = 'photos/photo-details-page.html'


class PhotoEditView(TemplateView):
    template_name = 'photos/photo-edit-page.html'


