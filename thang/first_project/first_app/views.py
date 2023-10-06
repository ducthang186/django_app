from django.shortcuts import render
from first_app.models import User1,AccessRecord,MyForm
from .forms import FormName

# Create your views here.
def get_user(request):
    list_users = User1.objects.all()
    user_dict = {'list_users' : list_users}
    return render(request,"user.html",user_dict)
# def index(request):
#     my_dict = {'insert_me' : 'index hehehehe' }
#     return render(request, 'index.html', context=my_dict)

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    return render(request,'index.html', context=date_dict)

def index1(request):
    return render(request,'index1.html')
    
def form_name_view(request):
    form = FormName(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = MyForm( name =form.cleaned_data['name'], 
                         email = form.cleaned_data['email'], 
                         text = form.cleaned_data['text'],)
            print("Validation sucess!")
            print('Name:'+ form.cleaned_data['name'])
            print('Email:'+ form.cleaned_data['email'])
            print('Text:'+ form.cleaned_data['text'])
            obj.save()

    return render(request,'form.html',{'form':form})


            # MyForm.objects.save(
            #     name = form.cleaned_data['name'],
            #     email = form.cleaned_data['email'],
            #     text = form.cleaned_data['text'],
            # )