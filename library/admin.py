from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from library.models import Reader, Books, Author


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_link', 'count_page', 'count_books', 'created')
    actions = ['updated_count_books']

    @admin.action(description='Изменение количества книг: на 0')
    def updated_count_books(self, request, queryset: QuerySet):
        count = queryset.update(count_books=0)
        self.message_user(request, f'Из библиотеки удалено {count} книг. ')

    def author_link(self, obj):
        aut = obj.author
        url = reverse("admin:library_author_changelist") + str(aut.pk)
        return format_html(f'<a href="{url}">{aut}</a>')

    author_link.short_description = 'Автор'


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'telephone', 'display_active_books', 'status', 'created')
    list_filter = ('status',)
    search_fields = ('surname',)
    list_display_links = ('surname',)
    actions = ['updated_status', 'deleted_books']

    @admin.action(description='Изменить статус читателя')
    def updated_status(self, request, queryset: QuerySet):
        queryset.update(status=False)

    @admin.action(description='Удаление всех книг у читателя')
    def deleted_books(self, request, queryset: QuerySet):
        for obj in queryset:
            obj.active_books.clear()


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'created', 'updated')


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
