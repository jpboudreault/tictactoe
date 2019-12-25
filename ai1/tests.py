from django.test import SimpleTestCase


class Ai1ServiceTest(SimpleTestCase):
    # Tests that the service can block on the first line
    def test_block_line(self):
        inputs = [
            ['x', 'x', ' '],
            ['o', ' ', ' '],
            ['o', ' ', ' '],
        ]

       # move = Ai1Service.play(inputs)
       # self.assertEqual()
