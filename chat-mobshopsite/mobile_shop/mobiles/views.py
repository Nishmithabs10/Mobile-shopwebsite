from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader 
from django.contrib import messages


# Create your views here.
from .models import Mobile
from .forms import EnquiryForm

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


#     mobiles = Mobile.objects.all()
#     return render(request, 'mobiles_list.html', {'mobiles': mobiles})
def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form.save()  # Save form data to the database
            success_message = (
                f"Thank you, {form_data['first_name']}! We have received your enquiry about "
                f"{form_data['product']} and will get back to you soon. Here are the details we received: "
                f"Last Name: {form_data['last_name']}, Mobile: {form_data['mobile']}, "
                f"Email Address: {form_data['email_address']}, Enquiry Message: {form_data['enquiry_message']}"
            )
            messages.success(request, success_message)
            return redirect('enquiry_success')  # Redirect to success page
        else:
             messages.error(request, 'Please correct the errors below.')
             return render(request, 'enquiry.html', {'form': form})
    else:
        form = EnquiryForm()

    return render(request, 'enquiry.html', {'form': form})

def enquiry_success(request):
    return render(request, 'enquiry_success.html')

    # if request.method == 'POST':
    #    print(request.POST)
    #    EnquiryFormData=EnquiryForm(request.POST)
    #    if EnquiryFormData.is_valid():
    #        print(EnquiryFormData.cleaned_data)
    #        messages.success(request,'Thankyou ,we will get back shortly')
           
    #    else:
    #        messages.error(request,'please correct the errors below.')
    #    return render(request,'enquiry.html')
    #         # Process form data
    # else:
    #    EnquiryFormRender=EnquiryForm()
    # return render(request,'enquiry.html',{'form':EnquiryFormRender})
# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html'
