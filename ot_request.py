from openerp.osv import fields,orm,osv
from openerp.tools.translate import _
import datetime

class ot_request(orm.Model):
	_name = "ot.request"


	def create(self,cr,uid,vals,context=None):
		if context is None:
			context = {}
		now = datetime.datetime.now()
		now_replace = now.replace(hour=4,minute=0,second=0,microsecond=0)
		if now < now_replace:
			raise osv.except_osv(_(u'warning'),_(u'time is over 12:00,you can not create ot request'))
		return super(ot_request,self).create(cr,uid,vals,context=context)

	def action_draft(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'draft'},context=context)

	def action_confirm(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'confirm'},context=context)

	def action_refused_by_department(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'refused by department'},context=context)

	def action_refused_by_administration(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'refused by administration'},context=context)

	def action_department(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'approved by department'},context=context)

	def action_administration(self,cr,uid,ids,context=None):
		return self.write(cr,uid,ids,{'state' : 'approved by administration'},context=context)

	def count_the_number(self,cr,uid,ids,field_name,arg,context=None):
		res = {}
		for i in self.browse(cr,uid,ids,context=context):
			res[i.id] = len(i.applicant)
		return res

	_columns = {
		'description' : fields.text("Description",readonly=True, states={'draft': [('readonly', False)]}),
		'number_of_applicants' : fields.function(count_the_number,type='integer',string="Number of Applicants"),
		'applicant' : fields.many2many('hr.employee',string="Applicant",readonly=True, states={'draft': [('readonly', False)]}),
		'date_start' : fields.date('Request Date',readonly=True, states={'draft': [('readonly', False)]}),
		'department' : fields.many2one('hr.department',string="Department",readonly=True, states={'draft': [('readonly', False)]}),
		'state' : fields.selection([
						('draft','Draft'),
						('confirm','Confirm'),
						('refused by department','Refused by Department'),
						('refused by administration','Refused by Administration'),
						('approved by department','Approved By Department'),
						('approved by administration','Approved By Administration')],'state'),
		'today' : fields.date('Today'),
		'create_date' : fields.date("Create_date"),
	}

	_defaults = {
		'state' : 'draft',
		'today' : lambda self, cr, uid, context={}: context.get('today', datetime.date.today()),
	}
