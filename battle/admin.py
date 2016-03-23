from django.contrib import admin
from .models import Player , Character , Group , Equipment


# Register your models here.
admin.site.register(Player)
admin.site.register(Character)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ( 'equipmentGid', 'equipmentName' , 'equipmentOwner' )

class GroupAdmin(admin.ModelAdmin):
	list_display = ( 'groupGid' , 'groupName' , 'groupOwner')

admin.site.register(Equipment , EquipmentAdmin)
admin.site.register(Group , GroupAdmin)
