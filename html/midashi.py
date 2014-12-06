import sublime, sublime_plugin, re

from ..util import sublime_view_util

############################################################################
# 見出しにマッチします。
############################################################################
def match_midashi(self, edit, curr_pos, curr_region, curr_line_str):
	# self.view.set_status("key1", "見出しにマッチ")
	if match_midashi_1(self, edit, curr_pos, curr_region, curr_line_str):
		return True
	if match_midashi_2(self, edit, curr_pos, curr_region, curr_line_str):
		return True
	if match_midashi_3(self, edit, curr_pos, curr_region, curr_line_str):
		return True
	return False


############################################################################
# 見出しの class 属性部を取得します。
############################################################################
def get_class_attr(self, h_level):
	# self.view.set_status("key5", "get_class_attrだよ")

	temp_str3 = sublime_view_util.get_h_default_class(self, h_level)
	if temp_str3 != "":
		temp_str3 = " class=\"" + temp_str3 + "\""

	# self.view.set_status("key6", "temp_str3 = " + temp_str3)

	return temp_str3

############################################################################
# 見出しにマッチします。
# (1) h1 数字
# (2) h2 数字
# (3) h3 数字
# (4) h4 数字
# (5) h5 数字
# (6) h6 数字
############################################################################
def match_midashi_1(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*h([1-6])\s+([1-9][0-9]*)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		h_level_str = matchOB.group(1)
		h_level     = int(h_level_str)
		h_max_count = int(matchOB.group(2))

		temp_str3 = get_class_attr(self, h_level)
		temp_str2 = "<h" + h_level_str + temp_str3 + "></h" + h_level_str + ">\n"

		temp_str4 = ""
		i = 0
		while i < h_max_count:
			temp_str4 = temp_str4 + temp_str2
			i = i + 1

		self.view.replace(edit, curr_region, temp_str4)
		return True
	return False


############################################################################
# 見出しにマッチします。
# (1) h1 文字列
# (2) h2 文字列
# (3) h3 文字列
# (4) h4 文字列
# (5) h5 文字列
# (6) h6 文字列
############################################################################
def match_midashi_2(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*h([1-6])\s+(.+)"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		h_level_str = matchOB.group(1)
		h_level     = int(h_level_str)
		h_naiyo     = matchOB.group(2)

		temp_str3 = get_class_attr(self, h_level)
		temp_str2 = "<h" + h_level_str + temp_str3 + ">" + h_naiyo + "</h" + h_level_str + ">\n"

		self.view.replace(edit, curr_region, temp_str2)
		return True
	return False


############################################################################
# 見出しにマッチします。
# (1) h1
# (2) h2
# (3) h3
# (4) h4
# (5) h5
# (6) h6
############################################################################
def match_midashi_3(self, edit, curr_pos, curr_region, curr_line_str):
	pattern = r"\s*h([1-6])"
	matchOB = re.match(pattern, curr_line_str)
	if matchOB:
		h_level_str = matchOB.group(1)
		h_level     = int(h_level_str)

		temp_str3 = get_class_attr(self, h_level)
		temp_str2 = "<h" + h_level_str + temp_str3 + ">" + "</h" + h_level_str + ">\n"

		self.view.replace(edit, curr_region, temp_str2)
		return True
	return False











