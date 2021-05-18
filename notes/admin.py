from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'note', 'is_read', 'is_edit', 'created_date', 'updated_date']
    list_display_links = ['note']
    list_per_page = 25
    ordering = ['-created_date']
    search_fields = [
        'note'
    ]
    list_filter = (
        # for ordinary fields
        ('is_read', DropdownFilter),
        ('is_edit', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('currency', RelatedDropdownFilter),
    )

    def note(self, obj):
        # print(len(obj.text))
        if len(obj.text) > 40:
            return "{}...".format(obj.text[:39])
        else:
            return obj.text


admin.site.register(Note, NoteAdmin)
