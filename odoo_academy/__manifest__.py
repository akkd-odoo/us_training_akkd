# -*- coding: utf-8 -*-

{
    
    "name": "odoo ACADEMY",
    
    'summary': """This is an academy app to manage training""",
    
    'description': """
    
        Academy Module to manage Trainings:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': "Odoo",
    
    'website': "https://odoo.com",
    
    'category': 'training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    
    
    'demo':[
        
        "demo/academy_demo.xml",
        
    ],
    
    
}