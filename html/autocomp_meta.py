import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# meta charset 構文を取得します。
############################################################################
def get_meta_charset():
	save = sublime_view_util.get_indent() + \
		"<meta http-equiv=\"Content-Type\"  content=\"text/html; charset=" + \
		sublime_view_util.get_charset() + "\">"
	return save

############################################################################
# meta charset に対するコンプリートメソッドです。
############################################################################
def autocomp_meta_charset(view):
	return ("meta_charset\tHapoItak", get_meta_charset())




############################################################################
# no cache 構文を取得します。
############################################################################
def get_no_cache(is_indent):
	indent = ""
	if is_indent:
		indent = sublime_view_util.get_indent()
	save = indent + "<meta http-equiv=\"pragma\"        content=\"no-cache\">\n" +\
		indent + "<meta http-equiv=\"cache-control\" content=\"no-cache\">\n" +\
		indent + "<meta http-equiv=\"Expires\"       content=\"0\">\n"

	return save

############################################################################
# no cache に対するコンプリートメソッドです。
############################################################################
def autocomp_no_cache(view):
	return ("no_cache\tHapoItak", get_no_cache(False))

