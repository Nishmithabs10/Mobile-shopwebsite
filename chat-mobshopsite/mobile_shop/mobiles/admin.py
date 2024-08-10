from django.contrib import admin




# Register your models here.
from.models import Enquiry
admin.site.register(Enquiry)

from.models import Mobile
admin.site.register(Mobile)

class EnquiryAdmin(admin.ModelAdmin):
    list_display={'first_name','last_name','email_address','mobile','product','submitted_at'}
    list_filter={'product',}
    
admin.site.register(Enquiry,EnquiryAdmin)