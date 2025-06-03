#!/usr/bin/env python3
"""
models/sabdirclass.py

Help docstring
"""
import datetime
import os
import argparse
import sys
# sys.path.insert('.')
# import localuserpylib.pydates.localpydates as lpd # module where gen_last_n_monday_dates_from_today() resides


def list_help_n_exit():
  """

  :return:
  """
  print(__doc__)
  sys.exit(0)


parser = argparse.ArgumentParser(description="Walk a dirtree to find SabDir course dates.")
parser.add_argument("--rootdir", type=str, default=None,
                    help="Directory from which to walk up directory to find SabDir course dates")
parser.add_argument("--nlist", type=int, default=50,
                    help="number of courses to list in descending alphabetical order")
args = parser.parse_args()


class SabDirCourse:

  zinfofilename = "z-info.txt"

  def __init__(
      self, coursename: str, coursedate: datetime.date = None,
      instructor_fullname: str = None, instructor: str = None, n_lecture: int = 5
    ):
    self.coursename = coursename
    self.coursedate = coursedate
    self.instructor_fullname = instructor_fullname
    self._instructor = instructor
    self.n_lectures = n_lecture

  @property
  def instructor(self):
    if self._instructor is not None:
      return self._instructor
    if self.instructor_fullname is None:
      return 's/inf'
    pp = self.instructor_fullname.split(' ')
    first_n_last = pp[0] + ' ' + pp[-1]
    return first_n_last

  def create_zinfofile_if_not_exists(self, courses_folderpath):
    text = f"{self.coursename} _i {self.instructor}\n"
    text += f"fullname: s/inf"
    text += f"female: s/inf"
    text += f"{self.coursedate}"
    filepath = os.path.join(courses_folderpath, self.zinfofilename)
    if os.path.exists(filepath):
      return False
    fd = open(filepath, 'w')
    fd.write(text)
    fd.close()
    return False

  def __str__(self):
    outstr = f"{self.coursedate} | {self.coursename} | {self.instructor}"
    return outstr


def get_cli_args():
  """
  """
  pass


def adhoc_test():
  """
  """
  today = datetime.date.today()
  sabdir = SabDirCourse('Direitos Humandos', today, None, 'José João', 5)
  print(sabdir)


def process():
  pass


if __name__ == '__main__':
  """
  """
  process()
  adhoc_test()
