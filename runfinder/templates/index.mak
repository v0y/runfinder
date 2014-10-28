<%inherit file="base.mak"/>

<%block name="content">
    ${search_form.render() | n}
    <br>

    % if events:
        % for event in events['results']:
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
    % endif

</%block>
