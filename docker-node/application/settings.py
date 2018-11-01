# ============================================================================
# Celery config
# ============================================================================
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'