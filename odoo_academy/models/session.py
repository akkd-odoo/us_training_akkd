# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class Session(models.Model):
    
    _name = 'academy.session'
    _description = 'Session Info'
    
    # add logging
    _logger.info('------------------------')

    _logger.info('NEW SESSION HERE ********************')
    _logger.info('------------------------')
    #
    
    course_id = fields.Many2one(comodel_name='academy.course',string="Course",ondelete="cascade",required=True)
    
    name = fields.Char(string="Title", related="course_id.name")
    
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")
    
    student_ids = fields.Many2many(comodel_name="res.partner", string="Students")