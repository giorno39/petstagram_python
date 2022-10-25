from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.


def index(request):
    photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    context = {
        "all_photos": photos,
        "comment_form": comment_form,
        "search_form": search_form,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    form = CommentForm(request.POST)
    photo = Photo.objects.filter(id=photo_id).get()  # possibly pk=photo_id
    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()

    return redirect('index')
