#!/usr/bin/python
from test import load_code_segment
from style_grader_functions import *
from StyleRubric import *
import unittest

class RegressionTesting(unittest.TestCase):
    styleRubric = StyleRubric()

    @load_code_segment('good.cpp')
    def test_good_file(self): self.assertTrue(not len(self.rubric.error_types))
    @load_code_segment('num_of_commands.cpp')
    def test_statements_per_line(self): self.assertEqual(self.rubric.error_types['STATEMENTS_PER_LINE'], 3)
    @load_code_segment('test_valid_return.cpp')
    def test_int_for_bool(self): self.assertEqual(self.rubric.error_types['INT_FOR_BOOL'], 2)
    #@load_code_segment('if_else_good.cpp')
    #def test_good_if_else(self): self.assertEqual(0, self.rubric.error_types['IF_ELSE_ERROR'])
    #@load_code_segment('if_else_bad.cpp')
    #def test_bad_if_else(self): self.assertEqual(3, self.rubric.error_types['IF_ELSE_ERROR'])
    @load_code_segment('equals_true.cpp')
    def test_equals_true(self): self.assertEqual(5, self.rubric.error_types['EQUALS_TRUE'])
    @load_code_segment('function_def_above_main_good.cpp')
    def test_def_above_main_good(self): self.assertEqual(0, self.rubric.error_types['DEFINITION_ABOVE_MAIN'])
    @load_code_segment('function_def_above_main_bad.cpp')
    def test_def_above_main_bad(self): self.assertEqual(5, self.rubric.error_types['DEFINITION_ABOVE_MAIN'])
    @load_code_segment('goto_good.cpp')
    def test_goto_good(self): self.assertEqual(0, self.rubric.error_types['GOTO'])
    @load_code_segment('goto_bad.cpp')
    def test_goto_bad(self): self.assertEqual(3, self.rubric.error_types['GOTO'])
    @load_code_segment('continue_good.cpp')
    def test_continue_good(self): self.assertEqual(0, self.rubric.error_types['CONTINUE_STATEMENT'])
    @load_code_segment('continue_bad.cpp')
    def test_continue_bad(self): self.assertEqual(4, self.rubric.error_types['CONTINUE_STATEMENT'])
    @load_code_segment('define_good.cpp')
    def test_define_good(self): self.assertEqual(0, self.rubric.error_types['DEFINE_STATEMENT'])
    @load_code_segment('define_bad.cpp')
    def test_define_bad(self): self.assertEqual(2, self.rubric.error_types['DEFINE_STATEMENT'])
    @load_code_segment('ternary_good.cpp')
    def test_ternary_good(self): self.assertEqual(0, self.rubric.error_types['TERNARY_OPERATOR'])

    @load_code_segment('ternary_bad.cpp')
    def test_ternary_bad(self):
        self.assertEqual(\
            3 if self.styleRubric.config.get('SINGLE_LINE_CHECKS', 'ternary_operator') == 'yes' else 0,\
            self.rubric.error_types['TERNARY_OPERATOR'])

    @load_code_segment('while_true_good.cpp')
    def test_while_true_good(self): self.assertEqual(0, self.rubric.error_types['WHILE_TRUE'])
    @load_code_segment('while_true_bad.cpp')
    def test_while_true_bad(self): self.assertEqual(3, self.rubric.error_types['WHILE_TRUE'])
    #@load_code_segment('global_good.cpp')
    #def test_global_good(self): self.assertEqual(0, self.rubric.error_types['NON_CONST_GLOBAL'])
    #@load_code_segment('global_bad.cpp')
    #def test_global_bad(self): self.assertEqual(3, self.rubric.error_types['NON_CONST_GLOBAL'])
    @load_code_segment('main_good.cpp')
    def test_main_good(self): self.assertEqual(0, self.rubric.error_types['MAIN_SYNTAX'])
    @load_code_segment('main_bad.cpp')
    def test_main_bad(self): self.assertEqual(2, self.rubric.error_types['MAIN_SYNTAX'])
    @load_code_segment('first_char_good.cpp')
    def test_first_char_good(self): self.assertEqual(0, self.rubric.error_types['FIRST_CHAR'])
    @load_code_segment('first_char_bad.cpp')
    def test_first_char_bad(self): self.assertEqual(6, self.rubric.error_types['FIRST_CHAR'])
    @load_code_segment('semicolon_spacing_good1.cpp')
    def test_semicolon_spacing_good1(self): self.assertEqual(0, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])
    @load_code_segment('semicolon_spacing_good2.cpp')
    def test_semicolon_spacing_good2(self): self.assertEqual(0, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])
    @load_code_segment('semicolon_spacing_bad.cpp')
    def test_semicolon_spacing_bad(self): self.assertEqual(4, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])

    @load_code_segment('logical_AND_OR_spacing_bad.cpp')
    def test_bad_logical_spacing(self): self.assertEqual(3, self.rubric.error_types['OPERATOR_SPACING'])
    @load_code_segment('logical_AND_OR_spacing_good.cpp')
    def test_good_logical_spacing(self): self.assertEqual(0, self.rubric.error_types['OPERATOR_SPACING'])
    @load_code_segment('operator_spacing_bad.cpp')
    def test_bad_operator_spacing(self): self.assertEqual(23, self.rubric.error_types['OPERATOR_SPACING'])
    @load_code_segment('operator_spacing_good.cpp')
    def test_good_operator_spacing(self): self.assertEqual(0, self.rubric.error_types['OPERATOR_SPACING'])

    @load_code_segment('func_def_no_main.cpp')
    def test_func_def_no_main(self): self.assertEqual(0, self.rubric.error_types['DEFINITION_ABOVE_MAIN'])

    @load_code_segment('indent_conditional.cpp')
    def test_simple_conditional_indent(self): self.assertEqual(4, self.rubric.error_types['BLOCK_INDENTATION'])
    @load_code_segment('indent_switch.cpp')
    def test_simple_switch_indent(self): self.assertEqual(8, self.rubric.error_types['BLOCK_INDENTATION'])
    @load_code_segment('indent_classes.h')
    def test_class_indentation_header(self): self.assertEqual(11, self.rubric.error_types['BLOCK_INDENTATION'])
    @load_code_segment('indent_structs.h')
    def test_struct_indentation_header(self): self.assertEqual(11, self.rubric.error_types['BLOCK_INDENTATION'])

    # Test for too long lines based on the setting in the config (valid for line lengths that are multiples of 10 between 30 and 120)
    @load_code_segment('long_lines.cpp')
    def test_check_line_width(self):
        self.assertEqual(26 - int(self.styleRubric.max_line_length / 5), self.rubric.error_types['LINE_WIDTH'])

    @load_code_segment('brace_consistancy_allman_good.cpp')
    def test_brace_consistancy_allman_good(self): self.assertEqual(0, self.rubric.error_types['BRACE_CONSISTENCY'])
    @load_code_segment('brace_consistancy_stroustrup_good.cpp')
    def test_brace_consistancy_stroustrup_good(self): self.assertEqual(0, self.rubric.error_types['BRACE_CONSISTENCY'])
    @load_code_segment('brace_consistancy_bad.cpp')
    def test_brace_consistancy_stroustrup_good(self): self.assertEqual(1, self.rubric.error_types['BRACE_CONSISTENCY'])


    @load_code_segment('regression_indentation_group.cpp')
    def test_regression_indentation_group(self):
        # The input file will throw an error if there's a bug, so we don't
        # actually need to test for anything.
        pass
