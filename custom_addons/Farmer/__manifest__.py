{
    'name': 'supply chain management system',
    'author': "Govind Bhujbal",
    'website': 'www.iqInnovationHub.com',
    'summary': 'Odoo 16 Development app',
    'license': 'AGPL-3',
    'depends': ['mail','purchase','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/farmer.xml',
        'views/packer.xml',
        'views/appointment.xml',
    ]
}
