from unittest import TestCase, main


class BaseTest(TestCase):

    basic_bits = {
        '1': (
            (0,),
            (1,),
        ),
        '2': (
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
        ),
        '3': (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ),
        '4': (
            (0, 0, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
            (0, 0, 1, 1),
            (0, 1, 0, 0),
            (0, 1, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 1, 1),
            (1, 0, 0, 0),
            (1, 0, 0, 1),
            (1, 0, 1, 0),
            (1, 0, 1, 1),
            (1, 1, 0, 0),
            (1, 1, 0, 1),
            (1, 1, 1, 0),
            (1, 1, 1, 1),
        ),
        '16b1': (
            ((1,) * 16,),
            ((0,) * 16,),
        ),
        '16b2': (
            ((0,) * 16, (0,) * 16),
            ((0,) * 16, (1,) * 16),
            ((1,) * 16, (0,) * 16),
            ((1,) * 16, (1,) * 16),
        ),
        '16b3': (
            ((0,) * 16, (0,) * 16, (0,) * 16),
            ((0,) * 16, (0,) * 16, (1,) * 16),
            ((0,) * 16, (1,) * 16, (0,) * 16),
            ((0,) * 16, (1,) * 16, (1,) * 16),

            ((1,) * 16, (0,) * 16, (0,) * 16),
            ((1,) * 16, (0,) * 16, (1,) * 16),
            ((1,) * 16, (1,) * 16, (0,) * 16),
            ((1,) * 16, (1,) * 16, (1,) * 16),
        ),
        '16b4': (
            ((0,) * 16, (0,) * 16, (0,) * 16, (0,) * 16),
            ((0,) * 16, (0,) * 16, (0,) * 16, (1,) * 16),
            ((0,) * 16, (0,) * 16, (1,) * 16, (0,) * 16),
            ((0,) * 16, (0,) * 16, (1,) * 16, (1,) * 16),
            ((0,) * 16, (1,) * 16, (0,) * 16, (0,) * 16),
            ((0,) * 16, (1,) * 16, (0,) * 16, (1,) * 16),
            ((0,) * 16, (1,) * 16, (1,) * 16, (0,) * 16),
            ((0,) * 16, (1,) * 16, (1,) * 16, (1,) * 16),

            ((1,) * 16, (0,) * 16, (0,) * 16, (0,) * 16),
            ((1,) * 16, (0,) * 16, (0,) * 16, (1,) * 16),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16),
            ((1,) * 16, (0,) * 16, (1,) * 16, (1,) * 16),
            ((1,) * 16, (1,) * 16, (0,) * 16, (0,) * 16),
            ((1,) * 16, (1,) * 16, (0,) * 16, (1,) * 16),
            ((1,) * 16, (1,) * 16, (1,) * 16, (0,) * 16),
            ((1,) * 16, (1,) * 16, (1,) * 16, (1,) * 16),
        ),
        # 4 bit の真理値表 0000 〜 1111 の左に 1 bit 追加するためのデータセット
        '1r4': (
            (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,),
            (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,),

            (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,),
            (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,),
        ),
        '2r4': (
            (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
            (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),

            (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
            (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),

            (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0),
            (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0), (1, 0),

            (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
            (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
        )

    }

    def tuple_join(self, a, b):
        """
        2 つの tuple として a, b を引数で受け取り、結合した結果を戻り値とする。
        e.g.)
         引数
          a = ((1, 1, 1), (2, 2, 2))
          b = (3, 4)
         戻り値
          ((1, 1, 1, 3), (2, 2, 2, 4))
        """
        return tuple((*x, y) for x, y in (tuple(zip(a, b))))

    def exec(self, f, inputs, expected):
        for i, e in zip(*(inputs, expected)):
            with self.subTest(input=input, expected=expected):
                actual = f(*i)
                self.assertEqual(*e, actual)
