from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Bookmark


def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    # Pagination with 3 posts per page
    paginator = Paginator(bookmark_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        bookmarks = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        bookmarks = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        bookmarks = paginator.page(paginator.num_pages)
    return render(request, 'app/bookmark/list.html', {'bookmarks': bookmarks})


def bookmark_detail(request, year, month, day, bookmark):
    bookmark = get_object_or_404(Bookmark,
                                 slug=bookmark,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request, 'app/bookmark/detail.html', {'bookmark': bookmark})
