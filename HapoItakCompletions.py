import sublime
import sublime_plugin

from .html  import autocomp_doctype
from .html  import autocomp_html
from .html  import autocomp_link
from .html  import autocomp_list
from .html  import autocomp_meta
from .html  import autocomp_style
from .html  import autocomp_script

from .jsf   import autocomp_jsf_button
from .jsf   import autocomp_jsf_hidden
from .jsf   import autocomp_jsf_if
from .jsf   import autocomp_jsf_output

from .util  import sublime_view_util


############################################################################
# HTML に対する全オートコンプリートのリストを取得します。
############################################################################
def get_html_completions(view):
	completions = []

	# doctype のオートコンプリート
	comp_list = autocomp_doctype.autocomp_get_doctype(view)
	completions.extend(comp_list)
	# for comp in comp_list:
	# 	completions.append(comp)

	# HTML4 のオートコンプリート
	comp_list = autocomp_html.autocomp_get_html4(view)
	completions.extend(comp_list)

	# HTML5 のオートコンプリート
	completions.append(autocomp_html.autocomp_get_html5(view))

	# list のオートコンプリート
	comp_list = autocomp_list.autocomp_get_list(view)
	completions.extend(comp_list)

	# number list のオートコンプリート
	comp_list = autocomp_list.autocomp_get_number_list(view)
	completions.extend(comp_list)

	# meta charset, no cache, link style, link javascript のオートコンプリート
	completions.append(autocomp_meta.autocomp_meta_charset(view))
	completions.append(autocomp_meta.autocomp_no_cache(view))
	completions.append(autocomp_link.autocomp_get_link_style(view))
	completions.append(autocomp_link.autocomp_get_link_javascript(view))

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

		if extension == "html" or extension == "jsp":
			completions = get_html_completions(view)

		if extension == "jsp":
			tmp_completions = autocomp_jsf_if.autocomp_get_jsf_if(view)
			completions.extend(tmp_completions)

			completions.append(autocomp_jsf_button.autocomp_get_jsf_command_button(view))
			completions.append(autocomp_jsf_hidden.autocomp_get_jsf_hidden(view))
			completions.append(autocomp_jsf_output.autocomp_get_jsf_output_text(view))

		return (completions, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)