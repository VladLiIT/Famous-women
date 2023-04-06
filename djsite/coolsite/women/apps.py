from django.apps import AppConfig


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Женщины мира'                            # Women заголовок переименовали в 'Женщины мира' в admin django  
