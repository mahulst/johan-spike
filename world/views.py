from .models import Entry
from rest_framework import serializers, viewsets, generics, filters
from django.contrib.gis.geos import Point, GEOSGeometry
from django.contrib.gis.measure import Distance, D
from drf_extra_fields.geo_fields import PointField

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    point = PointField(required=False)

    class Meta:
        model = Entry
        fields = ('name', 'point')

# ViewSets define the view behavior.
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryList(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get_queryset(self):
        long = float(self.kwargs['long'])
        lat = float(self.kwargs['lat'])
        pnt = Point(long, lat)
        return Entry.objects.filter(point__distance_lt=(pnt, D(m=500)))