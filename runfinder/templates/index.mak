<%inherit file="base.mak"/>

<%block name="content">
    ${search_form.render() | n}
    <br>

    % if page and page.objects_list:
        % for event in page.objects_list:
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">${event['assetName']}</h3>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th class="col-md-4">Place</th>
                            <th class="col-md-2">Urls</th>
                            <th>Start date</th>
                        </tr>
                    </thead>
                    <tr>
                        <td>
                            ${event['place']['cityName']}, ${event['place']['countryName']}<br>
                            ${event['place']['placeName']}<br>
                            ${event['place']['addressLine1Txt']} ${event['place']['addressLine2Txt']}
                        </td>
                        <td>
                            % if event['homePageUrlAdr']:
                                <a href="${event['homePageUrlAdr']}" title="${event['assetName']}">homepage</a><br>
                            % endif
                            % if event['registrationUrlAdr']:
                                <a href="${event['registrationUrlAdr']}" title="${event['assetName']} registration">registration</a>
                            % endif
                        </td>
                        <td>
                            % if event['activityStartDate']:
                                ${' '.join(event['activityStartDate'].split('T'))}
                            % endif
                        </td>
                    </tr>
                </table>
            </div>

##            ${event['place']['geoPoint']}
##            ${event['assetImages']}

        % endfor

        % if page.pageno > 1 or page.has_next:
            <nav>
                <ul class="pagination">
                    % if page.pageno > 1:
                        <li><a href="${request.current_route_url()}&page=${page.pageno - 1}">&laquo; prev</a></li>
                    % endif
                    % if page.has_next:
                        <li><a href="${request.current_route_url()}&page=${page.pageno + 1}">&raquo; next</a></li>
                    % endif
                </ul>
            </nav>
        % endif

    % endif

</%block>
