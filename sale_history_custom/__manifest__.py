# Technical Author: Pavel Daniel López Castillo
# -*- coding: utf-8 -*-
{
   "name": "Histórico de ventas",
   "summary": """Histórico de ventas del ERP anterior Navision""",

   "description": '''Funcionalidad:
- crear los modelos y añade el menú Ventas/Histórico de ventas para acceder a las vistas.
- crea botones smart en los formularios de clientes y productos, para mostrar la información.

Last version: 19-10-2023''',
   "author": "Landoo",
   "website": "https://www.landoo.es",
   'category': 'Sales',
   "version": "16.0.0.0.0",
   "depends": ['sale'],
   "data": [
       'security/ir.model.access.csv',
       'views/sale_history_model.xml',
       'views/sale_history_line_model.xml',
       'wizard/import_sale_history_wizard.xml',
       'wizard/import_sale_history_line_wizard.xml'
   ],
   'license': 'OPL-1',
}

