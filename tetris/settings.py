import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings = {
    'debug': bool(os.environ.get('DEBUG', False)),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'templates'),
}
