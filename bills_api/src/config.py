# /src/config.py
import os

class Config(object):
    """Parent configuration class."""
    CSRF_ENABLED = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Development(Config):
    """Configurations for the development environment"""
    DEBUG = True
    TESTING = False

class Testing(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'

class Staging(Config):
    """Configurations for Staging"""
    DEBUG = True

class Production(Config):
    """Production environment configuration"""
    DEBUG = False
    TESTING = False





app_config = {
    'development': Development,
    'production': Production,
}
