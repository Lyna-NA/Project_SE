from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as authViews


urlpatterns = [
    # auth app 
    path('signup/' ,views.signup, name="signup"),
    path('signin/' ,views.signin, name="signin"),
    path('logout/' ,views.userLogout, name="logout"),
    path('setInfo/' ,views.setInfo, name="setInfo"),
    path('resetInfo/<str:username>' ,views.resetInfo, name="resetInfo"),

     path('reset_password/' ,authViews.PasswordResetView.as_view(template_name= "registration/auth/password_reset.html") , name="reset_password"),
     path('reset_password_sent/' ,authViews.PasswordResetDoneView.as_view(template_name= "registration/auth/password_reset_sent.html") , name="password_reset_done"),
     path('reset/<uidb64>/<token>/' ,authViews.PasswordResetConfirmView.as_view(template_name= "registration/auth/password_reset_form.html") , name="password_reset_confirm"),
     path('reset_password_complete/' ,authViews.PasswordResetCompleteView.as_view(template_name= "registration/auth/password_reset_done.html") , name="password_reset_complete"),

]
urlpatterns +=static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)

 