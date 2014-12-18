import sublime
import sublime_plugin

from .css   import autocomp_css_hack

from .html  import autocomp_doctype
from .html  import autocomp_h
from .html  import autocomp_html
from .html  import autocomp_link
from .html  import autocomp_list
from .html  import autocomp_meta
from .html  import autocomp_pre

from .html  import autocomp_div
from .html  import autocomp_p

from .html  import autocomp_style
from .html  import autocomp_script

from .jsf   import autocomp_jsf_button
from .jsf   import autocomp_jsf_hidden
from .jsf   import autocomp_jsf_if
from .jsf   import autocomp_jsf_output

from .jsf   import autocomp_jsf_taglib

from .jsp   import autocomp_request
from .jsp   import autocomp_jsp_code

from .util  import sublime_view_util


############################################################################
# JSP に対する全オートコンプリートのリストを取得します。
############################################################################
def get_jsp_completions(view, prefix):
	completions = []

	if prefix[0] == "j":
		comp_list = autocomp_jsf_if.autocomp_get_jsf_if(view)
		completions.extend(comp_list)

		completions.append(autocomp_jsf_button.autocomp_get_jsf_command_button(view))
		completions.append(autocomp_jsf_hidden.autocomp_get_jsf_hidden(view))
		completions.append(autocomp_jsf_output.autocomp_get_jsf_output_text(view))

		comp_list = autocomp_jsf_taglib.autocomp_get_jsf_taglib(view)
		completions.extend(comp_list)

		comp_list = autocomp_jsp_code.autocomp_get_jsp_code(view)
		completions.extend(comp_list)

	if prefix[0] == "r":
		comp_list = autocomp_request.autocomp_get_request(view)
		completions.extend(comp_list)

	return completions

############################################################################
# CSS に対する全オートコンプリートのリストを取得します。
############################################################################
def get_css_completions(view, prefix):
	completions = []

	if prefix[0] == "c":
		comp_list = autocomp_css_hack.autocomp_get_css_hack(view)
		completions.extend(comp_list)

	return completions


############################################################################
# HTML に対する全オートコンプリートのリストを取得します。
############################################################################
def get_html_completions(view, prefix):
	completions = []

	if prefix[0] == "d":
		# doctype のオートコンプリート
		comp_list = autocomp_doctype.autocomp_get_doctype(view)
		completions.extend(comp_list)

		# div のオートコンプリート
		comp_list = autocomp_div.autocomp_get_div(view)
		completions.extend(comp_list)

	elif prefix[0] == "h":
		# HTML4 のオートコンプリート
		comp_list = autocomp_html.autocomp_get_html4(view)
		completions.extend(comp_list)

		# HTML5 のオートコンプリート
		completions.append(autocomp_html.autocomp_get_html5(view))

		# h のオートコンプリート
		comp_list = autocomp_h.autocomp_get_h_all(view)
		completions.extend(comp_list)

	elif prefix[0] == "l":
		# list のオートコンプリート
		comp_list = autocomp_list.autocomp_get_list(view)
		completions.extend(comp_list)
		# link style, link javascript のオートコンプリート
		completions.append(autocomp_link.autocomp_get_link_style(view))
		completions.append(autocomp_link.autocomp_get_link_javascript(view))

	elif prefix[0] == "m":
		# meta charset, no cache
		completions.append(autocomp_meta.autocomp_meta_charset(view))
		completions.append(autocomp_meta.autocomp_no_cache(view))

	elif prefix[0] == "n":
		# number list のオートコンプリート
		comp_list = autocomp_list.autocomp_get_number_list(view)
		completions.extend(comp_list)

	elif prefix[0] == "p":
		# pre のオートコンプリート
		comp_list = autocomp_pre.autocomp_get_pre(view)
		completions.extend(comp_list)

		# p のオートコンプリート
		comp_list = autocomp_p.autocomp_get_p(view)
		completions.extend(comp_list)

	elif prefix[0] == "s":
		# style のオートコンプリート
		comp_list = autocomp_style.autocomp_get_style(view)
		completions.extend(comp_list)

		# script のオートコンプリート
		completions.append(autocomp_script.autocomp_get_script(view))

	return completions

############################################################################
# HapoItak のオートコンプリートを行うクラスです。
############################################################################
class HapoItakCompletions(sublime_plugin.EventListener):
	
	############################################################################
	# オートコンプリートメソッド
	############################################################################
	def on_query_completions(self, view, prefix, locations):
		completions = []

		extension = sublime_view_util.get_extension(view.file_name())

		if extension == "html" or extension == "htm" or \
			extension == "jsp" or extension == "erb":
			
			completions = get_html_completions(view, prefix)

		if extension == "css" or extension == "html" or \
			extension == "htm" or extension == "jsp":
			
			comp_list = get_css_completions(view, prefix)
			completions.extend(comp_list)

		if extension == "jsp":
			comp_list = get_jsp_completions(view, prefix)
			completions.extend(comp_list)

		return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
