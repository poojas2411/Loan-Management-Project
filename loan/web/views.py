from django.shortcuts import render,HttpResponse,redirect
from . models import userinfo,Car_loan,Home_loan,Contact,Usefull_links,What_we_offer
from django.contrib.auth import logout
# Create your views here.
def home(request):
    usefull=Usefull_links.objects.all()
    return render(request,'index.html',{'usefull':usefull})
def about(request):
    usefull=Usefull_links.objects.all()
    what=What_we_offer.objects.all()
    return render(request,'about.html',{'usefull':usefull,'what':what})

def how(request):
    if(request.method=="GET"):
        usefull=Usefull_links.objects.all()
        return render(request,'how.html',{'usefull':usefull})
    
    elif(request.method=="POST"):
        apply=Home_loan()
        apply.loan_type=request.POST.get('loan_type')
        apply.Bank_name=request.POST.get('bank_name')
        apply.Account_number=request.POST.get('account_number')
        apply.Bank_ifsc=request.POST.get('ifsc_code')
        apply.Aadhaar_no=request.POST.get('aadhaar_number')
        apply.pancard_number=request.POST.get('pancard_number')
        apply.Address=request.POST.get('address')
        apply.phone_no=request.POST.get('phone_number')
        apply.Email=request.POST.get('email')
        apply.money=request.POST.get('money')
        #apply.pan_card=request.FILES['pan_photo']
        #apply.Aadhaar_card=request.FILES['adhar_photo']
        
        apply.save()
        #Home=Home_loan.objects.create(loan_type=loan_type,Bank_name=bank_name,Account_number=account_number,Bank_ifsc=ifsc_code,Aadhaar_no=adhar_no,pancard_number=pan_no,Address=addres,phone_no=phone_no,Email=email,money=money,Aadhaar_card=adhar_card,pan_card=pan_card)
        #Home.save()
        return render(request,'submited.html')
    
def loan_status(request):
    loanre=Home_loan.objects.filter(status=1)
    re_aprove=Home_loan.objects.filter(status=2)
    re_loan=Home_loan.objects.filter(status=0)
    usefull=Usefull_links.objects.all()
    return render(request,'loan.html',{'loanre':loanre,'re_aprove':re_aprove,'re_loan':re_loan,'usefull':usefull})

def contact(request):
    if(request.method=="GET"):
        usefull=Usefull_links.objects.all()
        return render(request,'contact.html',{'usefull':usefull})
    elif(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        usefull=Usefull_links.objects.all()
        con=Contact.objects.create(name=name,email=email,message=message)
        con.save()
        return render(request,"contact.html",{'usefull':usefull,'message':'Our Team will contact you soon','userfull':usefull})
   

def out(request):
    logout(request)
    return redirect('acc')