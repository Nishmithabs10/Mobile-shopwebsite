from django.urls import path
# from .views import home
from.import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('enquiry/', views.enquiry, name='enquiry'),
      path('enquiry_success/', views.enquiry_success, name='enquiry_success'),
   
    # path('contact-success/', TemplateView.as_view(template_name="success.html"), name='contact_success'),
#     path('mobiles/', views.mobiles_list, name='mobiles'),
#     path('enquiry/', views.enquiry_form, name='enquiry'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
 ]
