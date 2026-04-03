from collections import OrderedDict
from dataclasses import asdict

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src.base_dataclasses import ResponseMessage
from src.models.application_models import ApplicationTour
from src.serializers.application_serializers import ApplicationTourSerializer
from src.services.application_services import ApplicationTourCreateSrv


class ApplicationTourViewSet(GenericViewSet):
    """ Работа с заявками """
    serializer_class = ApplicationTourSerializer
    queryset = ApplicationTour.objects.all()

    @action(methods=['POST'], detail=False)
    def create_application(self, request, *args, **kwargs) -> Response:

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if isinstance(serializer.data, OrderedDict):
            application_tour_srv = ApplicationTourCreateSrv(serializer.data)
            return application_tour_srv.execute()

        return Response(
            asdict(
                ResponseMessage(
                    success=True,
                    message="Возникла ошибка",
                    data=None
                )
            ),
            status=422
        )