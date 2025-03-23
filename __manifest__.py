{
    'name': 'Sales_Analysis',
    'version': '1.0',
    'summary': 'Module to analyze financial and sales data',
    'description': """
        This module provides tools to analyze financial and sales data in Odoo 17.
    """,
    'author': 'Your Name',
    'depends': ['account', 'sale'],
    'data': [
            'views/menu.xml',
            'views/actions.xml',
            'views/sale_analysis_view.xml',
            'views/financial_analysis_view.xml',
            'reports/sale_report.xml',
            'reports/financial_report.xml',
    ],
    'installable': True,
    'application': True,
}
