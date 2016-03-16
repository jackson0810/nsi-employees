from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns(
    'internal.views',
    url(r'^$', 'home', name='home'),

    # Featured Images
    url(r'^featured/images/$', 'featured_images', name='featured_images'),
    url(r'^process/featured/image/{}/$'.format(settings.UUID_PATTERN_REGEX), 'featured_images',
        name='edit_featured_image'),
    url(r'^delete/featured/image/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_featured_image',
        name='delete_featured_image'),

    # News Items
    url(r'^news/items/$', 'news_items', name='news_items'),
    url(r'^process/news/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'news_items', name='edit_news_items'),
    url(r'^delete/news/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_news_item', name='delete_news_item'),

    # Functional Capabilities
    url(r'^functional/capabilities/$', 'functional_capabilities', name='functional_capabilities'),
    url(r'^process/functional/capability/{}/$'.format(settings.UUID_PATTERN_REGEX), 'functional_capabilities',
        name='edit_func_capability'),
    url(r'^delete/functional/capability/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_func_capability',
        name='delete_func_capability'),

    # Task Orders
    url(r'^task/orders/$', 'task_orders', name='task_orders'),
    url(r'^process/task/order/{}/$'.format(settings.UUID_PATTERN_REGEX), 'task_orders', name='edit_task_order'),
    url(r'^delete/task/order/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_task_order', name='delete_task_order'),

    # Contact Items
    url(r'^contact/itemss/$', 'contact_items', name='contact_items'),
    url(r'^view/contact/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'contact_items', name='view_contact_item'),
    url(r'^delete/contact/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_contact_item',
        name='delete_contact_item'),

    # Forms
    url(r'^form/categories/$', 'form_category', name='form_category'),
    url(r'^process/form/category{}/$'.format(settings.UUID_PATTERN_REGEX), 'form_category', name='edit_form_category'),
    url(r'^delete/form/category/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_form_category',
        name='delete_form_category'),

    url(r'^forms/$', 'employee_forms', name='employee_forms'),
    url(r'^form/items/$', 'forms_items', name='forms_items'),
    url(r'^process/forms/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'forms_items', name='edit_forms_items'),
    url(r'^delete/forms/item/{}/$'.format(settings.UUID_PATTERN_REGEX), 'delete_forms_item', name='delete_forms_item'),
)
