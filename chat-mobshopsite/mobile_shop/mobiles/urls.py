from django.urls import path
from .views import home



urlpatterns = [
    path('', home, name='home'),
   
    # path('contact-success/', TemplateView.as_view(template_name="success.html"), name='contact_success'),
#     path('mobiles/', views.mobiles_list, name='mobiles'),
#     path('enquiry/', views.enquiry_form, name='enquiry'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
 ]
