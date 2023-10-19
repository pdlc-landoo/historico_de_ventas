# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools

class SaleHistory(models.Model):
    _name = 'sale.history'
    _description = 'Sale History'
    _rec_name = 'order_num'

    date = fields.Date(string="Fecha pedido")
    business_account = fields.Char('Grupo contable negocio')
    status = fields.Char('Estado')
    order_num = fields.Char('Número de pedido')
    sale_address_ref = fields.Char('Venta a-Nº cliente')
    sale_address_name = fields.Char('Venta a-Nombre')
    sale_address_partner_id = fields.Many2one('res.partner', string='Venta a')
    amount = fields.Float(string='Importe')
    sale_address_country_pcode = fields.Char('Venta a-C.P.')
    sale_address_country_name = fields.Char('Venta a-Cód. país/región')
    sale_address_country_id = fields.Many2one('res.country', string='Venta a País')
    sale_address_contact = fields.Char('Venta a-Atención')
    invoice_partner_ref = fields.Char('Factura a-Nº cliente')
    invoice_partner_name = fields.Char('Fact. a-Nombre')
    comercial_ref = fields.Char('Cód. vendedor')

