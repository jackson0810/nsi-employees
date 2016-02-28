import shutil

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from internal.forms import NewsItemForm, FunctionalCapabilityForm, TaskOrderForm
from shared.models import NewsItem, FunctionalCapability, TaskOrder, ImageItem


def home(request):
    return render(request, 'home.html')


def news_items(request, news_uuid=None):
    items = NewsItem.objects.all()
    news_item = None

    if news_uuid:
        try:
            news_item = items.get(news_uuid=news_uuid)
        except NewsItem.DoesNotExist:
            messages.error(request, 'The news item selected to be edited no longer exists.')

            return redirect('internal:news_items')

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

    return render(request, 'news_items.html', {'form': form, 'news_items': items, 'news_uuid': news_uuid})


def delete_news_item(request, news_uuid):
    try:
        news_item = NewsItem.objects.get(news_uuid=news_uuid)
        news_item.delete()

        messages.success(request, 'The news items was deleted')
    except NewsItem.DoesNotExist:
        messages.error(request, 'The news item selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected new item.  Please try again.')

    return redirect('internal:news_items')


def functional_capabilities(request, capability_uuid=None):
    items = FunctionalCapability.objects.all()
    func_capability_item = None

    if capability_uuid:
        try:
            func_capability_item = items.get(capability_uuid=capability_uuid)
        except FunctionalCapability.DoesNotExist:
            messages.error(request, 'The functional capability selected to be edited no longer exists.')

            return redirect('internal:functional_capabilities')

    if request.method == 'POST':
        form = FunctionalCapabilityForm(request.POST, instance=func_capability_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.updated_by = request.user
            item.save()

            messages.success(request, 'The functional capability was saved successfully.')
            return redirect('internal:functional_capabilities')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = FunctionalCapabilityForm(instance=func_capability_item)

    return render(request, 'functional_capabilities.html', {'form': form, 'func_items': items,
                                                            'capability_uuid': capability_uuid})


def delete_func_capability(request, capability_uuid):
    try:
        func_capability_item = FunctionalCapability.objects.get(capability_uuid=capability_uuid)
        func_capability_item.delete()

        messages.success(request, 'The functional capability was deleted')
    except FunctionalCapability.DoesNotExist:
        messages.error(request, 'The functional capability selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected functional capability.  Please try again.')

    return redirect('internal:functional_capabilities')


def handle_uploaded_file(f):
    with open('{}/documents'.format(settings.STATIC_ROOT), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def task_orders(request, task_uuid=None):
    items = TaskOrder.objects.all()
    task_order_item = None

    if task_uuid:
        try:
            task_order_item = items.get(task_uuid=task_uuid)
        except TaskOrder.DoesNotExist:
            messages.error(request, 'The task order selected to be edited no longer exists.')

            return redirect('internal:task_orders')

    if request.method == 'POST':
        form = TaskOrderForm(request.POST, request.FILES, instance=task_order_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.updated_by = request.user
            item.save()

            # move the document to shared/static/documents
            shutil.move('{}{}'.format(settings.MEDIA_ROOT, item.document), '{}/shared/static/documents/'.format(
                settings.SITE_ROOT, settings.STATIC_ROOT,))

            messages.success(request, 'The task order was saved successfully.')
            return redirect('internal:task_orders')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = TaskOrderForm(instance=task_order_item)

    return render(request, 'task_orders.html', {'form': form, 'task_order_items': items, 'task_uuid': task_uuid})


def delete_task_order(request, task_uuid):
    try:
        task_order_item = TaskOrder.objects.get(task_uuid=task_uuid)
        task_order_item.delete()

        messages.success(request, 'The task order was deleted')
    except TaskOrder.DoesNotExist:
        messages.error(request, 'The task order selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected task order.  Please try again.')

    return redirect('internal:task_orders')
