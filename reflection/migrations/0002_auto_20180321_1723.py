# Generated by Django 2.0.1 on 2018-03-21 07:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reflection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reflection',
            name='team1_grade',
            field=models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AddField(
            model_name='reflection',
            name='team1_name',
            field=models.CharField(default=1, help_text='Write your team member name', max_length=100, verbose_name='team1_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='team1_reflection',
            field=models.TextField(default=1, help_text='Evaluation of contribution and performance ', verbose_name='team1_reflection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='team2_grade',
            field=models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AddField(
            model_name='reflection',
            name='team2_name',
            field=models.CharField(default=1, help_text='Write your team member name', max_length=100, verbose_name='team2_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='team2_reflection',
            field=models.TextField(default=1, help_text='Evaluation of contribution and performance ', verbose_name='team2_reflection'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='team3_grade',
            field=models.PositiveIntegerField(default=1, help_text='Grade between 1 and 7', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
        migrations.AddField(
            model_name='reflection',
            name='team3_name',
            field=models.CharField(default=1, help_text='Write your team member name', max_length=100, verbose_name='team3_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reflection',
            name='team3_reflection',
            field=models.TextField(default=1, help_text='Evaluation of contribution and performance ', verbose_name='team3_reflection'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reflection',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]