// (C) 2015 by Yefei
var Web = {};

$.ajaxSetup({cache:false, dataType:'json'});

$.ajaxPrefilter(function(options, originalOptions, xhr){
	if (!options.crossDomain) {
		var token = $.cookie('csrftoken') || $('meta[name="csrf-token"]').attr('content');
		if (token) xhr.setRequestHeader('X-CSRFToken', token);
	}
});

$.notifySetup({sound: '/audio/notify.wav'});

/**
 * modal 浮层对话框
 */
Web.modal_defaults = {
	header: null,
	body: '',
	footer: null,
	closeButton: '<button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>',
	// bootstrap model options
	backdrop: true,
	keyboard: true,
	show: true,
	remote: false
};
Web.modal = function(options){
	var opts = $.extend({}, Web.modal_defaults, options);
	var header = null, footer = null;
	
	if (opts.header) {
		header = $('<div></div>').addClass('modal-header').append(opts.header);
	}
	
	if (opts.footer || opts.closeButton) {
		footer = $('<div></div>').addClass('modal-footer');
		opts.footer && footer.append(opts.footer);
		opts.closeButton && footer.append(opts.closeButton);
	}
	
	var body = $('<div></div>').addClass('modal-body').append(opts.body);
	var modal = $('<div></div>').addClass('modal fade').append(header).append(body).append(footer).modal({
		backdrop: opts.backdrop,
		keyboard: opts.keyboard,
		show: opts.show,
		remote: opts.remote
	});
	
	modal.on('hidden', function(){
		$(this).remove();
	});
	
	return modal;
};

$(document).ajaxError(function(event, xhr, ajaxSettings, thrownError){
	if (xhr.status >= 500 && xhr.status < 600) {
		$('<p>500: 服务器程序错误</p>').notify('error');
	}
	else if (xhr.status == 401) {
		$('<p>401: 未授权，请登陆帐号</p>').notify('error');
	}
	else if (xhr.status == 403) {
		$('<p>403: 没有权限</p>').notify('error');
	}
	else if (xhr.status == 404) {
		$('<p>404: 请求的资源不存在</p>').notify('error');
	}
	else if (xhr.status == 422) {
		var data = $.parseJSON(xhr.responseText);
		switch (data.type) {
		case 'FormError':
			var body = $('<div class="form-error"></div>');
			body.html($.map(data.message, function(v){
				return '<p>' + (v.label?'<label>'+v.label+'：</label>':'') + v.message + '</p>';
			}));
			Boxy.alert(body);
			break;
		case 'Deny':
			Boxy.alert(data.message);
			break;
		default:
			Boxy.alert(data.message);
			break;
		}
	}
});

Web.processingModal = function(){
	var html = $('<div class="processing">请稍候...</div>');
	return new Boxy(html, {modal:false, closeable:false, show:true, title:'处理中'});
};
