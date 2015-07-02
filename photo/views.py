from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from albumsite.settings import MEDIA_URL
from django.views import generic
from django.template import RequestContext
from photo.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from photo.forms import UserForm
from photo.forms import AddImage
from albumsite.settings  import MEDIA_ROOT

def main(request):
    """Main listing."""
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 3)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()[:4]

    return render_to_response("photo/list.html", dict(albums=albums, user=request.user,
        media_url=MEDIA_URL))

class DetailView(generic.DetailView):
    model = Image
    template_name = 'photo/image.html'

# class DetailView(generic.DetailView):
#     model = Chart
#     template_name = 'photo/chart.html'

def upload(request):
    image_form = AddImage()
    return render_to_response("photo/upload.html",{'image_form':image_form},context_instance=RequestContext(request))


#register view
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        uform = UserForm(data = request.POST)
        # pform = UserProfileForm(data = request.POST)
        if uform.is_valid():
            user = uform.save()
                # form brings back a plain text string, not an encrypted password
            pw = user.password
                # thus we need to use set password to encrypt the password string
            user.set_password(pw)
            user.save()
            # profile = pform.save(commit = False)
            # profile.user = user
            # profile.save()
            registered = True
        else:
            print uform.errors
    else:
        uform = UserForm()
        # pform = UserProfileForm()

    return render_to_response('photo/register.html', {'uform': uform,  'registered': registered }, context)


# def save_file(file, path=''):
#     filename = file._get_name()
#     fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb' )
#     for chunk in file.chunks():
#         fd.write(chunk)
#         fd.close()  



#login view
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("photo/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print  "invalid login details " + username + " " + password
              return render_to_response('photo/login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render_to_response('photo/login.html', {}, context)
#logout
def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/photo/login/')

def album(request, pk):
    """Album listing."""
    album = Album.objects.get(pk=pk)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")

    images = album.image_set.all()
    paginator = Paginator(images, 4)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)

    return render_to_response("photo/album.html", dict(album=album, images=images, user=request.user,
        media_url=MEDIA_URL))