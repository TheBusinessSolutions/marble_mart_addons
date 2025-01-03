
from odoo import api, fields, models, tools


class PosOrderReport(models.Model):
	_inherit = "report.pos.order"

	def _select(self):
		return """
			SELECT
				MIN(l.id) AS id,
				COUNT(*) AS nbr_lines,
				s.date_order AS date,
				SUM(l.qty) AS product_qty,
				SUM(l.qty * l.price_unit) AS price_sub_total,
				CASE WHEN l.discount_line_type = 'Fixed'
					THEN  SUM((l.price_unit-l.discount)*l.qty)
					ELSE  SUM((l.qty * l.price_unit) * (100 - l.discount) / 100)
				END AS price_total, 
				CASE WHEN l.discount_line_type = 'Fixed'
					THEN  SUM((l.price_unit*l.qty)-(l.price_unit-l.discount)*l.qty)
					ELSE  SUM((l.qty * l.price_unit) * (l.discount / 100))
				END AS total_discount, 
				-- SUM((l.qty * l.price_unit) * (l.discount / 100)) AS total_discount,
				(SUM(l.qty*l.price_unit)/SUM(l.qty * u.factor))::decimal AS average_price,
				SUM(cast(to_char(date_trunc('day',s.date_order) - date_trunc('day',s.create_date),'DD') AS INT)) AS delay_validation,
				s.id as order_id,
				s.partner_id AS partner_id,
				s.state AS state,
				s.user_id AS user_id,
				s.location_id AS location_id,
				s.company_id AS company_id,
				s.sale_journal AS journal_id,
				l.product_id AS product_id,
				pt.categ_id AS product_categ_id,
				p.product_tmpl_id,
				ps.config_id,
				s.pricelist_id,
				s.session_id,
				s.account_move IS NOT NULL AS invoiced

		"""

	def _group_by(self):
		return super(PosOrderReport, self)._group_by() + ", l.discount_line_type"
