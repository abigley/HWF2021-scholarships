"""Scholarships development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = b'Ym,\xbdf\xc8\x03>\xe8z\x9b\x02%\x0fQ\x04i\xd1R\x1c\x80\xa8\x8a\x83'
SESSION_COOKIE_NAME = 'login'
# File Upload to var/uploads/
SCHOLARSHIPS_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = SCHOLARSHIPS_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
DATABASE_FILENAME = SCHOLARSHIPS_ROOT/'var'/'scholarships.sqlite3'