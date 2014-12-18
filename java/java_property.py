import sublime, sublime_plugin, re

from ..util import string_util
from ..util import sublime_view_util


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
