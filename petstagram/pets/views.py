from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetCreateForm, PetDeleteForm, PetEditForm
from petstagram.pets.models import Pet


class PetAddView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={'pk': self.object.pk})


class PetDeleteView(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={"pk": self.object.pk})


class PetDetailsView(DetailView):
    model = Pet
    context_object_name = "pet"
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photos'] = self.object.photos.all()
        context["comment_form"] = CommentForm()

        return context

