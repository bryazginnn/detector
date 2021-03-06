"""detector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^get_prev_photo$', 'lightsite.views.get_prev_photo_from_ajax', name="get_prev_photo"),
    url(r'^search_logo$', 'lightsite.views.search_logo_from_ajax', name="search_logo"),
    url(r'^check_image$', 'lightsite.views.check_image_from_ajax', name="check_image"),
    url(r'^save_logo$', 'lightsite.views.save_logo_from_ajax', name="save_logo"),
    url(r'^remove_logo$', 'lightsite.views.remove_logo_from_ajax', name="remove_logo"),
    url(r'^remove_company', 'lightsite.views.remove_company_from_ajax', name="remove_company"),
    url(r'^save_stat', 'lightsite.views.save_stat_from_ajax', name="save_stat"),
    url(r'^company/edit/(?P<pk>\d+)$', views.CompanyEditView.as_view(),
        name='company-edit', ),
    url(r'^company/new$', views.CompanyNewView.as_view(),
        name='company-new', ),
    url(r'^company/(?P<pk>\d+)$', views.CompanyView.as_view(),
        name='company-view', ),
    url(r'^companies$', views.ListCompanyView.as_view(),
        name='company-list', ),
    url(r'^statistic', views.ListStatisticView.as_view(),
        name='statistic-list', ),
    url(r'^admin/statistic', views.ListAdminStatisticView.as_view(),
        name='admin-statistic-list', ),
    url(r'^denied', views.DeniedView.as_view(),
        name='denied', ),

    # url(r'^new$', views.CreatePhotoView.as_view(),
    #     name='userphoto-new', ),
    # url(r'^list$', views.ListPhotoView.as_view(),
    #     name='userphoto-list', ),
    # url(r'^search(?P<photo_pk>\d+)$', views.SearchView.as_view(), name='search-done'),
    # url(r'^search$', views.SearchView.as_view(), name='search'),
    # url(r'^search((?:/(?P<photo_id>\d+))|(?:/))?$', 'lightsite.views.init_search',
    #     name='search'),
    # url(r'^load$', views.load,
    #     name='load'),
]
