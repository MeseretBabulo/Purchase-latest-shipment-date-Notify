from odoo import _, api, models, fields
import logging
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError,Warning 
from datetime import datetime, timedelta


class PurchaseShipmentDate(models.Model):
    _inherit = "purchase.order"

    

    issue_date = fields.Datetime(string="Issue Date", required=True, store=True)
    shipment_date = fields.Datetime(string="Shipment Date", compute='_compute_date', readonly=True, store=True)
    expired_date = fields.Datetime(string="Expiration Date", compute='_compute_date', readonly=True, store=True)
    user_id = fields.Many2one('res.users', string="Purchase")
    
    @api.depends('issue_date','shipment_date','expired_date')
    def _compute_date(self):
      
        for order in self:
          
            dates_list = order.issue_date
            
            _logger.info(dates_list)
           
            if dates_list:
               
                date = dates_list + timedelta(days=60);
                _logger.info(date)
                
                order.shipment_date = dates_list + timedelta(days=69)
                order.expired_date = dates_list + timedelta(days=90)
           
                
                


    def action_notify(self):
        values = self.env['purchase.order'].search([('state','like','draft')])
        _logger.info(len(values))
        
        if len(values) != 0:
            # values = self.env['purchase.order'].search([('issue_date', '>=', dates_list)])
            
            _logger.info("----------------dffff----------------------")
            val = []
            # products = []
            # notify = []
            # user = []
            for n in range(len(values)):
                    _logger.info(values[n].id)
                    shipment_date = values[n].shipment_date
                    issue_date = values[n].issue_date
                    
                    if(issue_date and shipment_date != False):
                        # dd = (shipment_date - issue_date)
                        date_difference = datetime.now() - issue_date
                        _logger.info(date_difference)
                       
                        _logger.info("--------------------------------------")
                        day, time  = str(date_difference).split(",")
                        d = f"{day}"
                        _logger.info(d)
                        da, days = str(d).split(" ")
        
                        days = f"{da}"
                        last_days = 69 - int(days)
                        last_days = str(last_days)
                        _logger.info(days)
                        
                        if int(days) >= 60 and int(days) < 70:
                            for l in values[n].order_line:
                                _logger.info(l.product_id.name)
                                val.append((last_days,l.product_id.name,values[n].user_id))#,values[n].product_id.name,values[n].user_id)
                                _logger.info(val)
                            # products.append(values[n].product_id.name)
                            # user.append(values[n].user_id)   
                              
                            
            _logger.info("----------------last day-------")
            _logger.info(val)
           
            for x in val:
                notify = 'You Have <h3><i>' + x[0] +  ' days left </i></h3>' + 'For Latest Shipment Date You  Must Check Product.<br>Products Like =  <b><i>' + x[1] + '</i></b>'
                
                x[2].notify_warning(notify,"<h3><b>Latest Shipment Date Alert</b></h3>",True)
            
            
        
                  
        
                       
            

    
  