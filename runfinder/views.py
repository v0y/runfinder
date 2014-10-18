from deform import Form, ValidationFailure
from pyramid.view import view_config

from .forms import SearchSchema


@view_config(route_name='home', renderer='templates/index.mak')
def my_view(request):
    search_form = Form(SearchSchema(), buttons=('submit', ))

    data = {}
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            data = search_form.validate(controls)
        except ValidationFailure:
            pass

    return {
        'search_form': search_form,
        'data': data
    }
