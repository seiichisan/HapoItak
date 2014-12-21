import sublime, sublime_plugin, re
from .util import string_util
from .util import sublime_view_util



############################################################################
# HTML の特殊文字セットを変換するコマンド
# メイン処理
#
# 下記の処理を行います。
# < → &lt;
# > → &gt;
############################################################################
class HapoItakReplaceHtmlSpecialCharacterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		extension = sublime_view_util.get_extension_from_view(self.view)
		if extension == "html" or extension == "htm" or extension == "jsp":
			selection_list = self.view.sel()
			for region in selection_list:
				if not region.empty():
					selection = self.view.substr(region)
					selection = string_util.replace_html_special_character(selection)
					self.view.replace(edit, region, selection)
