from django.db import models


class Movie(models.Model):
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('عنوان', max_length=100)
    director = models.CharField('کارگردان', max_length=50)
    year = models.IntegerField('سال ساخت')
    length = models.IntegerField('زمان')  # minute
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinemaa(models.Model):
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    cinema_code = models.IntegerField('کد سینما', primary_key=True)
    name = models.CharField('نام ', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('ظرفیت')
    phone = models.CharField('شماره تماس', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, verbose_name='فیلم')
    cinemaa = models.ForeignKey('Cinemaa', on_delete=models.PROTECT, verbose_name='سینما')
    start_time = models.DateTimeField('شروع سانس')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('صندلی های قابل فروش')
    free_seats = models.IntegerField('صندلی های خالی', default='100')
    # status_choices
    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKET_SOLED = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش شروع نشده است'),
        (SALE_OPEN, 'در حال فروش بلیط'),
        (TICKET_SOLED, 'بلیط تمام شد'),
        (SALE_CLOSED, 'فروش بلیط بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )

    status = models.IntegerField('وضعیت سانس', choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinemaa, self.start_time)
