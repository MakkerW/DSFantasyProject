from GreenGroceries import app


@app.template_filter('format_data')
def format_data(string):
    if isinstance(string, str):
        return string.replace('_', ' ').capitalize()
    else :
        return string

