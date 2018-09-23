from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # 伊 迪 丝 访 问 首 页， 不 小 心 提 交 了 一 个 空 待 办 事 项
        #  输 入 框 中 没 输 入 内 容， 她 就 按 下 了 回 车 键
        #  首 页 刷 新 了， 显 示 一 个 错 误 消 息
        # 提 示 待 办 事 项 不 能 为 空 # 她 输 入 一 些 文 字， 然 后 再 次 提 交， 这 次 没 问 题 了
        #  她 有 点 儿 调 皮， 又 提 交 了 一 个 空 待 办 事 项
        #  在 清 单 页 面 她 看 到 了 一 个 类 似 的 错 误 消 息

        #  输 入 文 字 之 后 就 没 问 题 了
        self.fail('write me!')

