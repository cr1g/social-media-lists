from django_filters import constants, rest_framework as filters


class ListFilter(filters.CharFilter):
    """
    Allows to specify multiple values in 
    query parameters separated by comma.
    """

    def filter(self, qs, value):
        if value in constants.EMPTY_VALUES:
            return qs
        
        values_list = value.split(',')
        qs = super().filter(qs, values_list)
        
        return qs
