<%inherit file="base.mak"/>

<%block name="content">
    ${search_form.render() | n}
    <br><br>

    % for event in events['results']:

        ${event}<br>
        <hr>

    % endfor

</%block>
