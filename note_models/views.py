from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_utils.pagination import StandardResultsSetPagination

from note_models.models import Note
from note_models.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = NoteSerializer
