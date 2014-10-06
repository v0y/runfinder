<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <title>Runfinder - find your run</title>

        % for url in webassets(request, 'bootstrap/dist/css/bootstrap.min.css'):
            <link href="${url}" rel="stylesheet" type="text/css">
        % endfor

        % for url in webassets(request, \
                'bootstrap/dist/js/bootstrap.min.js', 'jquery/dist/jquery.min.js'):
            <script src="${url}"></script>
        % endfor
    </head>

    <body>
        <%block name="content" />
    </body>

</html>
