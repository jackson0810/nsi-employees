from datetime import datetime, timedelta
import shutil
import urllib3

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from internal.forms import NewsItemForm, FunctionalCapabilityForm, TaskOrderForm, ImageItemForm, FormDataForm, \
    FomCategoryForm
from shared.models import NewsItem, FunctionalCapability, TaskOrder, ImageItem, ContactItem, FormData, FormCategory
from shared.utilities import collect_static

http = urllib3.PoolManager()


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

            collect_static()

            if settings.IS_PROD:
                # copy the document to the public site
                shutil.copy(item.document.url, '{}/{}'.format(settings.DOCUMENT_PATH, item.get_document_name))
                http.request('GET', settings.PUBLIC_URL)

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

            collect_static()

            messages.success(request, 'The featured image was saved successfully.')
            return redirect('internal:featured_images')
        else:
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


def forms_items(request, form_uuid=None):
    items = FormData.objects.filter(is_active=True)
    form_item = None

    if form_uuid:
        try:
            form_item = items.get(form_uuid=form_uuid)
        except FormData.DoesNotExist:
            messages.error(request, 'The form selected to be edited no longer exists.')

            return redirect('internal:forms_items')

    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES, instance=form_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.updated_by = request.user
            item.save()
            form.save_m2m()

            collect_static()
            messages.success(request, 'The form was saved successfully.')
            return redirect('internal:forms_items')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = FormDataForm(instance=form_item)

    return render(request, 'manage_forms.html', {'form': form, 'form_items': items, 'form_uuid': form_uuid})


def delete_forms_item(request, form_uuid):
    try:
        form_item = FormData.objects.get(form_uuid=form_uuid)

        # remove the uploaded file.
        form_item.document.delete()

        form_item.delete()

        messages.success(request, 'The form was deleted')
    except FormData.DoesNotExist:
        messages.error(request, 'The form selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected form.  Please try again.')

    return redirect('internal:forms_items')


def employee_forms(request):
    categories = FormCategory.objects.filter(is_active=True)
    items = FormData.objects.filter(is_active=True)

    return render(request, 'forms.html', {'form_items': items, 'categories': categories})


def edit_form_category(request):
    return render(request, 'forms.html')


def form_category(request, category_uuid=None):
    items = FormCategory.objects.filter(is_active=True)

    category_item = None

    if category_uuid:
        try:
            category_item = items.get(category_uuid=category_uuid)
        except FormCategory.DoesNotExist:
            messages.error(request, 'The form category selected to be edited no longer exists.')

            return redirect('internal:forms_items')

    if request.method == 'POST':
        form = FomCategoryForm(request.POST, request.FILES, instance=category_item)

        if form.is_valid():
            item = form.save(commit=False)
            item.updated_by = request.user
            item.save()

            collect_static()
            messages.success(request, 'The form category was saved successfully.')
            return redirect('internal:form_category')
        else:
            messages.error(request, settings.GENERIC_ERROR)
    else:
        form = FomCategoryForm(instance=category_item)

    return render(request, 'form_categories.html', {'form': form, 'items': items, 'category_uuid': category_uuid})


def delete_form_category(request, category_uuid):
    try:
        item = FormCategory.objects.get(category_uuid=category_uuid)
        item.delete()

        messages.success(request, 'The form category was deleted')
    except FormCategory.DoesNotExist:
        messages.error(request, 'The form category selected to be deleted no longer exists.')
    except Exception as e:
        messages.error(request, 'An error occurred deleting the selected form category.  Please try again.')

    return redirect('internal:form_category')
