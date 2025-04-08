from rest_framework import viewsets
from .models import Commune
from .serializers import CommuneSerializer
from rest_framework.permissions import IsAuthenticated

class CommuneViewSet(viewsets.ModelViewSet):
    serializer_class = CommuneSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Commune.objects.all()
        nom_commune = self.request.query_params.get('nomCommune', None)
        if nom_commune:
            queryset = queryset.filter(nomCommune__icontains=nom_commune)  # icontains = insensible à la casse
        return queryset

