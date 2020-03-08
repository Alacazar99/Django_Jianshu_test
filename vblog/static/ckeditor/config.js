/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.removePlugins = 'image';
	config.extraPlugins = 'codesnippet, image2, uploadimage';

	config.toolbarGroups = [
		{
		  "name": "basicstyles",
		  "groups": ["basicstyles"]
		},
		{
		  "name": "links",
		  "groups": ["links"]
		},
		{
		  "name": "paragraph",
		  "groups": ["list", "blocks"]
		},
		{
		  "name": "document",
		  "groups": ["mode"]
		},
		{
		  "name": "insert",
		  "groups": ["insert"]
		},
		{
		  "name": "styles",
		  "groups": ["styles"]
		},
		{
		  "name": "about",
		  "groups": ["about"]
		}
  	];
	config.removeButtons = 'Underline, Strike, Subscript, Superscript, Anchor, Styles, Specialchar';
	config.filebrowserUploadUrl = '/blog/fileupload';
	config.filebrowserImageUploadUrl = '/blog/fileupload';
};