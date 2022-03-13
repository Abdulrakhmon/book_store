from django.contrib import admin

from books.models import Category, Book, ExtraQuantityForExistBook, DiscountedBook, RateOfBook, Order, OrderedBook


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ExtraQuantityForExistBookInline(admin.TabularInline):
    extra = 0
    model = ExtraQuantityForExistBook


class RateOfBookInline(admin.TabularInline):
    extra = 0
    model = RateOfBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price', 'quantity']
    search_fields = ['title', 'author']
    list_filter = ['category']
    inlines = [ExtraQuantityForExistBookInline, RateOfBookInline]

    #   make a field editable while creating, but read only in existing objects
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["quantity"]
        else:
            return []


@admin.register(DiscountedBook)
class DiscountedBookAdmin(admin.ModelAdmin):
    list_display = ['beginning_time', 'ending_time', 'percentage']
    search_fields = ['percentage']


class OrderedBookInline(admin.TabularInline):
    extra = 0
    model = OrderedBook


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['number', 'total_quantity_of_items', 'total_amount_of_purchase', 'status']
    search_fields = ['number']
    list_filter = ['status']
    inlines = [OrderedBookInline]
