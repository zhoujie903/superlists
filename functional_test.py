from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

def main():
    unittest.main(warnings='ignore')

if __name__ == '__main__':
    main()
# 应用邀请她一个待办事项

# 她 在 一 个 文 本 框 中 输 入 了“ Buy peacock feathers”（ 购 买 孔 雀 羽 毛）
# 伊 迪 丝 的 爱 好 是 使 用 假 蝇 做 饵 钓 鱼 # 她 按 回 车 键 后， 页 面 更 新 了
# 待 办 事 项 表 格 中 显 示 了“ 1: Buy peacock feathers”
# 页 面 中 又 显 示 了 一 个 文 本 框， 可 以 输 入 其 他 的 待 办 事 项 # 她 输 入 了“ Use peacock feathers to make a fly”（ 使 用 孔 雀 羽 毛 做 假 蝇）
# 伊 迪 丝 做 事 很 有 条 理 # 页 面 再 次 更 新， 她 的 清 单 中 显 示 了 这 两 个 待 办 事 项
# 伊 迪 丝 想 知 道 这 个 网 站 是 否 会 记 住 她 的 清 单
# 她 看 到 网 站 为 她 生 成 了 一 个 唯 一 的 URL
# 而 且 页 面 中 有 一 些 文 字 解 说 这 个 功 能
# 她 访 问 那 个 URL， 发 现 她 的 待 办 事 项 列 表 还 在 # 她 很 满 意， 去 睡 觉 了
