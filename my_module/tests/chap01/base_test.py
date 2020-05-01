from unittest import TestCase, main


class BaseTest(TestCase):

    basic_bits = {
        '1': (
            0,
            1,
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

    }

    basic2bits = (

    )

    def exec(self, f, inputs, expected):
        for i, e in zip(*(inputs, expected)):
            with self.subTest(input=input, expected=expected):

                if isinstance(i, tuple):
                    actual = f(*i)
                else:
                    actual = f(i)

                self.assertEqual(e, actual)
