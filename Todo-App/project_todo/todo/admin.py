from django.contrib import admin
from todo.models import TodoModel

# Register your models here.
class todoAdminModel(admin.ModelAdmin):
    list_display=('id','task','status',)


admin.site.register(TodoModel, todoAdminModel)