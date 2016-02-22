from django import template

register = template.Library()

def dictionary_lookup(d,k):
    return d[k]

register.filter('dictionary_lookup', dictionary_lookup)