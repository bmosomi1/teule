#from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from sms import views
from django.contrib.auth import views as auth_views
from sms.views import OrderListJson, OrderReportJson, AllMessagesJson
app_name = 'sms'
urlpatterns = [
    # path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login', views.roberms_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('verify/account', views.verify_account, name='verify_account'),
    path('', views.home, name='sms-home'),
    
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

   
    path('apps', views.apps, name='apps'),
    path('home', views.teule_home, name='teule_home'),
    path('home', views.teule_home, name='water_apps'),
    path('main/meter', views.main_meter, name='main_meter'),
    path('main/meter/chart', views.main_meterchart, name='main_meterchart'),
    path('client/dashboard/<int:client_id>', views.client_dashboard, name='client_dashboard'),
    path('send/', views.send, name='send'),
    path('send/plain', views.send_to_plain, name='send_to_plain'),
    path('simple/sms', views.simple_sms, name='simple_sms'),
    path('simple/sms/resend/<int:message_id>', views.simple_sms_resend, name='simple_sms_resend'),
    path('simple/sms/preview', views.simple_sms_preview, name='simple_sms_preview'),
    path('simple/disconnection/reminder/<int:client_id>', views.disconnection_reminder, name='disconnection_reminder'),
    path('import/csv', views.import_csv_2, name='import_csv'),
    path('import/readings/csv', views.import_readings_csv, name='import_readings_csv'),
    path('merge', views.merge_sms_2, name='merge_sms'),
    path('confirm', views.confirm, name='confirm'),
    path('customer/reports/<int:tracking_code>', views.reports, name='customer_reports'),
    path('water/sms/reports/<int:tracking_code>', views.water_sms_reports, name='water_sms_reports'),
    path('customer/credit', views.customer_credit, name='customer_credit'),
    path('customer/contacts', views.customer_contacts, name='customer_contacts'),
    path('water/clients', views.water_clients, name='water_clients'),
    path('water/clients/<int:court_id>', views.water_clients_court, name='water_clients_court'),
    path('water/payments', views.water_payments, name='water_payments'),
    path('water/payments/unallocated', views.water_payments_unallocated, name='water_payments_unallocated'),
    path('water/payments/<int:client_id>', views.water_payments_clients, name='water_payments_clients'),
    path('water/sub/accounts/<int:main_id>', views.water_subaccounts_allocations, name='water_subaccounts_allocations'),
    path('water/payments/manual', views.water_manual_payments, name='water_manual_payments'),
    path('water/payments/allocations', views.water_payments_allocations, name='water_payments_allocations'),
    path('water/court/allocations', views.water_court_allocations, name='water_court_allocations'),
    path('water/courts', views.water_courts, name='water_courts'),
    path('house/reports', views.house_report, name='house_report'),
    path('teule/clients', views.teule_clients, name='teule_clients'),
    path('teule/vacated/clients', views.teule_vacated_clients, name='teule_vacated_clients'),
    path('teule/vacate/history', views.teule_vacate_history, name='teule_vacate_history'),
    path('add/teule/client', views.create_teule_client, name='create_teule_client'),
    path('teule/client/dashboard/<int:client_id>', views.teule_client_dashboard, name='teule_client_dashboard'),
    path('teule/house/dashboard/<int:house_id>', views.teule_house_dashboard, name='teule_house_dashboard'),
    path('edit/teule/client/<int:client_id>', views.edit_teule_client, name='edit_teule_client'),
    path('teule/main/account', views.teule_main_account, name='teule_main_account'),
    path('teule/revenues', views.teule_revenues, name='teule_revenues'),
    path('teule/houses', views.teule_houses, name='teule_houses'),
    path('house/invoices/<int:house_id>', views.house_invoices, name='house_invoices'),
    path('house/statement/preview/<int:client_id>', views.house_statement_preview, name='house_statement_preview'),
    path('house/invoice/preview/<int:invoice_id>', views.house_invoice_preview, name='house_invoice_preview'),
    path('house/import/clients', views.import_house_clients, name='import_house_clients'),
    path('house/import/houses', views.import_houses, name='import_houses'),
    path('vacate/house/<int:client_id>', views.vacate_house, name='vacate_house'),
    path('teule/house/allocations', views.teule_house_allocations, name='teule_house_allocations'),
    path('edit/teule/house/<int:house_id>', views.edit_teule_house, name='edit_teule_house'),
    path('teule/flats', views.teule_flats, name='teule_flats'),
    path('create/flats', views.create_teule_flat, name='create_teule_flat'),
    path('create/houses', views.create_teule_house, name='create_teule_house'),
    path('teule/caretakers', views.teule_caretakers, name='teule_caretakers'),
    path('teule/payments', views.teule_payments, name='teule_payments'),
    path('teule/payments/<int:client_id>', views.teule_payments_clients, name='teule_payments_clients'),
    path('teule/payments/allocations', views.teule_payments_allocations, name='teule_payments_allocations'),
    path('add/caretakers', views.add_caretaker, name='add_caretaker'),
    path('meter/readers', views.meter_readers, name='meter_readers'),
    path('add/meter/reader', views.add_meter_reader, name='add_meter_reader'),
    #path('water/courts/network', views.water_courts_network, name='water_courts_network'),
    path('create/water/network', views.create_water_network, name='create_water_network'),
    path('edit/client/<int:client_id>', views.edit_water_client, name='edit_water_client'),
    path('edit/water/station/<int:network_id>', views.edit_water_network, name='edit_water_network'),
    path('edit/sms/reading/<int:reading_id>', views.edit_sms_reading, name='edit_sms_reading'),
    path('edit/meter/reader/<int:reader_id>', views.edit_meter_reader, name='edit_meter_reader'),
    path('invoice/preview/<int:invoice_id>', views.invoice_preview, name='invoice_preview'),
    path('bill/preview/<int:invoice_id>', views.bill_preview, name='bill_preview'),
    path('statement/preview/<int:client_id>', views.statement_preview, name='statement_preview'),
    
    path('edit/sysconf/<int:client_id>', views.edit_sys_config, name='edit_sys_config'),
    path('client/invoices/<int:client_id>', views.client_invoices, name='client_invoices'),
    path('client/bills/<int:client_id>', views.client_bills, name='client_bills'),
    #path('client_invoices/<int:client_id>', views.client_invoices, name='client_invoices'),
    path('meter/readings', views.meter_readings, name='meter_readings'),
    path('meter/readings/sms', views.meter_readings_sms, name='meter_readings_sms'),
    path('main/readings', views.main_readings, name='main_readings'),
    path('bills/sent', views.bills_sent, name='bills_sent'),
    path('meter/readings/<int:client_id>', views.meter_readings_clients, name='meter_readings_clients'),
    path('bills/sent/<int:client_id>', views.bills_sent_clients, name='bills_sent_clients'),
    path('add/meter', views.add_meter, name='add_meter'),
    path('add/meter/readings', views.add_meter_readings, name='add_meter_readings'),
    path('add/main/readings', views.add_main_readings, name='add_main_readings'),
    path('add/fines', views.add_fines, name='add_fines'),
    #path('meter/readings/report/<int:report_value>', views.meter_readings_report, name='meter_readings_report'),
    #path('meter/readings/report', views.meter_readings_report, name='meter_readings_report'),
    #path('meter/readings/report', views.meter_readings_report, name='meter_readings_report'),
    path('meter/replace', views.meter_replacement, name='meter_replacement'),
    path('main/meter/replace', views.main_meter_replacement, name='main_meter_replacement'),
    path('water/sysconfig', views.water_system_config, name='water_system_config'),
    path('water/config/history', views.water_config_history, name='water_config_history'),
    path('customer/comprehensive/reports', views.comprehensive_reports, name='comprehensive_reports'),
    path('water/reports', views.meter_readings_report, name='meter_readings_report'),
    path('multisearch', views.multi_search, name='multi_search'),
    path('statement/date', views.statement_date, name='statement_date'),
    
    #path('water/reports', views.water_reports, name='water_reports'),
    #path('water/reports', views.meter_readings_report, name='meter_readings_report'),
    #path('meter/readings/report/<int:report_value>', views.meter_readings_report, name='meter_readings_report'),
    path('sent/report/details/<str:track_code>', views.report_details, name='report_details'),
    path('generate/sms/report/<str:track_code>', views.generate_sms_report, name='generate_sms_report'),
    path('add/meter/upload/', views.add_meter_upload, name='add_meter_upload'),
    path('add/fine/upload', views.add_fine_upload, name='add_fine_upload'),
    path('personalized/sms/menu', views.personalized_sms_menu, name='personalized_sms_menu'),
    path('personalized/contacts', views.personalized_from_contact_list, name='personalized_contacts'),
    path('send/all', views.send_to_all, name='send_to_all'),
    path('send/to/court', views.send_to_court, name='send_to_court'),
    path('send/reminder/network', views.send_reminder_network, name='send_reminder_network'),
    path('send/to/network', views.send_to_network, name='send_to_network'),
    # path('choose/contact/personalized/contactsgroups', views.choose_contact_groups, name='choose_contact_groups'),
    path('contact/list/sample/merged', views.c_sample_merged, name='c_sample_merged'),
    path('messages/dashboard', views.messages_dashboard, name='messages_dashboard'),

    # groups
    path('create/group', views.create_group, name='create_group'),
    path('group/contacts/<int:group_id>', views.group_contacts, name='group_contacts'),
    path('water/courts/network/<int:network_id>', views.water_courts_network, name='water_courts_network'),
    path('create/group/contact/<int:group_id>', views.create_contact, name='create_group_contact'),
    path('create/court/network/<int:network_id>', views.create_court, name='create_network_court'),
    path('import/group/contacts/<int:group_id>', views.import_contacts, name='import_contacts'),
    path('import/water/clients', views.import_water_clients, name='import_water_clients'),
    path('import/water/clients/<int:client_id>', views.import_water_sub_clients, name='import_water_sub_clients'),
    path('delete/group/<int:group_id>', views.delete_group, name='delete_group'),
    path('monthly/credit/usage', views.credit_used, name='credit_usage'),
    path('delete/contacts/<int:contact_id>', views.delete_contact, name='delete_contact'),
    path('update/group/<int:group_id>', views.update_group, name='update_group'),
    path('update/network/<int:network_id>', views.update_network, name='update_network'),
    path('update/contact/<int:contact_id>', views.update_contact, name='update_contact'),
    # path('delete/contact/<int:g')

    path('simple', views.SendSmsView.as_view(), name='sms-simple'),
    path('smsreport', views.SmsReportView.as_view(), name='sms-simple'),
    path('water/revenues', views.water_revenues, name='water_revenues'),
    path('sms/reports', views.sms_reports, name='my_sms_reports'),
    path('water/sent/sms', views.water_sent_sms, name='water_sent_sms'),
    path('water/sent/sms/<str:client_phone>', views.water_sent_sms_client, name='water_sent_sms_client'),
    # path('send/sms', views.send_sms, name='send_sms'),
    # path('get/sms/delivery/status', views.get_delivery_status, name='get_delivery_status'),

    #top up
    path('payment/verification', views.verify_payment, name='verify_payment'),
    path('register', views.register, name='register'),
    path('edit/profile', views.edit_profile, name='edit_profile'),

    # till_numbers
    path('till/numbers', views.customer_till_numbers, name='customer_till_numbers'),
    path('add/till/number', views.add_till_number, name='add_till_number'),
    path('edit/till/number/<int:till_number_id>', views.edit_till_number, name='edit_till_number'),
    path('delete/till/number/<int:till_number_id>', views.delete_till_number, name='delete_till_number'),

    #contacts
    path('activate/deactivate/contact/<int:contact_id>', views.activate_deactivate_contact, name='activate_deactivate_contact'),

    #celery
    path('contacts/upload/status/<str:task_id>', views.contacts_upload_status, name='contacts_upload_status' ),
    path('meter/reading/upload/status/<str:task_id>', views.meter_reading_upload_status, name='meter_reading_upload_status' ),
    path('poll_contact_upload_state/<str:task_id>', views.poll_contact_upload_state, name='poll_contact_upload_state'),

    #trial
    path('get/token', views.trial, name='trial'),

    #docs
    path('documentation', views.documentation, name='documentation'),

    #sender name
    path('sender_name/applications', views.applications, name='applications'),
    path('new/sender_name/application', views.new_application, name='new_application'),
    path('application/contacts/<int:application_id>', views.application_contacts, name='application_contacts'),
    path('add/application/contact/<int:application_id>', views.add_application_contacts, name='add_application_contact'),
    path('download/application/<int:application_id>', views.show_pdf, name='show_pdf'),

    #inbox
    # path('inbox', views.inbox, name='inbox'),

    path('offers', views.offers, name='offers'),
    path('new/tag', views.new_tag, name='new_tag'),
    path('tags', views.get_tags, name='get_tags'),
    path('create_client', views.create_client, name='create_client'),
    path('water/create/client', views.create_water_client, name='create_water_client'),
    path('water/create/client/<int:main_client_id>', views.create_water_sub_client, name='create_water_sub_client'),
    path('import/meter/readings', views.import_meter_readings, name='import_meter_readings'),
    path('import/fine/readings', views.import_fine_readings, name='import_fine_readings'),
    path('tag/messages/<int:tag_id>', views.tag_messages, name='tag_messages'),

    path('express/import/contacts/<int:group_id>', views.express_import_contacts, name='express_import_contacts'),

    path('clean/contacts', views.temp_clean_sys),

    #datatables
    path('my/datatable/data/<int:group_id>/', login_required(OrderListJson.as_view()), name='order_list_json'),
    path('sample/datatable/<int:group_id>', views.sample_datatable, name='sample_datatable'),
    path('sample/datatable/court/<int:network_id>', views.sample_datatable_network, name='sample_datatable_network'),
    path('my/datatablenet/data/<int:network_id>/', login_required(OrderListJson.as_view()), name='order_list_net_json'),
    path('sample/network/<int:network_id>', views.sample_networktable, name='sample_networktable'),
    #path('sample/network', views.sample_networktable, name='sample_networktable'),
    path('sample/water/<int:group_id>', views.sample_water, name='sample_water'),


    path('draw/<str:track_code>', login_required(OrderReportJson.as_view()), name='order_report_json'),
    path('json/all/messages', login_required(AllMessagesJson.as_view()), name='all_messages_json'),

    path('my/payments', views.my_payments, name="my_payments"),
    path('add/patient', views.st_ann_add_patient, name='st_ann_add_patient'),
]