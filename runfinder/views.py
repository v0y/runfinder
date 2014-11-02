from active_com.api import SearchApiV2
from deform import Form, ValidationFailure
from pyramid.view import view_config

from .active_com_api_key import SEARCH_API_V2_KEY
from .forms import SearchSchema, search_at_least_one_validator


@view_config(route_name='index', renderer='templates/index.mak')
def index(request):
    search_form = Form(
        SearchSchema(validator=search_at_least_one_validator),
        buttons=('submit', ), method='GET')

    response_data = {'search_form': search_form, 'data': {}}
    get = request.GET

    # if form was not sent, return
    if 'submit' not in get:
        return response_data

    # validate form, return if invalid
    try:
        search_form.validate(get.items())
    except ValidationFailure:
        return response_data

    # if we are here, form is valid. Get events!
    response_data['page'] = Page(request)

    return response_data


class Page(object):
    """
    Page object for events
    """

    def __init__(self, request):
        self.request = request
        self.search_api = SearchApiV2(SEARCH_API_V2_KEY)

        self.pageno = request.GET.get('page', 1)
        try:
            self.pageno = int(self.pageno)
        except ValueError:
            self.pageno = 1


    @property
    def _base_query(self):
        return self.search_api \
            .country(self.request.POST.get('country')) \
            .city(self.request.POST.get('city')) \
            .topic('running') \
            .sort('date_asc') \
            .exclude_children(True)

    @property
    def objects_list(self):
        """
        :rtype: list
        :return: current page objects
        """
        return self._base_query.current_page(self.pageno).get()['results']

    @property
    def has_next(self):
        """
        :rtype: bool
        :return: True, if paginator has next page, otherwise
        """
        return bool(
            self._base_query.current_page(self.pageno + 1).get()['results'])
