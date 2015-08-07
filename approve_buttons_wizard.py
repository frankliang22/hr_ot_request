from openerp.osv import fields,orm,osv
from openerp.tools.translate import _

class approve_buttons(osv.osv_memory):
	_name = "approve.buttons"

	def department_approve_request(self,cr,uid,ids,context=None):
		if context is None:
			context = {}
		ot_request_obj = self.pool.get('ot.request')
		confirm_request_id = self.pool.get('ot.request').search(cr,uid,[('state', '=', 'confirm'),('date_start','=','today')],limit=None,context=context)
		for record in ot_request_obj.browse(cr,uid,confirm_request_id,context=context):
			record.state = 'approved by department'

	def administration_approve_request(self,cr,uid,ids,context=None):
		if context is None:
			context = {}
		ot_request_obj = self.pool.get('ot.request')
		department_approve_request_id = self.pool.get('ot.request').search(cr,uid,[('state','=','approved by department'),('date_start','=','today')],context=context)
		for record in ot_request_obj.browse(cr,uid,department_approve_request_id,context=context):
			record.state = 'approved by administration'

	def department_refuse_request(self,cr,uid,ids,context=None):
		if context is None:
			context = {}
		ot_request_obj = self.pool.get('ot.request')
		confirm_request_id = self.pool.get('ot.request').search(cr,uid,[('state','=','confirm'),('date_start','=','today')],limit=None,context=context)
		for record in ot_request_obj.browse(cr,uid,confirm_request_id,context=context):
			record.state = 'refused by department'		

	def administration_refuse_request(self,cr,uid,ids,context=None):
		if context is None:
			context = {}
		ot_request_obj = self.pool.get('ot.request')
		department_approve_request_id = self.pool.get('ot.request').search(cr,uid,[('state','=','approved by department'),('date_start','=','today')],context=context)
		for record in ot_request_obj.browse(cr,uid,department_approve_request_id,context=context):
			record.state = 'refused by administration'