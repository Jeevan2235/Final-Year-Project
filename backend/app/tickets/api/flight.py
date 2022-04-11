from rest_framework.generics import ListAPIView

from ..models import Flight
from .serializers import FlightSerializer

class FlightListAPI(ListAPIView):
    model = Flight
    serializer_class = FlightSerializer
    permission_classes = ()
    queryset = Flight.objects.filter(cancelled=False)
