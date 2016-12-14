#!/usr/bin/env python3

import subprocess
import unittest


def compile(prog):
    prog_bytes = bytes(prog, encoding='utf-8')
    proc = subprocess.run(['./bin/zappac', '--parse'], input=prog_bytes, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    return {
        'ok': proc.returncode == 0,
        'returncode': proc.returncode,
        'parse_error': b'parse error' in proc.stderr,
        'tokens': proc.stdout.split(b'\n')[:-1]
    }


class ParseTests(unittest.TestCase):
    def assert_parse_tokens(self, prog, expected_tokens):
        result = compile(prog)
        self.assertTrue(result['ok'])
        self.assertEqual(result['tokens'], expected_tokens)

    def assert_parse_error(self, prog):
        result = compile(prog)
        self.assertFalse(result['ok'])
        self.assertTrue(result['parse_error'])

    def test_indentation(self):
        expected_tokens = [b'identifier: main', b'eq', b'identifier: print',
                           b'string: Hello World!']

        good_prog_1 = '''main = print 'Hello World!'\n'''
        self.assert_parse_tokens(good_prog_1, expected_tokens)

        good_prog_2 = '''main =\n  print 'Hello World!'\n'''
        self.assert_parse_tokens(good_prog_2, expected_tokens)

        bad_prog_1 = '''main = '''
        self.assert_parse_error(bad_prog_1)

        bad_prog_2 = '''main =\nprint 'Hello World!'\n'''
        self.assert_parse_error(bad_prog_2)

        bad_prog_3 = '''main =\n\tprint 'Hello World!'\n'''
        self.assert_parse_error(bad_prog_3)

        bad_prog_4 = '''main =\n    print 'Hello World!'\n'''
        self.assert_parse_error(bad_prog_4)

        bad_prog_5 = '''  main =\n  print 'Hello World!'\n'''
        self.assert_parse_error(bad_prog_5)


if __name__ == '__main__':
    unittest.main()
