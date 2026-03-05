from django.contrib import admin


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title','author','created_at','updated_at')
#     list_filter = ('is_published','created_at')
#     search_fields = ('title','content')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','parent')
#     search_fields = ('name',)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author_name','author_email','contnt')




from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    # Какие колонки показывать в списке
    list_display = ('name', 'created_at')
    # Добавляем поиск по имени, чтобы быстро находить гостей
    search_fields = ('name',)
    # Сортировка: новые гости будут вверху списка
    ordering = ('-created_at',)
