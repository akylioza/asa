from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

# Create your views here.

class PublicaionsView(generic.ListView):
    template_name = 'publication.html'
    queryset = models.Publication.objects.all()

class PublicationDetailView(generic.DetailView):
    template_name = 'publication_detail.html'
    def get_object(self, **kwargs):
        publication_id = self.kwargs.get('id')
        return get_object_or_404(models.Publication, id=publication_id)

class PublicaionAddView(generic.CreateView):
    template_name = 'add_publication.html'
    queryset = models.Publication.objects.all()
    form_class = forms.ShowForm
    success_url = ''

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PublicaionAddView, self).form_valid(form=form)

class PublicationUpdateView(generic.UpdateView):
    template_name = 'publication_update.html'
    queryset = models.Publication.objects.all()
    form_class = forms.ShowForm
    success_url = ''
    def get_object(self, **kwargs):
        publication_id = self.kwargs.get('id')
        return get_object_or_404(models.Publication, id=publication_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PublicationUpdateView, self).form_valid(form=form)

class PublicationDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = ''
    def get_object(self, **kwargs):
        publication_id = self.kwargs.get('id')
        return get_object_or_404(models.Publication, id=publication_id)

