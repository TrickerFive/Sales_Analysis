from odoo import models, fields, api

class SaleAnalysis(models.Model):
    _name = 'sale.analysis'
    _description = 'Sales Analysis'

    date = fields.Date(string='Date')
    total_sales = fields.Float(string='Total Sales')
    total_revenue = fields.Float(string='Total Revenue')

    @api.model
    def calculate_sales(self):
        sales_data = self.env['sale.order'].read_group(
            [('state', '=', 'sale')],
            ['amount_total'],
            ['date_order:day']
        )
        for data in sales_data:
            self.create({
                'date': data['date_order:day'],
                'total_sales': data['amount_total_count'],
                'total_revenue': data['amount_total'],
            })