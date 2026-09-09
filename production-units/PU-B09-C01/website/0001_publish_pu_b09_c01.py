# Adapt model and dependency names to the current website baseline before applying.
from django.db import migrations

def publish(apps, schema_editor):
    Unit=apps.get_model('catalog','ProductionUnit')
    Unit.objects.update_or_create(code='PU-B09-C01',defaults={'title':'AI Strategy and Transformation','slug':'ai-strategy-and-transformation'})
class Migration(migrations.Migration):
    dependencies=[('catalog','REPLACE_WITH_CURRENT_MIGRATION')]
    operations=[migrations.RunPython(publish,migrations.RunPython.noop)]
