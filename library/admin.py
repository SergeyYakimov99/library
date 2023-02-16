from django.contrib import admin

from library.models import Reader, Books, Author

admin.site.register(Reader)
admin.site.register(Books)
admin.site.register(Author)
