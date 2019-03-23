# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import os, sys
#FPimport win32print
from ..controllers import ctrl_print
#from controllers import ctrl_print
#from pycups import cups

class wizard_printlabel(models.TransientModel):
    _name = "wiz_print_label"
    _description = "Wizard print label"
    
    printer_id = fields.Many2one("hubi.printer", required=False) #FP20190313 False pour compilation
    label_id = fields.Many2one("hubi.labelmodel", required=False)
    #message = fields.Text(string="Information")
    

    def print_label(self):
        
        #FP20190318 printerName = "\\\\" + self.printer_id.adressip + "\\" + self.printer_id.realname
        printerName = self.printer_id.name
        labelFile = self.label_id.text #FP20190318 avant .file
        
        
        
        test = [("key1","value1"),("key2","value2"),("key3","value3")]
        

        
        ctrl_print.printlabelonwindows(self,printerName,labelFile,'[',test)
        #return {'type': 'ir.actions.act_window_close'}       
        
        return {'type': 'ir.actions.act_window_close'}  
    
    #@api.model
    #def default_get(self, fields):
        #res = super(wizard_printlabel, self).default_get(fields)
        #res["printer_id"] = self.env.context["active_id"]
        #if not self.env.context["active_ids"]:
        #    raise ValidationError("No select record")
        #return res 
 