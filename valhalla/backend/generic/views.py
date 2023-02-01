"""
    We will create our own formats for our API.
"""
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset.x cf
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        if self.read_serializer_class is None:
            return self.write_serializer_class
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class


class APIModelViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    model = None

    def image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        return None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(
                page,
                many=True,
                context={'request': request})
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response({
            'data': serializer.data,
            'status': status.HTTP_202_ACCEPTED,
            'error': None},
            status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.read_serializer_class(instance)
            data = serializer.data
            _status = status.HTTP_202_ACCEPTED
            _error = None
        except ObjectDoesNotExist as e:
            _status = status.HTTP_404_NOT_FOUND
            _error = e
            data = {}
        return Response({
            'data': data,
            'status': _status,
            'error': _error},
            status=_status
        )

    def create(self, request, *args, **kwargs):
        serializer = self.write_serializer_class(
            data=request.data,
            context={'request': request}
        )
        _status = status.HTTP_400_BAD_REQUEST
        data = []
        if serializer.is_valid():
            serializer.save()
            _status = status.HTTP_201_CREATED
            data = serializer.data
        return Response({
            'data': data,
            'status': _status,
            'error': serializer.errors},
            status=_status)

    def update(self, request, *args, **kwargs):
        data = self.request.data
        instance = self.get_object()
        serializer = self.write_serializer_class(instance, data=data)
        _status = status.HTTP_400_BAD_REQUEST
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            _status = status.HTTP_201_CREATED
        return Response({
            'data': data,
            'status': _status,
            'error': serializer.errors},
            status=_status
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        _status = status.HTTP_204_NO_CONTENT
        _error = None
        try:
            instance.is_removed = True
            instance.save()
        except ObjectDoesNotExist as e:
            _status = status.HTTP_404_NOT_FOUND
            _error = e
            pass
        return Response({
            'data': self.request.data,
            'status': _status,
            'error': _error},
            status=_status
        )

