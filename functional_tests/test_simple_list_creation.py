from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get(self.server_url)

        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 她 在 一 个 文 本 框 中 输 入 了“ Buy peacock feathers”（ 购 买 孔 雀 羽 毛）
        # 伊 迪 丝 的 爱 好 是 使 用 假 蝇 做 饵 钓 鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她 按 回 车 键 后， 被 带 到 了 一 个 新 URL 
        # # 这 个 页 面 的 待 办 事 项 清 单 中 显 示 了“ 1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # # 她 按 回 车 键 后， 页 面 更 新 了
        # # 待 办 事 项 表 格 中 显 示 了“ 1: Buy peacock feathers”
        # inputbox.send_keys(Keys.ENTER)
        # self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页 面 中 又 显 示 了 一 个 文 本 框， 可 以 输 入 其 他 的 待 办 事 项
        # 她 输 入 了“ Use peacock feathers to make a fly”（ 使 用 孔 雀 羽 毛 做 假 蝇）
        # 伊 迪 丝 做 事 很 有 条 理
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 现 在 一 个 叫 作 弗 朗 西 斯 的 新 用 户 访 问 了 网 站 

        # 我 们 使 用 一 个 新 浏 览 器 会 话 
        # 确 保 伊 迪 丝 的 信 息 不 会 从 cookie 中 泄 露 出 来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗 朗 西 斯 访 问 首 页 
        # 页 面 中 看 不 到 伊 迪 丝 的 清 单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # 弗 朗 西 斯 输 入 一 个 新 待 办 事 项， 新 建 一 个 清 单
        # 他 不 像 伊 迪 丝 那 样 兴 趣 盎 然   
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 弗 朗 西 斯 获 得 了 他 的 唯 一 URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 这 个 页 面 还 是 没 有 伊 迪 丝 的 清 单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # # 伊 迪 丝 想 知 道 这 个 网 站 是 否 会 记 住 她 的 清 单
        # # 她 看 到 网 站 为 她 生 成 了 一 个 唯 一 的 URL 
        # # 而 且 页 面 中 有 一 些 文 字 解 说 这 个 功 能
        # self.fail('Finish the test!')

        # 应用邀请她一个待办事项
