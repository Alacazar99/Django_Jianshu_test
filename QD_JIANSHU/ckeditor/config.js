/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	config.uiColor = '#eeeeee';
	config.extraPlugins ='codesnippet';
	config.removePlugins = 'elementspath';
	config.format_div = { element : 'div', attributes : { class : 'normalDiv' } };
	// config.resize_enabled = false;
	// config.resize_enabled = false;
};
