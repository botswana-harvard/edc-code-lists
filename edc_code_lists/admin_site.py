from django.contrib.admin.sites import AdminSite


class EdcCodeListsAdminSite(AdminSite):
    site_header = 'Code Lists'
    site_title = 'Code Lists'
    index_title = 'Code Lists Administration'
    site_url = '/'
edc_code_lists_admin = EdcCodeListsAdminSite(name='edc_code_lists_admin')
