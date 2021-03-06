import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from .bash_runner import *

from timeit import default_timer as timer


class TestRunAsBash(unittest.TestCase):

    # python3 -m unittest svet.bash_runner_test

    def test_good_command_code_zero(self):
        bash_lines = [
            f'set -e',
            f"ls"]
        code = run_as_bash_script("\n".join(bash_lines))
        self.assertEqual(code.returncode, 0)  # ok

    def test_bad_command_error_code(self):
        bash_lines = [
            f'set -e',
            f"ok_computer_make_me_happy"]
        code = run_as_bash_script("\n".join(bash_lines))
        self.assertEqual(code.returncode, 127)  # error

    def test_alias_expansion(self):
        with TemporaryDirectory() as td:
            file_to_create = Path(td) / "to_be_or_not_to_be.txt"
            file_to_create_quoted = repr(str(file_to_create))
            bash_lines = [
                f'set -e',
                f"shopt -s expand_aliases",
                f'alias ohoho="echo"',  # this will work in bash, but not in sh
                f'ohoho "that is the answer" > {file_to_create_quoted}']
            self.assertFalse(file_to_create.exists())
            code = run_as_bash_script("\n".join(bash_lines))
            self.assertEqual(code.returncode, 0)
            self.assertTrue(file_to_create.exists())
            self.assertEqual(file_to_create.read_text().strip(), "that is the answer")

    #def test_timeout(self):
        #start = timer()
        #end = timer()
        #with self.assertRaises(subprocess.TimeoutExpired):
         #   run_as_bash_script("python", timeout=1)
        #self.assertGreater(end-start, 0.9)


