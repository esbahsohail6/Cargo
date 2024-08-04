from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("handlelogin", views.handlelogin, name="handlelogin"),
    path("data_entry", views.data_entry, name="data_entry"),
    path("checkNIC", views.checkNIC, name="checkNIC"),
    path("savecar", views.savecar, name="savecar"),
    path("saveprofit", views.saveprofit, name="saveprofit"),
    path("savecust", views.savecust, name="savecust"),
    path("checkmodel", views.checkmodel, name="checkmodel"),
    path("checksupp", views.checksupp, name="checksupp"),
    path("view_data", views.view_data, name="view_data"),
    path("suppdatacheck", views.suppdatacheck, name='suppdatacheck'),
    path("checkmodeldataform", views.checkmodeldataform, name='checkmodeldataform'),
    path("savesupp", views.savesupp, name='savesupp'),
    path("saveprofit", views.saveprofit, name="saveprofit"),
    path("sales_save", views.sales_save, name="sales_save"),
    path("deals_save", views.deals_save, name="deals_save"),
    path("soldcar", views.soldcar, name="soldcar"),
    path("unsoldcar", views.unsoldcar, name="unsoldcar"),
    path("custdata", views.custdata, name="custdata"),
    path("carinfo", views.carinfo, name="carinfo"),
    path("suppinfo", views.suppinfo, name="suppinfo"),
    path("update_data", views.update_data, name="update_data"),
    path('check_cust/', views.check_cust, name='check_cust'),
    path('update_cust/', views.update_cust, name='update_cust'),
    path('I_cust/', views.I_cust, name='I_cust'),
    
    
]
