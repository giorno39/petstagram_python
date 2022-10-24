from django.shortcuts import render, redirect

# Create your views here.
from petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


def add_pet(request):
    if request == "GET":
        form = AddPetForm()
    else:
        form = AddPetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_name):
    pet = Pet.objects\
        .filter(slug=pet_name)\
        .get()

    if request == "GET":
        form = DeletePetForm(instance=pet)
    else:
        form = DeletePetForm(request.POST, instance=pet)
        form.is_valid()
        form.save()
        return redirect('user profile', pk=1)

    context = {
        'form': form,
        "username": username,
        "pet_name": pet_name,
    }
    return render(request, 'pets/pet-delete-page.html', context)


def details_pet(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request == 'GET':
        form = EditPetForm(instance=pet)
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            redirect('pet details', username, pet_name)

    context = {
        "form": form,
        'username': username,
        'pet_slug': pet_name,
    }
    return render(request, 'pets/pet-edit-page.html', context)
