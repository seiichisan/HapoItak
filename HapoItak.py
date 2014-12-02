import sublime, sublime_plugin, re
from .html import html
from .util import string_util

class HapoItakHelloCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# 現在のカーソル位置を取得します。
		curr_pos = self.view.sel()[0].begin()
		# 現在のカーソル位置に Hello World と書き込みます。
		self.view.insert(edit, curr_pos, "Hello, World!")

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
# link javascript にマッチします。
# (1) link javascript ～
############################################################################
def match_link_javascript(self, edit, curr_pos, curr_region, curr_line_str):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	javascript_base_path = hapo_settings.get("javascript_base_path")

	pattern = r"\s*link\s+javascript\s+(.*)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		if javascript_base_path is not None:
			temp_str = javascript_base_path + "/" + temp_str
		temp_str2 = "\t<script type=\"text/javascript\" src=\"" + \
			temp_str + ".js?v=0.1\"></script>"
		self.view.replace(edit, curr_region, temp_str2)
		return True
	return False





# list にマッチします。
# (1) list ～
def match_list(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*list\s+([0-9]*)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		# 生成するリストの数を設定します。
		list_max_count = int(temp_str)
		temp_str2 = "<ul class=\"xxx\">\n"

		i = 0
		while i < list_max_count:
			temp_str2 = temp_str2 + "\t<li></li>\n"
			i = i + 1

		temp_str2 = temp_str2 + "</ul>\n"

		self.view.replace(edit, curr_region, temp_str2)
		return True
	return False





# html4 と html5 にマッチします。
# (1) html4
# (2) html5
def match_html(self, edit, curr_pos, curr_region, curr_line_str):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	css_base_path = hapo_settings.get("css_base_path")

	pattern = r"html([45])"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		if temp_str == "4":
			temp_str2 = \
				"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\n" +\
				"<html lang=\"ja\">\n" +\
				"<head>\n" +\
				"\t<meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\">\n" +\
				"\t<meta http-equiv=\"Pragma\"        content=\"no-cache\">\n" +\
				"\t<meta http-equiv=\"Cache-Control\" content=\"no-cache\">\n" +\
				"\t<meta http-equiv=\"Expires\"       content=\"0\">\n" +\
				html.get_link_style(css_base_path, "xxx") + "\n" +\
				"\t<title>XXX</title>\n" +\
				"</head>\n" +\
				"<body>\n" +\
				"\n" +\
				"</body>\n" +\
				"</html>\n"
			self.view.replace(edit, curr_region, temp_str2)
			return True
		elif temp_str == "5":
			temp_str2 = "<!doctype html>\n" +\
				"<html lang=\"ja\">\n" +\
				"<head>\n" +\
				"\t<meta charset=\"UTF-8\">\n" +\
				"\t<title>XXX</title>\n" +\
				"</head>\n" +\
				"<body>\n" +\
				"\n" +\
				"</body>\n" +\
				"</html>\n"
			self.view.replace(edit, curr_region, temp_str2)
			return True
	return False



# 下記にマッチします。
# (1) put css
# (2) put javascript
# (3) put javascript html5
def match_put_html_series(self, edit, curr_pos, curr_region, curr_line_str):
	patternJavaScript = r"\s*put\s+javascript"
	matchJavaScript = re.match(patternJavaScript, curr_line_str)
	if matchJavaScript:
		patternJavaScriptHtml5 = r"\s*put\s+javascript\s+html5"
		matchJavaScriptHtml5 = re.match(patternJavaScriptHtml5, curr_line_str)
		if matchJavaScriptHtml5:
			temp_str = "<script>\n" +\
				"\n" +\
				"</script>\n"
			self.view.replace(edit, curr_region, temp_str)
			return True
		temp_str = "<style type=\"text/javascript\">\n" +\
			"<!--\n" +\
			"\n" +\
			"// -->\n" +\
			"</style>\n"
		self.view.replace(edit, curr_region, temp_str)
		return True

	patternCss = r"\s*put\s+css"
	matchCss = re.match(patternCss, curr_line_str)
	if matchCss:
		temp_str = "<style type=\"text/css\">\n" +\
			"\n" +\
			"</style>\n"
		self.view.replace(edit, curr_region, temp_str)
		return True
	return False				

# doctype 系にマッチします。
# (1) doctype4
# (2) doctype4 frame
# (3) doctype4 strict
def match_doc_type_series(self, edit, \
	curr_pos, curr_region, curr_line_str):
	patternDocType = r"\s*doctype4"
	matchDocType = re.match(patternDocType, curr_line_str)
	if matchDocType:
		patternDocType2 = r"\s*doctype4\s+(.*)"
		matchDocType2 = re.match(patternDocType2, curr_line_str)
		if matchDocType2:
			temp_str = matchDocType2.group(1)
			if temp_str == "frame":
				temp_str2 = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Frameset//EN\" \"http://www.w3.org/TR/html4/frameset.dtd\">"
				self.view.replace(edit, curr_region, temp_str2)
				return True
			elif temp_str == "strict":
				temp_str2 = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
				self.view.replace(edit, curr_region, temp_str2)
				return True
		temp_str2 = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">"
		self.view.replace(edit, curr_region, temp_str2)
		return True
	return False

# no cache にマッチします。
# (1) no cache
def match_no_cache(self, edit, \
	curr_pos, curr_region, curr_line_str):
	patternNoCache = r"\s*no\s+cache"
	matchNoCache = re.match(patternNoCache, curr_line_str)
	if matchNoCache:
		temp_str =\
			"\t<meta http-equiv=\"pragma\"        content=\"no-cache\">\n" +\
			"\t<meta http-equiv=\"cache-control\" content=\"no-cache\">\n" +\
			"\t<meta http-equiv=\"Expires\"       content=\"0\">\n"
		self.view.replace(edit, curr_region, temp_str)
		return True
	return False

# meta utf8 にマッチします。
# (1) meta utf8
def match_meta_utf(self, edit, \
	curr_pos, curr_region, curr_line_str):
	patternMeta = r"\s*meta utf8"
	matchMeta = re.match(patternMeta, curr_line_str)
	if matchMeta:
		temp_str = "<meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\">"
		self.view.replace(edit, curr_region, temp_str)
		return True
	return False






############################################################################
# 関数 End
############################################################################

class HapoItakTranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# 現在のカーソル位置を取得します。
		curr_pos = self.view.sel()[0].begin()
		# 現在の行のリージョンを取得します。
		curr_region = self.view.line(curr_pos)
		# 現在の行の内容（文字列）を取得します。
		curr_line_str = self.view.substr(curr_region)

		if match_doc_type_series(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_html(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_jsf_two_word(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if html.match_link_javascript(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if html.match_link_style(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_list(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_meta_utf(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_no_cache(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_put_html_series(self, edit, curr_pos, curr_region, curr_line_str):
			return True
		if match_property(self, edit, curr_pos, curr_region, curr_line_str):
			return True



