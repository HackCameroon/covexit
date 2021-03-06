# Generated by Django 2.2.12 on 2020-04-16 19:24

from django.db import migrations
from oscar.apps.catalogue.categories import create_from_breadcrumbs


def forwards_func(apps, schema_editor):
    categories = [
        'Haushalt, Garten, Tier & Baumarkt > Küchen- & Haushaltsgeräte',
        'Haushalt, Garten, Tier & Baumarkt > Kochen & Essen',
        'Haushalt, Garten, Tier & Baumarkt > Aufbewahren & Ordnen',
        'Haushalt, Garten, Tier & Baumarkt > Möbel & Wohnaccessoires',
        'Haushalt, Garten, Tier & Baumarkt > Heimtextilien',
        'Haushalt, Garten, Tier & Baumarkt > Beleuchtung',
        'Haushalt, Garten, Tier & Baumarkt > Sonstige',

        'Blumen',

        'Beauty & Drogerie & Lebensmittel > Damen',
        'Beauty & Drogerie & Lebensmittel > Herren',
        'Beauty & Drogerie & Lebensmittel > Baby',
        'Beauty & Drogerie & Lebensmittel > Sonstige',
        'Beauty & Drogerie & Lebensmittel > Lebensmittel',

        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Accessoires',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Tops, T-Shirts & Blusen',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Kleider',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Streetwear',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Bademode',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Jacken, Mäntel & Westen',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Sportbekleidung',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Socken & Strümpfe',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Unterwäsche',
        'Kleidung, Schuhe, Schmuck > Damen > Bekleidung > Pullover & Strickjacken',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Sneaker & Sportschuhe',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Stiefel',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Sandalen & Slides',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Flache Schuhe',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Hausschuhe',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Pumps',
        'Kleidung, Schuhe, Schmuck > Damen > Schuhe > Arbeits- & Berufsschuhe',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Zubehör',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Umhängetaschen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Clutches',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Handtaschen & Schultertaschen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Henkeltaschen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Rucksäcke',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Schultaschen, Federmäppchen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Sporttaschen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Einkaufskörbe & -taschen',
        'Kleidung, Schuhe, Schmuck > Damen > Taschen > Business- & Laptop-Taschen',
        'Kleidung, Schuhe, Schmuck > Damen > Uhren',
        'Kleidung, Schuhe, Schmuck > Damen > Schmuck',
        'Kleidung, Schuhe, Schmuck > Damen > Gepäck > Koffer',
        'Kleidung, Schuhe, Schmuck > Damen > Gepäck > Reisetaschen',
        'Kleidung, Schuhe, Schmuck > Damen > Gepäck > Zubehör',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Accessoires',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Tops, T-Shirts & Hedem',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Streetwear',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Bademode',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Jacken, Mäntel & Westen',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Sportbekleidung',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Socken & Strümpfe',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Unterwäsche',
        'Kleidung, Schuhe, Schmuck > Herren > Bekleidung > Pullover & Strickjacken',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Sneaker & Sportschuhe',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Stiefel',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Sandalen & Slides',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Flache Schuhe',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Hausschuhe',
        'Kleidung, Schuhe, Schmuck > Herren > Schuhe > Arbeits- & Berufsschuhe',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Zubehör',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Umhängetaschen',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Clutches',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Handtaschen & Schultertaschen',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Rucksäcke',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Schultaschen, Federmäppchen',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Sporttaschen',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Einkaufskörbe & -taschen',
        'Kleidung, Schuhe, Schmuck > Herren > Taschen > Business- & Laptop-Taschen',
        'Kleidung, Schuhe, Schmuck > Herren > Uhren',
        'Kleidung, Schuhe, Schmuck > Herren > Schmuck',
        'Kleidung, Schuhe, Schmuck > Herren > Gepäck > Koffer',
        'Kleidung, Schuhe, Schmuck > Herren > Gepäck > Reisetaschen',
        'Kleidung, Schuhe, Schmuck > Herren > Gepäck > Zubehör',
        'Kleidung, Schuhe, Schmuck > Mädchen > Accessoires',
        'Kleidung, Schuhe, Schmuck > Mädchen > Hosen',
        'Kleidung, Schuhe, Schmuck > Mädchen > Kleider',
        'Kleidung, Schuhe, Schmuck > Mädchen > Tops & Shirts',
        'Kleidung, Schuhe, Schmuck > Mädchen > Jacken & Mäntel',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Sneaker & Sportschuhe',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Stiefel',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Sandalen & Slides',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Flache Schuhe',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Hausschuhe',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schuhe > Pumps',
        'Kleidung, Schuhe, Schmuck > Mädchen > Schmuck',
        'Kleidung, Schuhe, Schmuck > Mädchen > Uhren',
        'Kleidung, Schuhe, Schmuck > Jungen > Accessoires',
        'Kleidung, Schuhe, Schmuck > Jungen > Hosen',
        'Kleidung, Schuhe, Schmuck > Jungen > Shirts',
        'Kleidung, Schuhe, Schmuck > Jungen > Pullover & Stickjacken',
        'Kleidung, Schuhe, Schmuck > Jungen > Jacken & Mäntel',
        'Kleidung, Schuhe, Schmuck > Jungen > Schuhe > Sneaker & Sportschuhe',
        'Kleidung, Schuhe, Schmuck > Jungen > Schuhe > Stiefel',
        'Kleidung, Schuhe, Schmuck > Jungen > Schuhe > Sandalen & Slides',
        'Kleidung, Schuhe, Schmuck > Jungen > Schuhe > Flache Schuhe',
        'Kleidung, Schuhe, Schmuck > Jungen > Schuhe > Hausschuhe',
        'Kleidung, Schuhe, Schmuck > Jungen > Schmuck',
        'Kleidung, Schuhe, Schmuck > Jungen > Uhren',
        'Kleidung, Schuhe, Schmuck > Babies',

        'Bücher & Musik > Bücher > Kinder & Jugend',
        'Bücher & Musik > Bücher > Fachliteratur & Lernen',
        'Bücher & Musik > Bücher > Ratgeber & Freizeit',
        'Bücher & Musik > Bücher > Sachbücher',
        'Bücher & Musik > Bücher > Fremdsprachige Bücher',
        'Bücher & Musik > Bücher > Sonstige',
        'Bücher & Musik > Musik',

        'Büro & IT > Elektronik & Foto',
        'Büro & IT > Computer & Büro',

        'Spielzeug & Baby > Spielzeug',
        'Spielzeug & Baby > Baby',
        'Spielzeug & Baby > Babybekleidung & Babyschuhe',

        'Kunst',

        'Sport & Freizeit > Camping & Outdoor',
        'Sport & Freizeit > Fitness',
        'Sport & Freizeit > Fußball',
        'Sport & Freizeit > Radsport',
        'Sport & Freizeit > Running',
        'Sport & Freizeit > Sportelektronik',

        'Sonstiges',
    ]
    for breadcrumbs in categories:
        create_from_breadcrumbs(breadcrumbs)


def reverse_func(apps, schema_editor):
    Category = apps.get_model("catalogue", "Category")
    Category.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_set_site_names'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
