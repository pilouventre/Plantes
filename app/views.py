from rest_framework import viewsets
from .models import Plante
from .serializers import PlanteSerializer

class PlanteViewSet(viewsets.ModelViewSet):
    queryset = Plante.objects.all()
    serializer_class = PlanteSerializer
