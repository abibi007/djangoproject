from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm
from.models import Table20,Image
from django .contrib.auth import logout as logouts
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            country=form.cleaned_data['Country']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            user=Table20.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exist')
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/register')
            else:
                tab=Table20(Name=name,Age=age,Email=email,Country=country,Password=password)
                tab.save()
                messages.success(request,'successful')
                return redirect('/')    

    else:
            form=RegisterForm()    
    
    return render(request,'register.html',{'data':form})   

def index(request):
    return render(request,'index.html',)    

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Table20.objects.get(Email=email)
                if not user:
                    messages.warning(request,'email does not  exist')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/login')
                else:
                    messages.success(request,'successful')
                    return redirect('/home/%s' % user.id) 
    
            except: 
                messages.warning(request,'email or password incorrect')
                return redirect('/login')
    else:
            form=LoginForm()    
    
    return render(request,'login.html',{'data':form})
    

def update(request,id):
    user=Table20.objects.get(id=id)
    if request.method=="POST":
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"updation successful")
            return redirect('/')
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})

def home(request,id):
    user=Table20.objects.get(id=id)
    return render(request,'home.html',{'user':user})


def delete(request,id):
    users=Table20.objects.get(id=id)
    users.delete()
    messages.success(request,'deleted successfully')
    return redirect('/')

def changepassword(request,id):
    user=Table20.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']
            if oldpassword!=user.Password:
                messages.warning(request,'passsword incorrect')
                return redirect('/changepassword/%s '% user.id)
            elif newpassword==oldpassword:
                messages.warning(request,'password same')
                return redirect('/changepassword/%s '% user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,'sucessfully changed password')
                return redirect('/login')
            else:
                user.Password=newpassword
                user.save()               
                messages.success(request,'successful')
                return redirect('/')    

    else:
            form=ChangePasswordForm()    
    
    return render(request,'changepassword.html',{'form':form,'user':user})    

def logout(request):
    logouts(request)
    messages.success(request,'logout successful')
    return redirect('/')

def gallery(request,id):
    details=Image.objects.all()
    return render(request,'gallery.html',{'details':details})

def detail(request,id):
    detail=Image.objects.get(id=id)
    return render(request,'detail.html',{'detail':detail})

    
    