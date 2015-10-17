# Development environment settings file


# Database connection to the development DB
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_analytics',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'CONN_MAX_AGE': 300,
    },
    'housing_analytics': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_analytics',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 300,
    },
    'housing_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'CONN_MAX_AGE': 300,
    },
    'housing_pg_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_pg_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433'
    },
    'housing_np_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_np_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'CONN_MAX_AGE': 300,
    },
    'housing_subscription_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_subscription_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433'
    },
    'housing_ra_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_ra_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
    'email_service_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'email_service_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433'
    },
    'housing_regions_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'housing_regions_production',
        'USER': 'housing_su',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'OPTIONS': {
            'options': '-c search_path=public,postgis'
        },
        'CONN_MAX_AGE': 300,
    },
    'locality_expert_production': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'locality_expert_production',
        'USER': 'housing',
        'PASSWORD': 'housing',
        'HOST': '127.0.0.1',
        'PORT': '5434',
        'CONN_MAX_AGE': 300,
    },
}

DEBUG = True

TEMPLATE_DEBUG = True

# HOUSING
MAIL_HOST = 'data.staging.housing.com'
MAIL_MANDRILL_HOST = 'mail.internal.staging.housing.com'
MAIL_MANDRILL_KEY = 'lol'
SMS_HOST = 'sms.internal.staging.housing.com:81'
HOUSING_HOST = 'internal.staging.housing.com'
REDIS_HOST = 'dsl-redis.internal.staging.housing.com'
REDIS_PORT = 6379

# Below keys must be changed for production - Keys with A
HOUSING_API_KEY = 'abcdefg'
HOUSING_SHARED_SECRET_KEY = 'lol'

# impressions
REDIS_DB_IMPRESSIONS = 0
REDIS_DEACTIVATION_QUEUE = 'Deactivation-queue'

# engagement
REDIS_DB_ENGAGEMENT = 1

REDIS_DB = {
    'flats_db': 0,
    'users_db': 1
}

MONGO_URI = 'mongodb://10.1.10.14:27017/'

MONGO_DB = {
    'users_db': 'dsl_redis',
    'users_coll': 'users_data',
    'guid_coll': 'global_uid',
}

IS_SLAVE = False

# google_places_data
REDIRECT_URL = "data-staging.housing.com/places_data"
PERIPHERAL_URL = "http://regions.internal.staging.housing.com/api/v1/establishment/bulk_upsert"
PERIPHERAL_CRUD_URL = "http://regions.internal.staging.housing.com/admin/establishment"
LOGIN_URL = "http://accounts.internal.staging.housing.com"
HOUSINGCOM_HOST = "https://housing.com"

# price_trends
PRICE_TRENDS_REDIRECT_URL = 'http://data-staging.housing.com/price_trends'

# ACL
ACL_HOST = 'http://acl.internal.staging.housing.com'
DSL_ACL_SERVICE = 'HousingDSL'
PRICE_TRENDS_ACL_CONTROLLER = 'PriceTrendsPanel'

# rabbitmq credential
RABBITMQ_URI = 'amqp://guest:guest@localhost:5672//'

# regions
REGIONS_POLYGON_URL = 'http://regions.internal.staging.housing.com/api/v1/polygon/reverse_geocode'

# Backend Services
NEW_PROJECTS_API = 'https://newprojects.housing.com/api/v1/new-projects/'
# https://newprojects.housing.com/api/v1/new-projects/256/webapp

RENT_API = 'https://housing.com/api/v2/rent/'
# https://housing.com/api/v2/rent/194625
# https://housing.com/api/v2/rent/filter?latitude=28.4594965&longitude=77.02663830000006&radius=2000&key=lol

BUY_API = 'https://housing.com/api/v2/buy/'
# https://housing.com/api/v2/buy/108685

PG_API = 'https://pg.housing.com/api/v2/pg/'
# https://pg.housing.com/api/v2/pg/6067

REGIONS_ESTABLISHMENT_API = 'https://regions.housing.com/api/v1/establishment/'
# https://regions.housing.com/api/v1/establishment/filter?f=eyJsYXQiOjE5LjExNjgzOSwibG5nIjo3Mi45MDQ2NjQwMDAwMDAwMywibWF4X2NvdW50Ijo1LCJyYWRpdXMiOjIwMDAsInR5cGUiOiJob3NwaXRhbCJ9

# https://regions.housing.com//api/v1/establishment/aggregate?lat=28.4575&lng=77.023973

RAILWAYS_API = 'https://housing.com/api/v1/railways'
# https://housing.com/api/v1/railways?lat_lng=28.4575,77.023973&radius=20000&key=lol

AIRPORTS_API = 'https://housing.com/api/v1/airports'
# https://housing.com/api/v1/airports?city=gurgaon

# Routing URL
ROUTING_URL = 'http://78.46.97.15:5000/viaroute?loc={lat1},{lng1}&loc={lat2},{lng2}&z=12&instructions=true'

# Analytics Mongo URI
ANALYTICS_MONGO_URI = 'mongodb://dsl_read:dsl@localhost:3338/analytics'

# Internal housing host
INTERNAL_HOUSING_HOST = 'http://internal.housing.com'

DATA_HOST = 'https://data.housing.com'

URL_SHORTENER_HOST = 'http://url-shortener.internal.housing.com/'
SHORTENED_URL_DNS = 'http://hsng.co'

NOTIFICATION_HOST = 'http://notification.internal.staging.housing.com'

MONGO_URI_DICT = {
    'analytics': 'mongodb://dsl_read:dsl@localhost:3338/analytics',
    'dsl_redis': 'mongodb://dsl_read:dsl@localhost:3338/dsl_redis',
    'housingcrm': 'mongodb://mongo.internal.housing.com/housingcrm'
}

MONGO_DATABASES = {
    'analytics': 'analytics',
    'dsl_redis': 'dsl_redis',
}

MONGO_COLLECTIONS = {
    'dedicated_page': 'Dedicated_Page',
    'filters_new_projects': 'Filters_new_projects',
    'impressions': 'Impressions',
    'filters_buy': 'Filters_buy',
    'filters_rent': 'Filters_rent',
    'filters_pg': 'Filters_pg',
    'filters_serviced_apartments': 'Filters_serviced_apartments',
    'infowindow_buy': 'Infowindow_buy',
    'infowindow_rent': 'Infowindow_rent',
    'form': 'Form',
    'details_page': 'details_page',
    'conversion': 'conversion',
    'interactionSummary': 'interactionSummary',
    'search': 'search',
}

BUY_HOST = 'http://sahilt.housing.com:3069'
REGIONS_HOST = 'http://regions.internal.housing.com'
LOGIN_HOST = 'http://login.internal.housing.com'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'SOCKET_TIMEOUT': 5,
            'SOCKET_CONNECT_TIMEOUT': 5,
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                # By default max_connections is 50, Value can be changed if
                # required
                'timeout': 0.05,
            },
        },
    },
}

ES = {
    'uri': 'http://10.1.11.7:9200/',
    'rent_flats_index': 'rent_flats',
    'search': '_search'
}
