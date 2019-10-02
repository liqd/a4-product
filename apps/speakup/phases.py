from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps
from . import models
from . import views


class IssuePhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'issue'
    view = views.SpeakupIdeaListView

    name = _('Issue phase')
    description = _('Add new speakup.')
    module_name = _('speakup collection')
    icon = 'lightbulb-o'

    features = {
        'crud': (models.SpeakupIdea,),
    }


class CollectPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'collect'
    view = views.SpeakupIdeaListView

    name = _('Collect phase')
    description = _('Add new speakup and comment them.')
    module_name = _('speakup collection')
    icon = 'lightbulb-o'

    features = {
        'crud': (models.SpeakupIdea,),
        'comment': (models.SpeakupIdea,),
    }


class RatingPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'rating'
    view = views.SpeakupIdeaListView

    name = _('Rating phase')
    module_name = _('speakup collection')
    description = _('Get quantative feeback by rating the collected speakup.')
    icon = 'chevron-up'

    features = {
        'rate': (models.SpeakupIdea,)
    }


class FeedbackPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'feedback'
    view = views.SpeakupIdeaListView

    name = _('Feedback phase')
    description = _('Get feedback for collected speakup through rates and '
                    'comments.')
    module_name = _('speakup collection')
    icon = 'comment-o'

    features = {
        'rate': (models.SpeakupIdea,),
        'comment': (models.SpeakupIdea,)
    }


class UniversalPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'universal'
    view = views.SpeakupIdeaListView

    name = _('Universal phase')
    module_name = _('speakup collection')
    description = _('Use all features of the speakup collection.')
    icon = 'lightbulb-o'

    features = {
        'crud': (models.SpeakupIdea,),
        'comment': (models.SpeakupIdea,),
        'rate': (models.SpeakupIdea,),
    }


phases.content.register(IssuePhase())
phases.content.register(CollectPhase())
phases.content.register(RatingPhase())
phases.content.register(FeedbackPhase())
phases.content.register(UniversalPhase())
