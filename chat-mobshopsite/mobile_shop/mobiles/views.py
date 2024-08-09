from django.shortcuts import render

# Create your views here.
from .models import Mobile
from .forms import EnquiryForm

def home(request):
    return render(request, 'index.html')

# def mobiles_list(request):
#     mobiles = Mobile.objects.all()
#     return render(request, 'mobiles_list.html', {'mobiles': mobiles})

# def enquiry_form(request):
#     if request.method == 'POST':
#         form = EnquiryForm(request.POST)
#         if form.is_valid():
#             # Process form data
#             pass
#     else:
#         form = EnquiryForm()
#     return render(request, 'enquiry_form.html', {'form': form})

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')