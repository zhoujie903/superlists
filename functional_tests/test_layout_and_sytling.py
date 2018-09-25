from .base import FunctionalTest
from unittest import skip


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 伊 迪 丝 访 问 首 页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)


        inputbox = self.get_item_input_box()
        # self.assertAlmostEqual(
        #     inputbox.location['x'] + inputbox.size['width'] / 2,
        #     512,
        #     delta=5
        # )

        # 她 新 建 了 一 个 清 单， 看 到 输 入 框 仍 完 美 地 居 中 显 示
        inputbox.send_keys('testings\n')
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertAlmostEqual(
        #     inputbox.location['x'] + inputbox.size['width'] / 2,
        #     512,
        #     delta=5
        # )


