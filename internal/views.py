import shutil

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from internal.forms import NewsItemForm, FunctionalCapabilityForm, TaskOrderForm, ImageItemForm
from shared.models import NewsItem, FunctionalCapability, TaskOrder, ImageItem, ContactItem


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
            item.updated_by = request.user
            item.save()

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


def featured_images(request, image_uuid=None):
    items = ImageItem.objects.all()
    image_item = None

    if image_uuid:
        try:
            image_item = items.get(image_uuid=image_uuid)
        except ImageItem.DoesNotExist:
            messages.error(request, 'The featured image selected to be edited no longer exists.')

            return redirect('internal:featured_images')

    if request.method == 'POST':
        form = ImageItemForm(request.POST, request.FILES, instance=image_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.updated_by = request.user
            item.save()

            messages.success(request, 'The featured image was saved successfully.')
            return redirect('internal:featured_images')
        else:
            print(form.errors)
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = ImageItemForm(instance=image_item)

    return render(request, 'featured_images.html', {'form': form, 'featured_image_items': items,
                                                    'image_uuid': image_uuid})


def delete_featured_image(request, image_uuid):
    try:
        image_item = ImageItem.objects.get(image_uuid=image_uuid)
        image_item.delete()

        messages.success(request, 'The featured image was deleted')
    except ImageItem.DoesNotExist:
        messages.error(request, 'The featured image selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected featured image.  Please try again.')

    return redirect('internal:featured_images')


def contact_items(request, contact_uuid=None):
    items = ContactItem.objects.all()
    contact_item = None

    if contact_uuid:
        try:
            contact_item = items.get(contact_uuid=contact_uuid)
        except ImageItem.DoesNotExist:
            messages.error(request, 'The contact item selected to be edited no longer exists.')

            return redirect('internal:contact_items')

    return render(request, 'contact_items.html', {'contact_items': items, 'contact_uuid': contact_uuid,
                                                  'contact_item': contact_item})


def delete_contact_item(request, contact_uuid):
    try:
        contact_item = ContactItem.objects.get(contact_uuid=contact_uuid)
        contact_item.delete()

        messages.success(request, 'The contact item was deleted')
    except ContactItem.DoesNotExist:
        messages.error(request, 'The contact item selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected contact item image.  Please try again.')

    return redirect('internal:contact_items')
