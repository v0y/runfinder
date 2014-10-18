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
        <nav class="navbar navbar-default" role="navigation">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" href="/">Runfinder</a>
                </div>

                <ul class="nav navbar-nav">
                    <li><a href="/">Homepage</a></li>
                </ul>
            </div>
        </nav>

        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <%block name="content" />
                </div>
            </div>
        </div>

    </body>

</html>
