import environs


env = environs.Env()
env.read_env('.env')


API_VERSION = env('API_VERSION')

DATABASE_CONFIG = {
    'connections': {
        'default': f'postgres://{env("DB_USER")}:{env("DB_PASSWORD")}@localhost:5432/{env("DB_NAME")}?application_name={env("DB_LICATION_NAME")}'
    },
    'apps': {
        'models': {
            'models': [
                'aerich.models',
            ],
            'default_connection': 'default',
        },
    },
}

