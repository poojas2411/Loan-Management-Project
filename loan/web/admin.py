from django.contrib import admin
from . models import userinfo,Home_loan,Car_loan,Usefull_links,Contact,What_we_offer
# Register your models here.

admin.site.register(userinfo)
admin.site.register(Home_loan)
#admin.site.register(Car_loan)
admin.site.register(Usefull_links)
admin.site.register(Contact)
admin.site.register(What_we_offer)