# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.modules import module
import os
import xlrd
from xlrd import open_workbook
from datetime import datetime

class ImportSaleHistory(models.TransientModel):
    _name = 'import.sale.history'

    excel = fields.Binary('Archivo excel (formato recomendado: xlsx) para importar')

    def importar(self):
        path = os.path.join(module.get_module_path("sale_history_custom"), 'tmp', 'cc2.xlsx')
        wb = open_workbook(path)
        hoja = wb.sheet_by_index(0)
        numero_filas = hoja.nrows
        obj_sale_history_line = self.env['sale.history']
        for nro_fila in range(1, numero_filas):
            date = hoja.cell_value(rowx=nro_fila, colx=0)
            fecha = datetime(*xlrd.xldate_as_tuple(date, wb.datemode))
            sale_address_country_name = hoja.cell_value(rowx=nro_fila, colx=8)
            sale_address_country_id = self.env['res.country'].search([('code', '=',sale_address_country_name)]).id
            sale_address_name = hoja.cell_value(rowx=nro_fila, colx=5)
            sale_address_partner_id = self.env['res.partner'].search([('display_name','=',sale_address_name)]).id
            try:
                record_sale_history_line = obj_sale_history_line.create({
                    'date':                         fecha,
                    'business_account':             hoja.cell_value(rowx=nro_fila, colx=1),
                    'status':                       hoja.cell_value(rowx=nro_fila, colx=2),
                    'order_num':                    hoja.cell_value(rowx=nro_fila, colx=3),
                    'sale_address_ref':             str(hoja.cell_value(rowx=nro_fila, colx=4)).split('.')[0],
                    'sale_address_name':            sale_address_name,
                    'amount':                       hoja.cell_value(rowx=nro_fila, colx=6),
                    'sale_address_country_pcode':   str(hoja.cell_value(rowx=nro_fila, colx=7)).split('.')[0],
                    'sale_address_country_name':    sale_address_country_name,
                    'sale_address_contact':         hoja.cell_value(rowx=nro_fila, colx=9),
                    'invoice_partner_ref':          hoja.cell_value(rowx=nro_fila, colx=10),
                    'invoice_partner_name':         hoja.cell_value(rowx=nro_fila, colx=11),
                    'comercial_ref':                str(hoja.cell_value(rowx=nro_fila, colx=12)).split('.')[0],
                    'sale_address_country_id':      sale_address_country_id,
                    'sale_address_partner_id':      sale_address_partner_id,
                })
            except:
                continue


