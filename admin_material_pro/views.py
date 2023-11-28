from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from admin_material_pro.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required




def dashboard(request):
  context = {
    'segment': 'dashboard'
  }
  return render(request, 'pages/dashboard.html', context)

@login_required(login_url='/accounts/login/')
def charts(request):
  context = {
    'segment': 'charts'
  }
  return render(request, 'pages/charts.html', context)

@login_required(login_url='/accounts/login/')
def widgets(request):
  context = {
    'segment': 'widgets'
  }
  return render(request, 'pages/widgets.html', context)

@login_required(login_url='/accounts/login/')
def calendar(request):
  context = {
    'segment': 'calendar'
  }
  return render(request, 'pages/calendar.html', context)


# Components
@login_required(login_url='/accounts/login/')
def buttons(request):
  context = {
    'parent': 'components',
    'segment': 'buttons'
  }
  return render(request, 'pages/components/buttons.html', context)

@login_required(login_url='/accounts/login/')
def grid(request):
  context = {
    'parent': 'components',
    'segment': 'grid_system'
  }
  return render(request, 'pages/components/grid.html', context)

@login_required(login_url='/accounts/login/')
def panels(request):
  context = {
    'parent': 'components',
    'segment': 'panels'
  }
  return render(request, 'pages/components/panels.html', context)

@login_required(login_url='/accounts/login/')
def sweet_alerts(request):
  context = {
    'parent': 'components',
    'segment': 'sweet_alerts'
  }
  return render(request, 'pages/components/sweet-alert.html', context)

@login_required(login_url='/accounts/login/')
def notifications(request):
  context = {
    'parent': 'components',
    'segment': 'notifications'
  }
  return render(request, 'pages/components/notifications.html', context)

@login_required(login_url='/accounts/login/')
def icons(request):
  context = {
    'parent': 'components',
    'segment': 'icons'
  }
  return render(request, 'pages/components/icons.html', context)

@login_required(login_url='/accounts/login/')
def typography(request):
  context = {
    'parent': 'components',
    'segment': 'typography'
  }
  return render(request, 'pages/components/typography.html', context)

# Forms
@login_required(login_url='/accounts/login/')
def regular_forms(request):
  context = {
    'parent': 'forms',
    'segment': 'regular_forms'
  }
  return render(request, 'pages/forms/regular.html', context)

@login_required(login_url='/accounts/login/')
def extended_forms(request):
  context = {
    'parent': 'forms',
    'segment': 'extended_forms'
  }
  return render(request, 'pages/forms/extended.html', context)

@login_required(login_url='/accounts/login/')
def validation_form(request):
  context = {
    'parent': 'forms',
    'segment': 'validation_forms'
  }
  return render(request, 'pages/forms/validation.html', context)

@login_required(login_url='/accounts/login/')
def wizard(request):
  context = {
    'parent': 'forms',
    'segment': 'wizard'
  }
  return render(request, 'pages/forms/wizard.html', context)

# Tables
@login_required(login_url='/accounts/login/')
def regular_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'regular_tables'
  }
  return render(request, 'pages/tables/regular.html', context)

@login_required(login_url='/accounts/login/')
def extended_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'extended_tables'
  }
  return render(request, 'pages/tables/extended.html', context)

@login_required(login_url='/accounts/login/')
def datatables(request):
  context = {
    'parent': 'tables',
    'segment': 'datatables.net'
  }
  return render(request, 'pages/tables/datatables.net.html', context)

# Maps
@login_required(login_url='/accounts/login/')
def google_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'google_maps'
  }
  return render(request, 'pages/maps/google.html', context)

@login_required(login_url='/accounts/login/')
def fullscreen_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'full_screen_maps'
  }
  return render(request, 'pages/maps/fullscreen.html', context)

@login_required(login_url='/accounts/login/')
def vector_map(request):
  context = {
    'parent': 'maps',
    'segment': 'vector_map'
  }
  return render(request, 'pages/maps/vector.html', context)
  

# Pages
@login_required(login_url='/accounts/login/')
def pricing(request):
  context = {
    'parent': 'pages',
    'segment': 'pricing_page'
  }
  return render(request, 'pages/pages/pricing.html', context)

@login_required(login_url='/accounts/login/')
def lock(request):
  context = {
    'parent': 'pages',
    'segment': 'lock_page'
  }
  return render(request, 'pages/pages/lock.html', context)

@login_required(login_url='/accounts/login/')
def error(request):
  context = {
    'parent': 'pages',
    'segment': 'error_page'
  }
  return render(request, 'pages/pages/error.html', context)

@login_required(login_url='/accounts/login/')
def user_profile(request):
  context = {
    'parent': 'pages',
    'segment': 'user_profile'
  }
  return render(request, 'pages/pages/user.html', context)

@login_required(login_url='/accounts/login/')
def timeline(request):
  context = {
    'parent': 'pages',
    'segment': 'timeline'
  }
  return render(request, 'pages/pages/timeline.html', context)

@login_required(login_url='/accounts/login/')
def rtl_page(request):
  return render(request, 'pages/pages/rtl.html')

# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm

  def get_context_data(self, *args, **kwargs):
    context = super(UserLoginView, self).get_context_data(*args, **kwargs)
    context['segment'] = 'login_page'
    return context

#  def form_valid(self, form: AuthenticationForm) -> HttpResponse:
#    http_response = super().form_valid(form)
#    return http_response

class UserResetPasswordView(PasswordResetView):
  template_name = 'accounts/password-reset.html'
  form_class = UserPasswordResetForm

  def get_context_data(self, *args, **kwargs):
    context = super(UserResetPasswordView, self).get_context_data(*args, **kwargs)
    context['segment'] = 'password_reset_page'
    return context

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = {
    'parent': 'pages',
    'segment': 'register_page',
    'form': form
  }
  return render(request, 'accounts/register.html', context)

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password-reset-confirm.html'
  form_class = UserSetPasswordForm

  def get_context_data(self, *args, **kwargs):
    context = super(UserPasswordResetConfirmView, self).get_context_data(*args, **kwargs)
    context['segment'] = 'reset_confirm_page'
    return context

class UserChangePasswordView(PasswordChangeView):
  template_name = 'accounts/password-change.html'
  form_class = UserPasswordChangeForm

  def get_context_data(self, *args, **kwargs):
    context = super(UserChangePasswordView, self).get_context_data(*args, **kwargs)
    context['segment'] = 'password_change_page'
    return context
  

def template(request):
  return render(request, 'pages/template.html')