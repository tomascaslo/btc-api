# coding: utf-8

from tastypie.resources import ModelResource
from tastypie.validation import CleanedDataFormValidation

from django.forms.models import ModelChoiceField
from django.views.decorators.csrf import csrf_exempt


class ModelCleanedDataFormValidation(CleanedDataFormValidation):
    """
    Clase para validar modelos, esto evita que los FORMS marquen errores con
    los foreign key que llegan como resource_uris
    """
    def uri_to_pk(self, uri):
        """
        Convierte las uris a llaves primarias
        """
        if uri is None:
            return None

        if isinstance(uri, int) or isinstance(uri, long):
            return uri

        # convert everything to lists
        multiple = not isinstance(uri, basestring)
        uris = uri if multiple else [uri]

        # handle all passed URIs
        converted = []
        for one_uri in uris:
            try:
                # hopefully /api/v1/<resource_name>/<pk>/
                converted.append(int(one_uri.split('/')[-2]))
            except (IndexError, ValueError):
                raise ValueError(
                    "URI %s could not be converted to PK integer." % one_uri)

        # convert back to original format
        return converted if multiple else converted[0]

    def form_args(self, bundle):
        """
        Todos los fields de una forma son procesados y los PK son convertidos
        de URIS a PK
        """
        kwargs = super(ModelCleanedDataFormValidation, self).form_args(bundle)

        relation_fields = [name for name, field in
                           self.form_class.base_fields.items()
                           if issubclass(field.__class__, ModelChoiceField)]

        for field in relation_fields:
            if field in kwargs['data']:
                kwargs['data'][field] = self.uri_to_pk(kwargs['data'][field])

        # if bundle.request.user:
        #     kwargs['current_user'] = bundle.request.user

        return kwargs


class ModelResourceCustom(ModelResource):
    """
    Metodo sobreescrito del Model Resource que se usa para declarar los
    recursos de tastypie.
    """
    def wrap_view(self, view):
        @csrf_exempt
        def wrapper(request, *args, **kwargs):
            """
            Agregar que tastypie use csrf
            """
            request.META["CSRF_COOKIE_USED"] = True
            wrapped_view = super(ModelResourceCustom, self).wrap_view(view)
            return wrapped_view(request, *args, **kwargs)
        return wrapper