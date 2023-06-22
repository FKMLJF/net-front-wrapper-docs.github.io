## conf.py
def setup(app):
   app.add_css_file("css/style.css")

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/style.css',
]
