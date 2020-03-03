urls_docs = """example:
from utils.urls import *
urlpatterns = [
    add_absolute_path('need_url/', your_view_func, methods=['GET']),  # Creates a URL to this view_func
    # Creates URls from application.urls.urlpatterns starting with the URL given.
    add_relative_path('/start_url/', include('application.urls'),
    get_relative_path('need_url/', your_view_func, methods=['GET']),  # Return url, view_func, methods
]
"""

manage_docs = """Add new command:
@manage.manager.command
def command(params):
    pass

@manage.manager.options('-p', '--params', help='Hint')
def option_command(params):
    if params:
        pass
    else:
        pass
"""
