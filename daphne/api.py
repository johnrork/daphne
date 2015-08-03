from rest_framework import routers, viewsets, serializers
from daphne import models as m

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Page

class TestViewSet(viewsets.ModelViewSet):
    queryset = m.Page.objects.all()
    serializer_class = PageSerializer

router = routers.DefaultRouter()
router.register(r'^users', TestViewSet)


