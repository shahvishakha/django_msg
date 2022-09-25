from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages #import messages
# Create your views here.



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],

            }
            msg = "\n".join(body.values())
            # try:
                # send_mail(subject,msg,'admin@example.com',['admin@example.com'])
            try:
                print("Email sent.....!!!!", msg)
                
            except NameError:
                messages.error(request,"something wrong in serverside.")
                return redirect("contact")
            # except BadHeaderError:
                # return HttpResponse('Invalid header found.')
            messages.success(request,"Message sent successfully.")     
            return redirect("contact")

    forms = ContactForm()
    # print(data)
    return render(request,'contact.html',{'form':forms})
    # return render(request,"contact.html",{'form': data})       