from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_bonustransfer_preserve_on_employee_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonustransfer',
            name='cancellation_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Причина отмены'),
        ),
    ]
