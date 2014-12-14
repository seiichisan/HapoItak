import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# jsf taglib の宣言文を取得します。
############################################################################
def get_jsf_taglib_base():
	save = "<%@ taglib prefix=\"f\" uri=\"http://java.sun.com/jsf/core\" %>\n"
	save += "<%@ taglib prefix=\"h\" uri=\"http://java.sun.com/jsf/html\" %>\n"

	return save


############################################################################
# jsf taglib jstl の宣言文を取得します。
############################################################################
def get_jsf_taglib_jstl():
	save = "<%@ taglib prefix=\"c\" uri=\"http://java.sun.com/jsp/jstl/core\"　%>\n"

	return save


############################################################################
# jsf taglib に対するオートコンプリートメソッドです。
############################################################################
def autocomp_get_jsf_taglib(view):
	completions = []

	completions.append(("jsf_taglib\tHapoItak"     , get_jsf_taglib_base()))
	completions.append(("jsf_taglib_jstl\tHapoItak", get_jsf_taglib_jstl()))
	completions.append(("jsf_taglib_base_and_jstl\tHapoItak", get_jsf_taglib_base() + get_jsf_taglib_jstl()))

	return completions

