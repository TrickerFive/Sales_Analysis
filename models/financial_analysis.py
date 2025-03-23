from odoo import models, fields, api

class FinancialAnalysis(models.Model):
    _name = 'financial.analysis'
    _description = 'Financial Analysis'

    date = fields.Date(string='Date')
    total_income = fields.Float(string='Total Income')
    total_expense = fields.Float(string='Total Expense')
    net_profit = fields.Float(string='Net Profit')

    @api.model
    def calculate_financials(self):
        income_data = self.env['account.move'].read_group(
            [('move_type', '=', 'out_invoice')],
            ['amount_total'],
            ['invoice_date:day']
        )
        expense_data = self.env['account.move'].read_group(
            [('move_type', '=', 'in_invoice')],
            ['amount_total'],
            ['invoice_date:day']
        )
        for income, expense in zip(income_data, expense_data):
            self.create({
                'date': income['invoice_date:day'],
                'total_income': income['amount_total'],
                'total_expense': expense['amount_total'],
                'net_profit': income['amount_total'] - expense['amount_total'],
            })