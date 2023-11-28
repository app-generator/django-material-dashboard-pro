from django.urls import path
from admin_material_pro import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('charts/', views.charts, name='charts'),
    path('widgets/', views.widgets, name='widgets'),
    path('calendar/', views.calendar, name='calendar'),

    # Components
    path('components/buttons/', views.buttons, name='buttons'),
    path('components/grid/', views.grid, name='grid'),
    path('components/panels/', views.panels, name='panels'),
    path('components/sweet-alerts/', views.sweet_alerts, name='sweet_alerts'),
    path('components/notifications/', views.notifications, name='notifications'),
    path('components/icons/', views.icons, name='icons'),
    path('components/typography/', views.typography, name='typography'),

    # Forms
    path('forms/regular-forms/', views.regular_forms, name='regular_forms'),
    path('forms/extended-forms/', views.extended_forms, name='extended_forms'),
    path('forms/validation-form/', views.validation_form, name='validation_form'),
    path('forms/wizard/', views.wizard, name='wizard'),

    # Tables
    path('tables/regular-tables/', views.regular_tables, name='regular_tables'),
    path('tables/extended-tables/', views.extended_tables, name='extended_tables'),
    path('tables/datatables/', views.datatables, name='datatables'),

    # Maps
    path('maps/google-maps/', views.google_maps, name='google_maps'),
    path('maps/fullscreen-maps/', views.fullscreen_maps, name='fullscreen_maps'),
    path('maps/vector-map/', views.vector_map, name='vector_map'),

    # Pages
    path('pages/pricing/', views.pricing, name='pricing'),
    path('pages/lock/', views.lock, name='lock'),
    path('pages/error/', views.error, name='error'),
    path('pages/user-profile/', views.user_profile, name='user_profile'),
    path('pages/timeline/', views.timeline, name='timeline'),
    path('pages/rtl-page/', views.rtl_page, name='rtl_page'),

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),

    path('accounts/change-password/', views.UserChangePasswordView.as_view(), name="change_password"),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password-change-done.html"
    ), name="password_change_done"),

    path('accounts/password-reset/', views.UserResetPasswordView.as_view(), name="password_reset"),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password-reset-complete.html'
    ), name='password_reset_complete'),

    path('template/', views.template, name='template'),
]

