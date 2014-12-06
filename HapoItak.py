import sublime, sublime_plugin, re
from .html import html
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
# jsf 系メソッド Begin
############################################################################

############################################################################
# jsf if タグを取得します。
# if_flag が true  の場合、if   の働きをするタグを取得します。
# if_flag が false の場合、else の働きをするタグを取得します。
############################################################################
def get_jsf_if_tag(if_flag):
	if if_flag:
		save = "<c:if test='${xxx == \"y\"}'>\n" +\
			"\n" +\
			"</c:if>\n"
	else:
		save = "<c:if test='${xxx != \"y\"}'>\n" +\
			"\n" +\
			"</c:if>\n"
	return save


############################################################################
# jsf output text にマッチします。
# (1) jsf output text
############################################################################
def match_jsf_three_word(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*jsf\s+(.+)\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_var1 = matchOB.group(1)
		temp_var2 = matchOB.group(2)
		if temp_var1 == "output" and temp_var2 == "text":
			temp_str2 = "<h:outputText value=\"#{xxx}\" />"
			self.view.replace(edit, curr_region, temp_str2)
			return True
		elif temp_var1 == "if" and temp_var2 == "else":
			temp_str2 = get_jsf_if_tag(True) + get_jsf_if_tag(False)
			self.view.replace(edit, curr_region, temp_str2)
			return True
	return False

############################################################################
# jsf if にマッチします。
# (1) jsf if
# (2) jsf button
############################################################################
def match_jsf_two_word(self, edit, curr_pos, curr_region, curr_line_str):
	if match_jsf_three_word(self, edit, curr_pos, curr_region, curr_line_str):
		return True

	pattern = r"\s*jsf\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		if temp_str == "if":
			temp_str2 = get_jsf_if_tag(True)
			self.view.replace(edit, curr_region, temp_str2)
			return True
		elif temp_str == "button":
			temp_str2 = "<h:commandButton styleClass=\"xxx\" id=\"yyy\"\n" +\
				"\tvalue=\"zzz\" action=\"#{XxxAction.yyy}\">\n" +\
				"</h:commandButton>\n"
			self.view.replace(edit, curr_region, temp_str2)
			return True
		elif temp_str == "hidden":
			temp_str2 = "<h:inputHidden id=\"xxx\" value=\"#{xxx}\" />"
			self.view.replace(edit, curr_region, temp_str2)
			return True
	return False

############################################################################
# jsf 系メソッド End
############################################################################

############################################################################
# 関数 End
############################################################################



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

		extension = sublime_view_util.get_extension_from_view(self)
		# self.view.set_status("key2", "拡張子：" + extension)

		# java ファイルのための処理
		if extension == "java":
			if match_property(self, edit, curr_pos, curr_region, curr_line_str):
				return True

		# jsp のための処理
		elif extension == "jsp":
			if match_jsf_two_word(self, edit, curr_pos, curr_region, curr_line_str):
				return True

		if extension == "html" or extension == "jsp":
			# HTML のための処理
			if html.match_doc_type_series(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_html(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_link_javascript(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_link_style(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_list(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_meta_utf(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_no_cache(self, edit, curr_pos, curr_region, curr_line_str):
				return True
			if html.match_put_html_series(self, edit, curr_pos, curr_region, curr_line_str):
				return True



