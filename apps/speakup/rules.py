import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import is_context_initiator
from adhocracy4.modules.predicates import is_context_member
from adhocracy4.modules.predicates import is_context_moderator
from adhocracy4.modules.predicates import is_owner
from adhocracy4.modules.predicates import is_public_context
from adhocracy4.phases.predicates import phase_allows_add
from adhocracy4.phases.predicates import phase_allows_change
from adhocracy4.phases.predicates import phase_allows_comment
from adhocracy4.phases.predicates import phase_allows_rate

from .models import SpeakupIdea

rules.add_perm('a4_candy_speakup.rate_speakup',
               is_superuser | is_context_moderator | is_context_initiator
               | (is_context_member & phase_allows_rate))


rules.add_perm('a4_candy_speakup.comment_speakup',
               is_superuser | is_context_moderator | is_context_initiator
               | (is_context_member & phase_allows_comment))


rules.add_perm('a4_candy_speakup.modify_speakup',
               is_superuser | is_context_moderator | is_context_initiator
               | (is_context_member & is_owner & phase_allows_change))


rules.add_perm('a4_candy_speakup.propose_speakup',
               is_superuser | is_context_moderator | is_context_initiator
               | (is_context_member & phase_allows_add(SpeakupIdea)))


rules.add_perm('a4_candy_speakup.view_speakup',
               is_superuser | is_context_moderator | is_context_initiator
               | is_context_member | is_public_context)

rules.add_perm('a4_candy_speakup.export_speakup',
               is_superuser | is_context_moderator | is_context_initiator)
