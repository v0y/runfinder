<%inherit file="base.mak"/>

<%block name="content">
    ${search_form.render() | n}
    <br><br>
    ${data}
</%block>
