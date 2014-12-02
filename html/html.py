import sublime, sublime_plugin, re

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

	pattern = r"\s*link\s+style\s+(.*)"
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

	pattern = r"\s*link\s+javascript\s+(.*)"
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


