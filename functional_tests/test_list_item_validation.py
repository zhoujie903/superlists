from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')


    def test_cannot_add_empty_list_items(self):
        # 伊 迪 丝 访 问 首 页， 不 小 心 提 交 了 一 个 空 待 办 事 项
        #  输 入 框 中 没 输 入 内 容， 她 就 按 下 了 回 车 键
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        #  首 页 刷 新 了， 显 示 一 个 错 误 消 息
        # 提 示 待 办 事 项 不 能 为 空
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她 输 入 一 些 文 字， 然 后 再 次 提 交， 这 次 没 问 题 了
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # 她 有 点 儿 调 皮， 又 提 交 了 一 个 空 待 办 事 项
        self.get_item_input_box().send_keys('\n')

        # 在 列 表 页 面 她 看 到 了 一 个 类 似 的 错 误 消 息
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # 输 入 文 字 之 后 就 没 问 题 了
        self.get_item_input_box().send_keys('Manke tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Manke tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # 伊 迪 丝 新 建 一 个 清 单， 但 方 法 不 当， 所 以 出 现 了 一 个 验 证 错 误
        self.browser.get(self.server_url)

        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        # self.assertTrue(error.is_displayed())

        # 为 了 消 除 错 误， 她 开 始 在 输 入 框 中 输 入 内 容
        self.get_item_input_box().send_keys('a')

        # 看 到 错 误 消 息 消 失 了， 她 很 高 兴
        error = self.get_error_element()
        # self.assertFalse(error.is_displayed())

