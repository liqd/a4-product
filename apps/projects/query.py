from django.db.models import Q


def filter_viewable(queryset, user):
    # FIXME: has to be in sync with a4projects.view_project or here
    #        a4_candy_projects.view_project and should
    #        be implemented on the Project's QueryManager/QuerySet.
    #        Unfortunately that is not possible, as the QueryManager may not
    #        be overwritten and the Project model is not swappable.
    if user.is_superuser:
        return queryset
    elif user.is_authenticated:
        return queryset.filter(
            Q(is_public=True) |
            Q(participants__in=[user.pk]) |
            Q(organisation__initiators__id__in=[user.pk]) |
            Q(moderators__in=[user.pk])
        ).distinct()
    else:
        return queryset.filter(
            is_public=True
        )
