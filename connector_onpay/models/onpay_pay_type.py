# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class OnPayType(models.Model):
    _name = "onpay.pay.type"
    _description = "OnPay Pay Type"

    name = fields.Char()
    code = fields.Char()
    treat_as_cash = fields.Boolean()
