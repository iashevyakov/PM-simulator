# Generated by Django 2.1.7 on 2019-03-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bottom_line', models.FloatField()),
                ('upper_line', models.FloatField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_options', to='sim.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='OptionParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_to_add', models.FloatField()),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_params', to='sim.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='optionparam',
            name='param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='param_options', to='sim.Param'),
        ),
        migrations.AddField(
            model_name='jump',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Option'),
        ),
        migrations.AddField(
            model_name='jump',
            name='question_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='sim.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='optionparam',
            unique_together={('option', 'param')},
        ),
        migrations.AlterUniqueTogether(
            name='jump',
            unique_together={('option', 'question_to')},
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('question', 'text')},
        ),
    ]
