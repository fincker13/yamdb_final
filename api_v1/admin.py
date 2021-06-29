from django.contrib import admin

from api_v1.models import Categories, Genres, Comment, Title, Review


class CategoreiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review_id', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('review_id', 'pub_date', 'author')
    empty_value_display = '-пусто-'


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category')
    search_fields = ('name',)
    list_filter = ('year', 'category')
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title_id', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text',)
    list_filter = ('title_id', 'score', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Categories, CategoreiesAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Title, TitlesAdmin)
admin.site.register(Review, ReviewAdmin)
