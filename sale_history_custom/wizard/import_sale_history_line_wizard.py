# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.modules import module
import os
from xlrd import open_workbook

class ImportSaleHistoryLine(models.TransientModel):
    _name = 'import.sale.history.line'

    excel = fields.Binary('Archivo excel (formato recomendado: xlsx) para importar')

    def importar(self):
        path = os.path.join(module.get_module_path("sale_history_custom"), 'tmp', 'cc1.xlsx')
        wb = open_workbook(path)
        hoja = wb.sheet_by_index(0)
        numero_filas = hoja.nrows
        obj_sale_history_line = self.env['sale.history.line']
        for nro_fila in range(1, numero_filas):
            order_num = hoja.cell_value(rowx=nro_fila, colx=0)
            order_id = self.env['sale.history'].search([('order_num','=',order_num)]).id
            product_num = str(hoja.cell_value(rowx=nro_fila, colx=2))
            product_num = product_num.split('.')[0]
            product_id = self.env['product.product'].search([('default_code', '=', product_num)]).id
            try:
                record_sale_history_line = obj_sale_history_line.create({
                    'order_id':           order_id,
                    'order_num':          order_num,
                    'type':               hoja.cell_value(rowx=nro_fila, colx=1),
                    'product_id':         product_id,
                    'product_num':        product_num,
                    'ref_cruzada_num':    hoja.cell_value(rowx=nro_fila, colx=3),
                    'line_num':           hoja.cell_value(rowx=nro_fila, colx=4),
                    'product_iva_group':  hoja.cell_value(rowx=nro_fila, colx=5),
                    'description':        hoja.cell_value(rowx=nro_fila, colx=6),
                    'description2':       hoja.cell_value(rowx=nro_fila, colx=7),
                    'measures':           hoja.cell_value(rowx=nro_fila, colx=8),
                    'warehouse_ref':      hoja.cell_value(rowx=nro_fila, colx=9),
                    'quantity':           hoja.cell_value(rowx=nro_fila, colx=10),
                    'sale_price':         hoja.cell_value(rowx=nro_fila, colx=11),
                    'amount':             hoja.cell_value(rowx=nro_fila, colx=12),
                    'discount_percent':   hoja.cell_value(rowx=nro_fila, colx=13),
                    'discount_amount':    hoja.cell_value(rowx=nro_fila, colx=14),
                    'line_code':          hoja.cell_value(rowx=nro_fila, colx=15),
                })
            except:
                continue

