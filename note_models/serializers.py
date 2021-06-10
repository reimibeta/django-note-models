from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from note_models.models import Note


class NoteSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Note
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'user',
            'text',
            'is_read',
            'is_edit',
            'created_date',
            'updated_date',
        ]
        expandable_fields = {}
