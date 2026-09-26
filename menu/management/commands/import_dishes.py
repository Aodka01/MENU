from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from menu.models import Dish
import csv
import os


class Command(BaseCommand):
    help = 'Import dishes from a CSV file. CSV columns: name,description,price,image_filename,available'

    def add_arguments(self, parser):
        parser.add_argument('csvpath', type=str, help='Path to CSV file')
        parser.add_argument('--media-dir', type=str, default=None, help='Directory where images are located (defaults to MEDIA_ROOT/dishes)')

    def handle(self, *args, **options):
        csvpath = options['csvpath']
        media_dir = options['media_dir'] or os.path.join(settings.MEDIA_ROOT, 'dishes')

        if not os.path.exists(csvpath):
            self.stderr.write(self.style.ERROR(f'CSV file not found: {csvpath}'))
            return

        created = 0
        with open(csvpath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('name')
                description = row.get('description', '')
                price = row.get('price') or '0'
                image_filename = row.get('image_filename')
                available = row.get('available', 'True').lower() in ('1', 'true', 'yes')

                dish, _ = Dish.objects.get_or_create(name=name, defaults={'description': description, 'price': price, 'available': available})
                if image_filename:
                    img_path = os.path.join(media_dir, image_filename)
                    if os.path.exists(img_path):
                        with open(img_path, 'rb') as imgf:
                            dish.image.save(image_filename, File(imgf), save=True)
                else:
                    dish.description = description
                    dish.price = price
                    dish.available = available
                    dish.save()
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Imported/updated {created} dishes'))
