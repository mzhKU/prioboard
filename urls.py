# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [

    # add your own patterns here
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
