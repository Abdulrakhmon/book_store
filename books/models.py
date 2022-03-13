from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Categories'
        db_table = 'book_category'


class Book(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books')
    image = models.ImageField(upload_to='books/')
    description = models.CharField(max_length=512)
    author = models.CharField(max_length=128)
    published_date = models.DateField(verbose_name='Published date')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'book'
        ordering = ('title',)


class ExtraQuantityForExistBook(models.Model):
    """
    Admin kitoblar sonini oshirmoqchi bolsa django admin panelidan Ixtiyoriy kitobga kiradi va kelgan miqdorni kiritadi
    va natijada save()  methodni override qilinganligi sabali Book model dagi quantity da ham ozgarish automatik
    ravishda tasir qiladi hamda report shakillanib bora boraveradi
    """
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title + ' - ' + str(self.quantity)

    def save(self, *args, **kwargs):
        if self.pk:
            old_quantity = ExtraQuantityForExistBook.objects.get(pk=self.pk).quantity
            if self.book.quantity + self.quantity - old_quantity >= 0:
                self.book.quantity = self.book.quantity + self.quantity - old_quantity
                self.book.save()
            else:
                raise Exception('Maxsulot miqdori 0 dan kam bop qolishi mumukun emas')
        else:
            self.book.quantity = self.book.quantity + self.quantity
            self.book.save()
        super(ExtraQuantityForExistBook, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Extra Quantity For Exist Book'
        verbose_name_plural = 'Extra Quantity For Exist Books'
        db_table = 'extra_quantity_for_exist_book'
        ordering = ('-id',)


class DiscountedBook(models.Model):
    """
    Ushbu modelda Discount qiliniyotgan vaqt oraligi, foizi, va tegishli kitoblar tanlanadi
    """
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    percentage = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    beginning_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + f'({self.percentage}%)'

    class Meta:
        verbose_name = 'Discounted Book'
        verbose_name_plural = 'Discounted Books'
        db_table = 'discounted_book'
        ordering = ('-id',)


class RateOfBook(models.Model):
    """
    ktibni baholash va comment qoldirish. Birkishi bitta kitobga faqat bir marta rate qila oladi
    """
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=512, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.rate} for {self.book.title} by {self.user.username}'

    class Meta:
        unique_together = ('book', 'user',)
        verbose_name = 'Rate of book'
        verbose_name_plural = 'Rates of books'
        db_table = 'rate_of_book'
        ordering = ('-id',)


class Order(models.Model):
    """
    Buyirtmaning umumiy korinishi. Yani raqami, umumiy summasi va umumiy harid qilingan kitoblar soni va kim tomonidan ekanligi
    """
    STATUS_CHOICES = (
        (1, 'Created'),
        (2, 'In progress'),
        (3, 'Rejected'),
        (4, 'Completed'),
    )

    number = models.CharField(max_length=10)
    total_quantity_of_items = models.PositiveSmallIntegerField()
    total_amount_of_purchase = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'order'
        ordering = ('-id',)


class OrderedBook(models.Model):
    """
    Buyurtmaga tegishli kitoblar, har bitta kitobdan nechtadan, va nechi puldan sotib olinganligini record qilib borish uchun
    """
    order = models.ForeignKey(Order, related_name='books', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book.title}({self.book.quantity})'

    class Meta:
        verbose_name = 'Ordered Book'
        verbose_name_plural = 'Ordered Books'
        db_table = 'ordered_book'
        ordering = ('-id',)

