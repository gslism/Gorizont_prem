import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_bonustransfer_cancellation_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('technical_issue', 'Техническая проблема'), ('bonus_transfer_issue', 'Проблема с переводом бонусов'), ('profile_access', 'Проблема с доступом/профилем'), ('data_error', 'Ошибка в данных'), ('other', 'Другое')], max_length=50, verbose_name='Причина обращения')),
                ('description', models.TextField(verbose_name='Описание проблемы')),
                ('status', models.CharField(choices=[('new', 'Новое'), ('in_progress', 'В работе'), ('closed', 'Закрыто')], default='new', max_length=20, verbose_name='Статус')),
                ('admin_response', models.TextField(blank=True, default='', verbose_name='Решение/ответ администратора')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_requests', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('handled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handled_support_requests', to=settings.AUTH_USER_MODEL, verbose_name='Обработал администратор')),
            ],
            options={
                'verbose_name': 'Обращение в поддержку',
                'verbose_name_plural': 'Обращения в поддержку',
                'ordering': ['-created_at'],
            },
        ),
    ]
