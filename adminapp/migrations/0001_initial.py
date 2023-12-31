# Generated by Django 4.2.3 on 2023-09-17 09:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('luminarapi', '0002_alter_course_description_alter_course_thumbnail'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('faculty', 'Faculty')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomAdmin',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('adminapp.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(max_length=50)),
                ('parent_no', models.CharField(max_length=13)),
                ('phone', models.CharField(max_length=13)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('selected_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarapi.course')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('adminapp.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=100)),
                ('batch_code', models.CharField(max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('coursename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crs', to='luminarapi.course')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('selected_course', models.CharField(max_length=50)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.batch')),
                ('stud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student')),
            ],
        ),
    ]
