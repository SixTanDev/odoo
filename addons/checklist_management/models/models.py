# -*- coding: utf-8 -*-
# pylint: disable=W0104,C0103
from odoo import models, fields


class checklist_management(models.Model):
    """
        Represents a checklist management system in Odoo.
    """

    _name = 'checklist_management.checklist_management'
    _description = 'checklist_management.checklist_management'

    name = fields.Char(string='Título del checklist', required=True)
    description = fields.Text(string='Descripción del checklist')
    assigned_user_id = fields.Many2one('res.users', string='Usuario asignado')
    checklist_items = fields.One2many(
        'checklist_management.checklist_item',
        'checklist_id',
        string='Elementos del checklist'
    )


class checklist_item(models.Model):
    """
        Represents individual items or tasks within a checklist in Odoo.
    """

    _name = 'checklist_management.checklist_item'
    _description = 'checklist_management.checklist_item'

    name = fields.Char(string='Título del elemento del checklist', required=True)
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completado', 'Completado')
    ], string='Estado del elemento del checklist', default='pendiente')
    checklist_id = fields.Many2one(
        'checklist_management.checklist_management',
        string='Checklist al que pertenece'
    )
