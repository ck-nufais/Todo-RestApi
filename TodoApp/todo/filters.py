from django_filters import rest_framework 
from .models import Todo
class TodoFilter(rest_framework.FilterSet):
    name = rest_framework.CharFilter(field_name="text",lookup_expr='istartswith')
    com = rest_framework.BooleanFilter(field_name="is_completed")
    class Meta:
        model = Todo
        fields = ["name","com"]