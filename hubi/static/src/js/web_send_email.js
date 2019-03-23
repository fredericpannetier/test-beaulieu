odoo.define('web_send_email', function (require) {
"use strict";

		var core = require('web.core');
		var Sidebar = require('web.Sidebar');
		var ViewManager = require('web.ViewManager');
		var ListController = require('web.ListController');
		var session = require('web.session');
		var rpc = require('web.rpc');


		var QWeb = core.qweb;

		var _t = core._t;

		ListController.include({

			 renderButtons: function($node) {

			 this._super.apply(this, arguments);

					 if (this.$buttons) {
							 let filter_button = this.$buttons.find('.email_button');
               //  on click on the button with class export_treeview_xls call the function export_list_view
							 filter_button && filter_button.click(this.proxy('send_email')) ;
					 }
			 },
			 send_email: function () {
				//window.alert("email");
				//var res = rpc.query({
				rpc.query({
					model: 'account.invoice',
					method: 'invoice_send_email',
					args: [],
				    })
				    .fail(function() {
                        window.alert("send email failed");
                    })
                    .done(function(){
                        window.alert("send email done");
                    });
                //return false;
				return true;
			 }

	 });

});
