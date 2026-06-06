from django.db import migrations
import os
import json

def load_my_projects(apps, schema_editor):
    Project = apps.get_model('core', 'Project')
    
    # Path to your clean UTF-8 data dump file
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    fixture_path = os.path.join(base_dir, 'datadump.json')
    
    if os.path.exists(fixture_path):
        with open(fixture_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            for item in data:
                fields = item.get('fields', {})
                
                if item.get('model') == 'core.project':
                    Project.objects.get_or_create(
                        id=item.get('pk'),
                        defaults={
                            'title': fields.get('title'),
                            'thumbnail': fields.get('thumbnail'),
                            'description': fields.get('description'),
                            'problem_statement': fields.get('problem_statement'),
                            'solution_details': fields.get('solution_details'),
                            'result_roi': fields.get('result_roi'),
                            'github_link': fields.get('github_link'),
                        }
                    )

class Migration(migrations.Migration):

    dependencies = [
        # Linked directly to your actual 0005 file
        ('core', '0005_project'), 
    ]

    operations = [
        migrations.RunPython(load_my_projects),
    ]