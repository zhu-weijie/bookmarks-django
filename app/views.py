from django.shortcuts import render, get_object_or_404

from .models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'app/bookmark/list.html', {'bookmarks': bookmarks})


def bookmark_detail(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    return render(request, 'app/bookmark/detail.html', {'bookmark': bookmark})
