## Dataset Request and Issue Reporting Application for DjangoCMS-CKAN integration

Plugin and Admin application for managing requests for datasets and issue reporting.

For dataset requests, application will poll CKAN for organizations and will present options to user in form of drop down.

For issue reporting, application will poll CKAN for dataset list and will present to users in a typeahead selector.

Application currently utilizes Trello API to automatically sync app-side changes with API. Coming soon will be bi-directional
updates via Trello webhooks and application API. 

To activate trello integration add the following to `settings.py`

- `TRELLO_TOKEN = values.Value(environ_name='TRELLO_TOKEN')`
- `TRELLO_KEY = values.Value(environ_name='TRELLO_KEY')`
- `TRELLO_SECRET = values.Value(environ_name='TRELLO_SECRET')`
- `TRELLO_REQUEST_BOARD = values.Value(environ_name='TRELLO_BOARD')`

and then set the appropriate environmental variables.

If you are using Apache `SetEnv`, make sure to add apprpriate calls in `wsgi.py` to grab the env variables
and pass them through the application environment.

This is one approach that will work:

```
def application(environ, start_response):
    os.environ['DJANGO_DATABASE_URL'] = environ.get('DJANGO_DATABASE_URL','')
    os.environ['DJANGO_CONFIGURATION'] = environ.get('DJANGO_CONFIGURATION','')
    os.environ.setdefault('DJANGO_SECRET_KEY', environ.get('DJANGO_SECRET_KEY',''))
    os.environ['DJANGO_TRELLO_KEY'] = environ.get('DJANGO_TRELLO_KEY','')
    os.environ['DJANGO_TRELLO_SECRET'] = environ.get('DJANGO_TRELLO_SECRET','')
    os.environ['DJANGO_TRELLO_TOKEN'] = environ.get('DJANGO_TRELLO_TOKEN','')
    return _application(environ, start_response)
```
