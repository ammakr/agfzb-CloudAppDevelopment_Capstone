from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='', view=views.get_dealerships, name='index'),
    # path for about view
    path(route='contact/', view=views.contact, name='contact'),
    path(route='about/', view=views.about, name='contact'),
    path('signup/', view=views.registration_request),
    path('', include('django.contrib.auth.urls'))

    # path for contact us view

    # path for registration

    # path for login

    # path for logout


    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)