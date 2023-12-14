from django.shortcuts import render, redirect
from . import forms 
# Create your views here.


def add_category(request):
    if request.method == 'POST': # user post request korche 
         category_form = forms.CategoryForm(request.POST) # user er post request data store 
         if category_form.is_valid(): # data valid check kora hoitase 
              category_form.save() #  if data valid then sate the database 
              return redirect('add_category') #  return  'add_author ' url pathiye dibo 
         
    else:  # user normally website e gele blank form pabe 
        category_form = forms.CategoryForm( )
    return render(request, 'add_category.html',{'form' : category_form})