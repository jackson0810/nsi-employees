from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from internal.forms import NewsItemForm
from shared.models import NewsItem


def home(request):
    return render(request, 'home.html')


def news_items(request, news_uuid=None):
    items = NewsItem.objects.all()
    news_item = None

    if news_uuid:
        news_item = items.get(news_uuid=news_uuid)

    if request.method == 'POST':
        form = NewsItemForm(request.POST, instance=news_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.updated_by = request.user
            item.save()

            messages.success(request, 'The news item was saved successfully.')
            return redirect('internal:news_items')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = NewsItemForm(instance=news_item)

    return render(request, 'news_items.html', {'form': form, 'news_items': items})
