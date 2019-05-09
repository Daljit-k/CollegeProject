from django.shortcuts import render,redirect,HttpResponse
from .models import signup,complaint,contactform
from django.contrib import messages
from django.contrib import auth

def index(request):
    if request.method == 'POST':
        userid=request.session['username1']
        #data1=request.POST.get('dt','')
        data2=request.POST.get('nm','')
        data3=request.POST.get('em','')
        data33 = request.POST.get('mob', '')
        mainadd = request.POST.get('a1', '')
        if mainadd=="hostel":
            subadd = request.POST.get('subhos', '')
        if mainadd=="department":
            subadd = request.POST.get('br', '')
        if mainadd=="residental area":
            subadd = request.POST.get('add', '')

        data5=request.POST.get('cd','')
        c1=complaint(uid=userid,username=data2,email=data3,complaint_detail=data5,status1="processing",mobile=data33,address=mainadd,subaddress=subadd)
        c1.save()
        #-------Email send code-----------------
        """from django.core.mail import send_mail
        from django.conf import settings
        subject = 'Hello '+data2
        
        message = '''Our Complaint Center will analyze your complaint and take the appropriate measures in order that the reported situation will not occur at any other time in the future.\n\nYour Request will be Handled by Mr.Verma.It will be solved within 24hours\n\nRegards\nTechnical spport Member'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data3,]
        send_mail( subject, message, email_from, recipient_list )"""
        #-----------------------------------
        return render(request,'student/handle_complaint.html',{})
    return render(request,'student/index.html',{})
def about(request):
    return render(request,'student/about-us.html',{})

def contact(request):
    return render(request,'student/contact.html',{})

def sign(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        data1=request.POST.get('fn','')
        data2=request.POST.get('ln','')
        ds1 = request.POST.get('ds', '')
        data3=request.POST.get('em','')
        data4=request.POST.get('ps','')
        data5=request.POST.get('gn','')
        s1=signup(firstname=data1,lastname=data2,email=data3,password=data4,gender=data5,image=myfile,designation=ds1)
        s1.save()
        ff=0
        return render(request,'student/login.html',{'flag':ff})
    else:
        
        return render(request,'student/signup.html')

def log(request):
    if request.method == "POST":
            uss=request.POST['em']
            pss=request.POST['ps']
            try:
                d1=signup.objects.get(email=uss,password=pss)
            except signup.DoesNotExist:
                messages.error(request,'Username or password not exist')
                return render(request,'student/login.html')
            else:    
                if(uss==d1.email and pss==d1.password):
                    request.session['username1'] = d1.id
                    return redirect('index1')
                else:
                    return render(request,'student/login.html')
    return render(request,'student/login.html')
 
def prof(request):
    uid=request.session['username1']
    s1=signup.objects.get(id=uid)
    return render(request,'student/blog.html',{'s1':s1})
def lgout(request):
    auth.logout(request)
    try:
        del request.session['username1']
    except KeyError:
        pass 
    return redirect('log1')
def updt(request):
    uid = request.session['username1']
    if request.method == 'POST':
        s1 = signup.objects.get(id=uid)
        simg=s1.image
        myfile = request.FILES.get('ff', simg)
        data1 = request.POST.get('fn', '')
        data2 = request.POST.get('ln', '')
        data3 = request.POST.get('em', '')
        data4 = request.POST.get('gn', '')
        s1 = signup.objects.get(id=uid)
        s1.firstname=data1
        s1.lastname=data2
        s1.email = data3
        s1.gender = data4
        s1.image = myfile
        s1.save()
        #s1 = signup(firstname=data1, lastname=data2, email=data3, gender=data4, image=myfile)
        #s1.save()
        #s1 = signup.objects.filter(id=uid).update(firstname=data1, lastname=data2, email=data3, gender=data4,image=myfile)

        return redirect('profile1')
    else:

        return render(request, 'student/signup.html')

def st(request):
        from datetime import datetime
        uid = request.session['username1']
        s1 = signup.objects.get(id=uid)
        c1 = complaint.objects.filter(uid=uid)
        for j in c1:
            query_date=j.date
            delta = datetime.now().date() - query_date
            if (delta.days) >= 1:
                #s1 = signup.objects.get(id=uid)
                j.status1 = "complete"
                j.save()
        return render(request, 'student/status.html',{'c1':c1,'s1':s1})


def csend(request):
    if request.method == 'POST':
        uid = request.session['username1']

        data1 = request.POST.get('nm', '')

        data2 = request.POST.get('em', '')
        data3 = request.POST.get('sub', '')
        data4 = request.POST.get('msg', '')
        messages.error(request, 'Messege send')
        s1 = contactform(uid=uid,uname=data1, email=data2, subject=data3, message=data4)
        s1.save()

        return render(request, 'student/contact.html')
    else:

        return render(request, 'student/contact.html')
def forgot(request):
    if request.method == 'POST':
        data1=request.POST.get('em','')
        import random
        str1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        str2 = random.sample(str1, k=2)
        l1=str2[0]
        l2=str2[1]

        deck = range(1289, 9999)
        hand = random.sample(deck, k=1)
        # print(hand)
        hh = hand[0]
        newpass=str(l1)+str(hh)+str(l2)



        # -------Email send code-----------------
        """from django.core.mail import send_mail
        from django.conf import settings
        subject = 'change Password'

        message = '''Our Team send You a new generated Password.\n\nYour New password is='''+str(newpass)+'''\nYou can later change it.\n\nRegards\nTechnical spport Member'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data1,]
        send_mail( subject, message, email_from, recipient_list )"""
        # -----------------------------------
        # ---update to database

        s1 = signup.objects.get(email=data1)
        s1.password = newpass
        s1.save()
        return redirect('log1')
    else:
        return redirect('log1')
