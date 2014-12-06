import sublime, sublime_plugin, re

############################################################################
# no cache 構文を取得します。
############################################################################
def get_no_cache():
	save = "\t<meta http-equiv=\"pragma\"        content=\"no-cache\">\n" +\
		"\t<meta http-equiv=\"cache-control\" content=\"no-cache\">\n" +\
		"\t<meta http-equiv=\"Expires\"       content=\"0\">\n"
	return save

############################################################################
# no cache にマッチします。
# (1) no cache
############################################################################
def match_no_cache(self, edit, \
	curr_pos, curr_region, curr_line_str):
	patternNoCache = r"\s*no\s+cache"
	matchNoCache = re.match(patternNoCache, curr_line_str)
	if matchNoCache:
		self.view.replace(edit, curr_region, get_no_cache())
		return True
	return False

############################################################################
# meta utf8 構文を取得します。
############################################################################
def get_meta_utf():
	save = "\t<meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\">"
	return save

############################################################################
# meta utf8 にマッチします。
# (1) meta utf8
############################################################################
def match_meta_utf(self, edit, \
	curr_pos, curr_region, curr_line_str):
	patternMeta = r"\s*meta utf"
	matchMeta = re.match(patternMeta, curr_line_str)
	if matchMeta:
		# temp_str = "<meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\">"
		self.view.replace(edit, curr_region, get_meta_utf())
		return True
	return False






############################################################################
# link style タグを取得します。
# css_base_path   CSS のベースパス
# stylesheet_name スタイルシート名
############################################################################
def get_link_style(css_base_path, stylesheet_name):
	if css_base_path is None:
		tmp = stylesheet_name
	else:
		tmp = css_base_path + "/" + stylesheet_name

	save = "\t<link rel=\"stylesheet\" type=\"text/css\" href=\"" + \
		tmp + ".css?v=0.1\" />"
	return save



############################################################################
# link style にマッチします。
# (1) link style ～
############################################################################
def match_link_style(self, edit, curr_pos, curr_region, curr_line_str):
	self.view.set_status("key1", "設定の取得")

	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	css_base_path = hapo_settings.get("css_base_path")

	pattern = r"\s*link\s+style\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		temp_str2 = get_link_style(css_base_path, temp_str)
		self.view.replace(edit, curr_region, temp_str2)
		return True

	pattern = r"\s*link\s+style"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str2 = get_link_style(css_base_path, "xxx")
		self.view.replace(edit, curr_region, temp_str2)
		return True

	return False



############################################################################
# link javascript タグを取得します。
# javascript_base_path   JavaScript のベースパス
# javascript_name        JavaScript 名
############################################################################
def get_link_javascript(javascript_base_path, javascript_name):
	if javascript_base_path is None:
		tmp = javascript_name
	else:
		tmp = javascript_base_path + "/" + javascript_name

	save = "\t<script type=\"text/javascript\" src=\"" + \
		tmp + ".js?v=0.1\"></script>"
	return save

############################################################################
# link javascript にマッチします。
# (1) link javascript ～
############################################################################
def match_link_javascript(self, edit, curr_pos, curr_region, curr_line_str):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	javascript_base_path = hapo_settings.get("javascript_base_path")

	pattern = r"\s*link\s+javascript\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		temp_str2 = get_link_javascript(javascript_base_path, temp_str)
		self.view.replace(edit, curr_region, temp_str2)
		return True

	pattern = r"\s*link\s+javascript"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = "xxx"
		temp_str2 = get_link_javascript(javascript_base_path, temp_str)
		self.view.replace(edit, curr_region, temp_str2)
		return True

	return False



############################################################################
# html4 と html5 にマッチします。
# (1) html4
# (2) html5
############################################################################
def match_html(self, edit, curr_pos, curr_region, curr_line_str):
	# 設定を取得します。
	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
	css_base_path = hapo_settings.get("css_base_path")

	self.view.set_status("key3", "HTMLのマッチロジック")

	pattern = r"html([45])"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		temp_str = matchOB.group(1)
		if temp_str == "4":
			self.view.set_status("key4", "HTML4だよねねね")
			temp_str2 = \
				"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">\n" +\
				"<html lang=\"ja\">\n" +\
				"<head>\n" +\
				"\t" + get_meta_utf() + "\n" +\
				get_no_cache() +\
				get_link_style(css_base_path, "xxx") + "\n" +\
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



############################################################################
# 下記にマッチします。
# (1) put css
# (2) put javascript
# (3) put javascript html5
############################################################################
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

############################################################################
# doctype 系にマッチします。
# (1) doctype4
# (2) doctype4 frame
# (3) doctype4 strict
############################################################################
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


############################################################################
# list にマッチします。
# (1) list ～
############################################################################
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

# ############################################################################
# # link javascript にマッチします。
# # (1) link javascript ～
# ############################################################################
# def match_link_javascript(self, edit, curr_pos, curr_region, curr_line_str):
# 	# 設定を取得します。
# 	hapo_settings = sublime.load_settings("HapoItak.sublime-settings")
# 	javascript_base_path = hapo_settings.get("javascript_base_path")

# 	pattern = r"\s*link\s+javascript\s+(.*)"
# 	matchOB = re.match(pattern, curr_line_str)
# 	if matchOB:
# 		temp_str = matchOB.group(1)
# 		if javascript_base_path is not None:
# 			temp_str = javascript_base_path + "/" + temp_str
# 		temp_str2 = "\t<script type=\"text/javascript\" src=\"" + \
# 			temp_str + ".js?v=0.1\"></script>"
# 		self.view.replace(edit, curr_region, temp_str2)
# 		return True
# 	return False
