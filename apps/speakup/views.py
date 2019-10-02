from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.filters import views as filter_views
from adhocracy4.modules.models import Module
from adhocracy4.projects.mixins import ProjectMixin

from . import forms
from . import models as speakup_models
from .filters import SpeakupIdeaFilterSet


class SpeakupIdeaListView(
    ProjectMixin,
    filter_views.FilteredListView
):
    model = speakup_models.SpeakupIdea
    paginate_by = 15
    filter_set = SpeakupIdeaFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class SpeakupIdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = speakup_models.SpeakupIdea
    queryset = speakup_models.SpeakupIdea.objects \
        .annotate_positive_rating_count().annotate_negative_rating_count()
    permission_required = 'a4_candy_speakup.view_speakup'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_is_moderator'] = self.object.creator in self.object. \
            project.moderators.all()
        return context


class SpeakupIdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = speakup_models.SpeakupIdea
    form_class = forms.SpeakupIdeaForm
    permission_required = 'a4_candy_speakup.modify_speakup'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = kwargs.get('instance').module
        return kwargs


class SpeakupIdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = speakup_models.SpeakupIdea
    form_class = forms.SpeakupIdeaForm
    slug_url_kwarg = 'module_slug'
    permission_required = 'a4_candy_speakup.propose_speakup'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = Module.objects.get(slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)

    def get_permission_object(self, *args, **kwargs):
        return self.module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_slug'] = self.module.slug
        context['project'] = self.project
        context['mode'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = self.module
        return kwargs


class SpeakupIdeaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = speakup_models.SpeakupIdea
    success_message = _("Your SpeakupIdea has been deleted")
    permission_required = 'a4_candy_speakup.modify_speakup'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SpeakupIdeaDeleteView, self) \
            .delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={
                           'slug': self.object.project.slug,
                           'organisation_slug': self.object.project
                                                    .organisation.slug
                       })
