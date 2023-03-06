from django.shortcuts import render, get_object_or_404

from .models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'app/bookmark/list.html', {'bookmarks': bookmarks})


def bookmark_detail(request, year, month, day, bookmark):
    bookmark = get_object_or_404(Bookmark,
                                 slug=bookmark,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request, 'app/bookmark/detail.html', {'bookmark': bookmark})
