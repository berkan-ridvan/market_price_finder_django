from django.apps import AppConfig


class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'


class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.models.signals import post_migrate

        def create_admin(sender, **kwargs):
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin12345'
                )
                print("✅ Admin user created")

        post_migrate.connect(create_admin, sender=self)
