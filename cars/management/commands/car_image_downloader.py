# coding: utf-8

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

import requests

from cars.models import CarColor, Car, CarPhoto, CarModel


class Command(BaseCommand):
    """
    скачивает картинки
    """

    def handle(self, *args, **options):
        # self.hyundai()
        self.kia()

    def kia(self):
        self._kia(
            name=u"picanto",
            url_name=u"picanto5d",
            url_id=u"7001207",
            image_id=u'BEG',
            colors={
                u"Signal_Red": u"#860b0b",
                u"Clear_White": u"#ffffff",
                u"Bright_Silver": u"#dedee1",
                u"Midnight_Black": u"#0d0d0d",
                u"Milky_Beige": u"#d0d0c8",
                u"Titanium_Silver": u"#939393",
                u"Honey_Bee": u"#efc164",
                u"Alice_Blue": u"#4582b7",
                u"Cherry_Pink": u"#915467",
                u"Dazzling_Blue": u"#375c89",
            }
        )

    def _kia(self, name, url_name, url_id, image_id, colors, start=0, stop=80):

        url = (
            u"http://i{server_id}.kia.ru/upload/models/render/"
            u"{url_name}/{url_id}/{image_id}_{image_name}"
        )

        car_model = CarModel.objects.get(name=u"kia")
        car = Car.objects.get(name=name, model=car_model)
        CarPhoto.objects.filter(car=car).delete()
        print name
        for color_name, color_hex in colors.iteritems():
            print '', color_name
            try:
                color = CarColor.objects.get(hex=color_hex)
            except CarColor.DoesNotExist:
                color = CarColor(name=color_name.lower(), hex=color_hex.upper())
                color.save()
            server_id = 0
            for image_number in xrange(start, stop):
                server_id += 1
                image_name = u'{:0>5}.jpg'.format(image_number)
                _url = url.format(
                    server_id=server_id,
                    url_name=url_name,
                    url_id=url_id,
                    image_id=image_id,
                    image_name=image_name
                )
                response = requests.get(_url)
                if response.status_code != 200:
                    print image_number, response.status_code
                    break

                car_photo = CarPhoto(car=car, color=color)
                car_photo.image.save(
                    image_name,
                    ContentFile(response.content),
                    save=True)
                car_photo.save()
                if server_id > 9:
                    server_id = 0

    def hyundai(self):
        self._hyundai(
            name=u"creta",
            colors={
                u"Black": u"#18161B",
                u"Mystic_blue": u"#2170AA",
                u"Orange": u"#E95100",
                u"Pearibeage": u"#8f7563",
                u"Silver": u"#C9CDD6",
                u"Stardust": u"#626165",
                u"White": u"#F4F4F6",
            }
        )
        self._hyundai(
            name=u"solaris",
            colors={
                u"Garnet": u'#C64040',
                u"Carbon_Grey": u'#949597',
                u"Coffee_Bean": u'#86776C',
                u"Crystal_White": u'#FFFFFF',
                u"Dazzling_Blue": u'#325488',
                u"Misty_Beige": u'#C6C5C0',
                u"Phantom_Black": u'#08090B',
                u"Sleek_Silver": u'#CFCFCF',
                u"Vitamin_C": u'#D87C5A',
            })
        self._hyundai(
            name=u"elantra",
            colors={
                u"Marina_Blue": u'#135D9E',
                u"Polar_White": u'#DDDDDD',
                u"Fiery_Red": u'#B82F32',
                u"Ice_Wine": u'#99978B',
                u"Iron_Gray": u'#63696B',
                u"Blazing_Yellow": u'#BAAA5F',
                u"Moonlight_Blue": u'#3A4969',
                u"Phantom_Black": u'#3C3C3E',
                u"Phoenix_Orange": u'#9B371F',
                u"Platinum_Silver": u'#969798',
                u"Sparkling_Metal": u'#4A5154',
            })
        self._hyundai(
            name=u"i40",
            colors={
                u"Creamy_White": u'#E8E7E1',
                u"White_Crystal": u'#ECF0F2',
                u"Mineral_Blue": u'#91BDC0',
                u"Ocean_View": u'#45545F',
                u"Phantom_Black": u'#111111',
                u"Red_Merlot": u'#6E0E10',
                u"Sleek_Silver": u'#C4C7C9',
                u"Tan_Brown": u'#675D54',
                u"Titanum_Silver": u'#6A6B66',
                u"Chalk_Beige": u'#E8DFBE',
                u"Blue_Spirit": u'#87CEFA',
                u"Stone_Gray": u'#1B2324',
            })
        self._hyundai(
            name=u"santafe",
            colors={
                u"White_Crystal": u'#ECF0F2',
                u"Creamy_White": u'#E8E7E1',
                u"Mineral_Blue": u'#91BDC0',
                u"Mystic_Beige": u'#ABA8A0',
                u"Ocean_view": u'#45545F',
                u"Phantom_Black": u'#111111',
                u"Red_Merlot": u'#6E0E10',
                u"Sleek_Silver": u'#C4C7C9',
                u"Tan_Brown": u'#675D54',
                u"Titanium_Silver": u'#6A6B66',
                u"Chalk_Beige": u'#E8DFBE',
            })

    def _hyundai(self, name, colors, start=1, stop=50):

        url = (
            u"http://hyundai-kanavto.ru/media/images/360/"
            u"{car}/{color}/{image_name}")

        car_model = CarModel.objects.get(name=u"huyndai")
        car = Car.objects.get(name=name, model=car_model)
        CarPhoto.objects.filter(car=car).delete()
        print name
        for color_name, color_hex in colors.iteritems():
            print '', color_name
            try:
                color = CarColor.objects.get(hex=color_hex)
            except CarColor.DoesNotExist:
                color = CarColor(name=color_name.lower(), hex=color_hex.upper())
                color.save()

            for image_number in xrange(start, stop):
                image_name = u'{:0>2}.png'.format(image_number)
                _url = url.format(
                    car=car.name,
                    color=color_name,
                    image_name=image_name
                )
                response = requests.get(_url)
                if response.status_code != 200:
                    print image_number, response.status_code
                    break

                car_photo = CarPhoto(car=car, color=color)
                car_photo.image.save(
                    image_name,
                    ContentFile(response.content),
                    save=True)
                car_photo.save()
