from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView


class PetAddView(TemplateView):
    template_name = 'pets/pet-add-page.html'


class PetDeleteView(TemplateView):
    template_name = 'pets/pet-delete-page.html'


class PetEditView(TemplateView):
    template_name = 'pets/pet-edit-page.html'


class PetDetailsView(TemplateView):
    template_name = 'pets/pet-details-page.html'


