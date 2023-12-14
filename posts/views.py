from django.shortcuts import render, redirect
from . import forms 
from . import models

# Create your views here.

def add_post(request):
    if request.method == 'POST': # user post request korche 
         post_form = forms.PostForm(request.POST) # user er post request data store 
         if post_form.is_valid(): # data valid check kora hoitase 
              post_form.save() #  if data valid then sate the database 
              return redirect('add_post') #  return  'add_author ' url pathiye dibo 
         
    else:  # user normally website e gele blank form pabe 
        post_form = forms.PostForm( )
    return render(request, 'add_post.html',{'form' : post_form})



def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST': # user post request korche 
         post_form = forms.PostForm(request.POST, instance=post) # user er post request data store 
         if post_form.is_valid(): # data valid check kora hoitase 
              post_form.save() #  if data valid then sate the database 
              return redirect('homepage') #  return  'add_author ' url pathiye dibo 
         
    
    return render(request, 'add_post.html',{'form' : post_form})


def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')