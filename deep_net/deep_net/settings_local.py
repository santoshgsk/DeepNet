import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'housing_analytics',
    #     'USER': 'housing',
    #     'PASSWORD': 'housing',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    #     'OPTIONS': {
    #         'options': '-c search_path=public,postgis'
    #     }
    # },
    #  'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'gskdb2',
    #     'USER': 'santoshgsk',
    #     'PASSWORD': 'dev',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    #     # 'NAME': 'housing_analytics',
    #     # 'USER': 'dsl_readonly',
    #     # 'PASSWORD': 'dsl',
    #     # 'HOST': '127.0.0.1',
    #     # 'PORT': '5434',
    #     'OPTIONS': {
    #         'options': '-c search_path=public,postgis'
    #     }
    # },
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'housing_analytics',
    #     'USER': 'housing',
    #     'PASSWORD': 'housing',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5434',
    #     'CONN_MAX_AGE': 300,
    #     'OPTIONS': {
    #         'options': '-c search_path=public,postgis'
    #     }
    # },
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gskdb2',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        }
    },
    'housing_analytics': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_analytics',
        'USER': 'dsl_readonly',
        'PASSWORD': 'dsl',
        'HOST': '127.0.0.1',
        'PORT': '5434',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        }
    },
    'housing_regions_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_regions_production',
        'USER': 'housing_su',
        'PASSWORD': 'housing',
        'HOST': '10.1.1.224',
        'PORT': '5433',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        },
    },
    'housing_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        },
    },
    'housing_np_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_np_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        },
    }
}
