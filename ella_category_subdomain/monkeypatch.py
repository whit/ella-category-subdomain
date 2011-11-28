from urlparse import urlparse

from django.conf import settings
from django.core.urlresolvers import (reverse, RegexURLPattern,
                                      RegexURLResolver)
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
import django.conf.urls.defaults

from .models import CategorySubdomain
from ella.core.models import Category, Placement
from ella.core.cache import get_cached_object


original_url = django.conf.urls.defaults.url

def url(regex, view, kwargs=None, name=None, prefix=''):
    regex_url = original_url(regex, view, kwargs, name, prefix)
    if isinstance(regex_url, RegexURLPattern):
        pass
    if isinstance(regex_url, RegexURLResolver):
        pass
    return regex_url


def do_monkeypatch():
    django.conf.urls.defaults.url = url
