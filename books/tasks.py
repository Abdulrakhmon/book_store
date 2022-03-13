import os
from datetime import date, timedelta

import xlwt
from django.conf import settings
from django.core.mail import EmailMessage

from book_store.celery import app
from book_store.settings import BASE_DIR
from books.models import Order


@app.task
def send_excel():
    try:
        subject = 'Haftalil hisobot'
        message = 'Songi bir haftalik buyurtmalar bilan tanishing.'
        today = date.today()
        one_week_ago = today - timedelta(days=7)
        file_name = 'excel_for_' + today.strftime('%Y-%m-%d')
        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header names, you can use your own headers here
        columns = ['Buyurtma raqami', 'Umumiy narxi', 'Maxsulotlar soni', 'Xaridor ismi', 'Xaridor tel raqami']

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        orders = Order.objects.filter(updated_at__gte=one_week_ago, updated_at__lte=today)

        for order in orders:
            row_num = row_num + 1
            ws.write(row_num, 0, order.number, font_style)
            ws.write(row_num, 1, order.total_amount_of_purchase, font_style)
            ws.write(row_num, 2, order.total_quantity_of_items, font_style)
            ws.write(row_num, 3, order.user.first_name, font_style)
            ws.write(row_num, 4, order.user.phone, font_style)

        file_path = 'media/excel/{}.xls'.format(file_name)
        wb.save(os.path.join(BASE_DIR, file_path))
        attach = open(file_path)
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['abdulrakhmon.mukhitdinov.97@gmail.com', ])
        mail.content_subtype = 'text/xls'
        mail.attach_file(attach.name)
        mail.send()
    except Exception as e:
        print(e)
    return True