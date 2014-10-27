from active_com.api import SearchApiV2
from deform import Form, ValidationFailure
from pyramid.view import view_config

from .active_com_api_key import SEARCH_API_V2_KEY
from .forms import SearchSchema, search_at_least_one_validator


@view_config(route_name='index', renderer='templates/index.mak')
def index(request):
    search_form = Form(
        SearchSchema(validator=search_at_least_one_validator),
        buttons=('submit', ))

    response_data = {'search_form': search_form, 'data': {}}
    post = request.POST

    # if form was not sent, return
    if 'submit' not in post:
        return response_data

    # validate form, return if invalid
    controls = request.POST.items()
    try:
        data = search_form.validate(controls)
        response_data['data'] = data
    except ValidationFailure:
        return response_data

    # if we are here, form is valid. Get events!
    search_api = SearchApiV2(SEARCH_API_V2_KEY)
    response_data['events'] = search_api \
        .country(data.get('country')) \
        .city(data.get('city')) \
        .topic('running') \
        .get()

    print(response_data['events'])

    return response_data
