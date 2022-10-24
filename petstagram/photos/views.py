from django.shortcuts import render, redirect

# Create your views here.
from petstagram.photos.forms import AddPhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


def photo_add(request):
    if request == "GET":
        form = AddPhotoForm()
    else:
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects. \
        filter(pk=pk) \
        .get()



    context = {
        "photo": photo,

    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_edit(request, pk):
    photo = Photo.objects. \
        filter(pk=pk) \
        .get()

    if request == "GET":
        form = EditPhotoForm()
    else:
        form = EditPhotoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('details photo', pk=pk)

    context = {
        "photo": photo,
        'form': form,
        'pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = Photo.objects. \
        filter(pk=pk). \
        get()
    photo.delete()

    # if request == 'GET':
    #     form = DeletePhotoForm(instance=photo)
    # else:
    #     form = DeletePhotoForm(request.POST, instance=photo)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')

    context = {
        # 'form': form,
        'photo': photo,
    }
    return redirect('index')
    # return render(request, 'photos/photo-details-page.html', context)
