from django.shortcuts import render, redirect

from solo_prep.web.forms import ProfileCreateForms, AlbumCreateForms, AlbumEditForms, AlbumDeleteForms, \
    ProfileDeleteForms
from solo_prep.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)
    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForms()
    else:
        form = AlbumCreateForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'albums/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumEditForms()
    else:
        form = AlbumEditForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForms(instance=album)
    else:
        form = AlbumDeleteForms(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album
    }

    return render(request, 'albums/delete-album.html', context)


def add_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForms(instance=profile)
    else:
        form = ProfileCreateForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


def details_profile(request):
    profile = Profile.objects.all().get()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForms(instance=profile)
    else:
        form = ProfileDeleteForms(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-delete.html', context)