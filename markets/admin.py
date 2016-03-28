from django.contrib import admin
from .models import MarketBlu , MarketOpp , MarketCon

# Register your models here.
# admin.site.register(MarketBlu)
admin.site.register(MarketOpp)
admin.site.register(MarketCon)



class MarketBluAdmin(admin.ModelAdmin):
    list_display = ( 
          'gid' , 'category' , 'title' , 'corpus' , 'price_flo' 
        , 'price_com' , 'price_hon' , 'price_fav' 
        , 'price_con' , 'created_date' ,  'reputation')
admin.site.register(MarketBlu , MarketBluAdmin)