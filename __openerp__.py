{
    'name' : "HR OT Request System",
    'summary' : "Over Time request",
    'description' : """
        This is a module developed for OT request in Horn
	""",
    'author' : "Frank from Horn",
    'version' : "1.0",
    'depends' : ['base','hr'],
    'data' : [
       'approve_buttons_wizard.py',
       'approve_buttons_wizard_view.xml',
	     'ot_request_view.xml',
       'ot_request_workflow.xml',
       'security/ot_request_security.xml',
	]
}
