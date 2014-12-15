import sublime, sublime_plugin, re
from .util import string_util
from .util import sublime_view_util

############################################################################
# 関数 Begin
############################################################################

# ステータスバー表示
# self.view.set_status("key1", "In sample_read_excel3")

############################################################################
# プロパティにマッチします。
# (1) property ～ ～
############################################################################
def match_property(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*property\s+(.+)\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		variable_name = matchOB.group(1)
		logical_name  = matchOB.group(2)

		variable_camel  = string_util.to_camel_style(variable_name)
		variable_pascal = string_util.to_pascal_style(variable_name)

		answer_str = "\t/** " + logical_name + " */\n"
		answer_str += "\tprivate String " + variable_camel + ";\n"
		answer_str += "\n"
		answer_str += "\t/**\n"
		answer_str += "\t * " + logical_name + "を取得します。\n"
		answer_str += "\t * @return " + logical_name + "。\n"
		answer_str += "\t */\n"
		answer_str += "\tpublic String get" + variable_pascal + "() {\n"
		answer_str += "\t\treturn " + variable_camel + ";\n"
		answer_str += "\t}\n"
		answer_str += "\n"
		answer_str += "\t/**\n"
		answer_str += "\t * " + logical_name + "を設定します。\n"
		answer_str += "\t * @param " + variable_camel + " " + logical_name + "。\n"
		answer_str += "\t */\n"
		answer_str += "\tpublic void set" + variable_pascal + "(String " + variable_camel + ") {\n"
		answer_str += "\t\tthis." + variable_camel + " = " + variable_camel + ";\n"
		answer_str += "\t}\n"

		self.view.replace(edit, curr_region, answer_str)

		return True
	return False

############################################################################
# 関数 End
############################################################################



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
				# self.view.set_status("key1", "リプレイス")
				if not region.empty():
					selection = self.view.substr(region)
					selection = string_util.replace_html_special_character(selection)
					self.view.replace(edit, region, selection)

############################################################################
# ダブルクォーテーションに対してエスケープシーケンスを付与します。
############################################################################
class HapoItakAddEscapeToDoubleQuotationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection_list = self.view.sel()
		for region in selection_list:
			if not region.empty():
				selection = self.view.substr(region)
				selection = string_util.add_escape_sequence_to_double_quotation(selection)
				self.view.replace(edit, region, selection)


############################################################################
# Translate Command
# メイン処理
############################################################################
class HapoItakTranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# 現在のカーソル位置を取得します。
		curr_pos = self.view.sel()[0].begin()
		# 現在の行のリージョンを取得します。
		curr_region = self.view.line(curr_pos)
		# 現在の行の内容（文字列）を取得します。
		curr_line_str = self.view.substr(curr_region)

		extension = sublime_view_util.get_extension_from_view(self.view)

		# java ファイルのための処理
		if extension == "java":
			if match_property(self, edit, curr_pos, curr_region, curr_line_str):
				# sublime_view_util.move_cursor(self, edit, 0, -5)
				return True

		self.view.run_command('auto_complete', {
			'disable_auto_insert'      : False,
			'api_completions_only'     : True,
			'next_competion_if_showing': False
		})

	############################################################################
	# クイックパネルに関連付けられたメソッドです。
	# 選択時、InsertMyText メソッドを呼び出すことで、選択された文字列を挿入します。
	############################################################################
	def on_done(self, index):
		if index != -1:
			self.view.run_command("insert_my_text", {"args":{'text':self.list[index]}})

############################################################################
# クイックパネルの選択文字列を挿入するコマンドです。
############################################################################
class InsertMyText(sublime_plugin.TextCommand):
	def run(self, edit, args):
		# 現在のカーソル位置を取得します。
		curr_pos = self.view.sel()[0].begin()
		# 現在の単語のリージョンを取得します。
		curr_region = self.view.word(curr_pos)

		self.view.replace(edit, curr_region, args['text'])








