# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools

class SaleHistoryLine(models.Model):
    _name = 'sale.history.line'
    _description = 'Sale History Line'

    order_num = fields.Char('Número de pedido')
    order_id = fields.Many2one('sale.history', string='Pedido')
    type = fields.Char('Tipo')
    product_num = fields.Char('Num. Producto (Nº)')
    product_id = fields.Many2one('product.product', string='Producto')
    ref_cruzada_num = fields.Char('Nº referencia cruzada')
    line_num = fields.Char('Nº línea')
    product_iva_group = fields.Char('Grupo registro IVA prod.')
    description = fields.Char('Descripción')
    description2 = fields.Char('Descripción2')
    measures = fields.Char('Medidas')
    warehouse_ref = fields.Char('Cód. almacén')
    quantity = fields.Float('Cantidad')
    sale_price = fields.Float('Precio venta excl. IVA')
    amount = fields.Float('Importe línea excl. IVA')
    discount_percent = fields.Float('% Descuento línea')
    discount_amount = fields.Float('Importe dto. línea')
    line_code = fields.Char('Código Línea')