import logging
from datetime import datetime, timedelta
from odoo.tools import float_is_zero
import psycopg2
from odoo import fields, models, api, tools, _
from pytz import timezone


_logger = logging.getLogger(__name__)
class PosOrder(models.Model):
    _inherit = "pos.order"


    @api.model
    def _payment_fields(self, order, ui_paymentline):
        res=super(PosOrder, self)._payment_fields(order,ui_paymentline)
        payment_date = ui_paymentline['name']
        payment_date = fields.Date.context_today(self, fields.Datetime.from_string(payment_date))
        res.update({
            'amount': ui_paymentline['amount'] or 0.0,
            'payment_date': payment_date,
            'payment_method_id': ui_paymentline['payment_method_id'],
            'card_type': ui_paymentline.get('card_type'),
            'transaction_id': ui_paymentline.get('transaction_id'),
            'pos_order_id': order.id,
            'payment_ref': ui_paymentline.get('payment_ref'),
        })
        return res

