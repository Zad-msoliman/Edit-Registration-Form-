# -*- coding: utf-8 -*-
{
    'name': "task 2 ",

    'summary': "Task2",

    'website': "https://www.task2.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['auth_signup'],

    # always loaded
    'data': [
        'views/signup_inherit_template.xml',
        'views/res_user_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
