from django.contrib import admin
from boards.models import Board, Card, BoardList


class BoardAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_date')


class BoardListAdmin(admin.ModelAdmin):
    list_display = ('board', 'title', 'created_date')


class CardAdmin(admin.ModelAdmin):
    list_display = ('board_list', 'title', 'created_date')


admin.site.register(Board, BoardAdmin)
admin.site.register(BoardList, BoardListAdmin)
admin.site.register(Card, CardAdmin)
