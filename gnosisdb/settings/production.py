from gnosisdb.settings.base import *
from gnosisdb.chainevents.abis import abi_file_path, load_json_file
import os

CELERY_SEND_TASK_ERROR_EMAILS = True

SECRET_KEY = os.environ['SECRET_KEY']

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'

# ------------------------------------------------------------------------------
# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_HOST=os.environ['EMAIL_HOST']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = os.environ['EMAIL_SUBJECT_PREFIX']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_BACKEND = 'email_log.backends.EmailBackend'
EMAIL_LOG_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMINS = (
    ('Giacomo', 'giacomo.licari@gnosis.pm'),
    ('Denis', 'denis@gnosis.pm'),
    ('Rami', 'rami.khalil@gnosis.pm'),
    ('Stefa', 'stefan@gnosis.pm'),
)

# ------------------------------------------------------------------------------
# ETHEREUM
# ------------------------------------------------------------------------------
ETHEREUM_NODE_HOST = os.environ['ETHEREUM_NODE_HOST']
ETHEREUM_NODE_PORT = os.environ['ETHEREUM_NODE_PORT']
ETHEREUM_NODE_SSL = os.environ['ETHEREUM_NODE_SSL']

# ------------------------------------------------------------------------------
# IPFS
# ------------------------------------------------------------------------------
IPFS_HOST = os.environ['IPFS_HOST']
IPFS_PORT = os.environ['IPFS_PORT']

# ------------------------------------------------------------------------------
# RABBIT MQ
# ------------------------------------------------------------------------------
RABBIT_HOSTNAME = os.environ['RABBIT_HOSTNAME']
RABBIT_USER = os.environ['RABBIT_USER']
RABBIT_PASSWORD = os.environ['RABBIT_PASSWORD']
RABBIT_PORT = os.environ['RABBIT_PORT']
BROKER_URL = 'amqp://{user}:{password}@{hostname}:{port}'.format(
    user=RABBIT_USER,
    password=RABBIT_PASSWORD,
    hostname=RABBIT_HOSTNAME,
    port=RABBIT_PORT
)

# ------------------------------------------------------------------------------
# GNOSIS ETHEREUM CONTRACTS
# ------------------------------------------------------------------------------
ETH_EVENTS = [
    {
        'ADDRESSES': [os.environ['CENTRALIZED_ORACLE_FACTORY']],
        'ADDRESSES_GETTER': '',
        'EVENT_ABI': load_json_file(abi_file_path('CentralizedOracleFactory.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.CentralizedOracleFactoryReceiver',
        'NAME': 'centralizedOracleFactory',
        'PUBLISH': True,
    },
    {
        'ADDRESSES': [os.environ['ULTIMATE_ORACLE_FACTORY']],
        'ADDRESSES_GETTER': '',
        'EVENT_ABI': load_json_file(abi_file_path('UltimateOracleFactory.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.UltimateOracleFactoryReceiver',
        'NAME': 'ultimateOracleFactory',
        'PUBLISH': True,
    },
    {
        'ADDRESSES': [os.environ['EVENT_FACTORY']],
        'ADDRESSES_GETTER': '',
        'EVENT_ABI': load_json_file(abi_file_path('EventFactory.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.EventFactoryReceiver',
        'NAME': 'eventFactory',
        'PUBLISH': True,
    },
    {
        'ADDRESSES': [os.environ['MARKET_FACTORY']],
        'ADDRESSES_GETTER': '',
        'EVENT_ABI': load_json_file(abi_file_path('StandardMarketFactory.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.MarketFactoryReceiver',
        'NAME': 'standardMarketFactory',
        'PUBLISH': True,
        'PUBLISH_UNDER': 'marketFactories'
    },
    {
        'ADDRESSES': [],
        'ADDRESSES_GETTER': 'chainevents.address_getters.MarketAddressGetter',
        'EVENT_ABI': load_json_file(abi_file_path('StandardMarket.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.MarketInstanceReceiver',
        'NAME': 'Standard Markets Buy/Sell/Short Receiver'
    },
    {
        'ADDRESSES_GETTER': 'chainevents.address_getters.EventAddressGetter',
        'EVENT_ABI': load_json_file(abi_file_path('AbstractEvent.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.EventInstanceReceiver',
        'NAME': 'Event Instances'
    },
    {
        'ADDRESSES_GETTER': 'chainevents.address_getters.OutcomeTokenGetter',
        'EVENT_ABI': load_json_file(abi_file_path('OutcomeToken.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.OutcomeTokenInstanceReceiver',
        'NAME': 'Outcome Token Instances'
    },
    {
        'ADDRESSES_GETTER': 'chainevents.address_getters.CentralizedOracleGetter',
        'EVENT_ABI': load_json_file(abi_file_path('CentralizedOracle.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.CentralizedOracleInstanceReceiver',
        'NAME': 'Centralized Oracle Instances'
    },
    {
        'ADDRESSES_GETTER': 'chainevents.address_getters.UltimateOracleGetter',
        'EVENT_ABI': load_json_file(abi_file_path('UltimateOracle.json')),
        'EVENT_DATA_RECEIVER': 'chainevents.event_receivers.UltimateOracleInstanceReceiver',
        'NAME': 'Ultimate Oracle Instances'
    },
]

# ------------------------------------------------------------------------------
# GNOSIS ETHEREUM CONTRACTS
# ------------------------------------------------------------------------------
DATABASES = {
    'default': os.environ['DATABASE_URL'],
    'alternative': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}