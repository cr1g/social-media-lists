from django_filters import rest_framework as filters

from common.filters import ListFilter
from .models import Post


class PostFilterSet(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='date_posted', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='date_posted', lookup_expr='lt')
    collection = ListFilter(field_name='account__person__collections', lookup_expr='in')
    network = ListFilter(field_name='account__network', lookup_expr='in')
    search = filters.CharFilter(field_name='content', lookup_expr='search')

    class Meta:
        model = Post
        fields = (
            'date_from', 'date_to', 'network', 'collection', 'search'
        )
