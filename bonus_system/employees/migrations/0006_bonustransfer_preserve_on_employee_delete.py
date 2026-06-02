# -*- coding: utf-8 -*-
from django.db import migrations, models
import django.db.models.deletion


def _full_name(emp):
    return f"{emp.last_name} {emp.first_name} {emp.middle_name or ''}".strip()


def forwards_fill_names(apps, schema_editor):
    BonusTransfer = apps.get_model('employees', 'BonusTransfer')
    Employee = apps.get_model('employees', 'Employee')
    for t in BonusTransfer.objects.all():
        upd = []
        if t.from_employee_id:
            try:
                f = Employee.objects.get(pk=t.from_employee_id)
                t.from_display_name = _full_name(f)
                upd.append('from_display_name')
            except Employee.DoesNotExist:
                pass
        if t.to_employee_id:
            try:
                to = Employee.objects.get(pk=t.to_employee_id)
                t.to_display_name = _full_name(to)
                upd.append('to_display_name')
            except Employee.DoesNotExist:
                pass
        if upd:
            t.save(update_fields=upd)


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_systemsettings_employee_participates_in_bonus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonustransfer',
            name='from_display_name',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='От кого (ФИО, архив)'),
        ),
        migrations.AddField(
            model_name='bonustransfer',
            name='to_display_name',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Кому (ФИО, архив)'),
        ),
        migrations.RunPython(forwards_fill_names, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='bonustransfer',
            name='from_employee',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='sent_transfers',
                to='employees.employee',
                verbose_name='От кого',
            ),
        ),
        migrations.AlterField(
            model_name='bonustransfer',
            name='to_employee',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='received_transfers',
                to='employees.employee',
                verbose_name='Кому',
            ),
        ),
    ]
