#!/usr/bin/env python3
"""
models/sabdirclass.py
  This module contains class SabDirCourse which models a Saber Direito Course.

Its attributes (at the moment of this writing) are:

    self.coursename => the course's title
    self.coursedate = the course's initial date
    self.coursedirpath = the course dirpath that depends on the mount path, but useful for deriving knowledge areas
    self.rootdir_abspath = the rootpath to the course repository, useful as above
    self._knowledgearea_path = the knowledge areas string from main topic to subtopics
    self.knowledgeareas = same as above but as a list
    self.instructor_fullname = instructor's fullname
    self._instructor = instructor's first and last name (when Jr, Neto etc happen, they are sufix)
    self.n_lectures = number of lectures in the course (usually 5)

"""
import datetime
import os
import argparse
import sys
from os.path import relpath


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
      instructor_fullname: str = None, instructor: str = None, n_lecture: int = 5,
      coursedirpath: os.path = None, rootdir_abspath: os.path = None
    ):
    self.coursename = coursename
    self.coursedate = coursedate
    self.coursedirpath = coursedirpath
    self.rootdir_abspath = rootdir_abspath
    self._knowledgearea_path = None
    self.knowledgeareas = []
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

  def recup_knowledgeareas_by_after_rootdir(self):
    relativepath = self.coursedirpath[len(self.rootdir_abspath):]
    return relativepath.split('/')

  @property
  def knowledgearea_path(self):
    if self._knowledgearea_path is not None:
      return self._knowledgearea_path
    if self.knowledgeareas is None or len(self.knowledgeareas) == 0:
      if self.rootdir_abspath is None:
        return None
      else:
        self.knowledgeareas = self.recup_knowledgeareas_by_after_rootdir()
    self._knowledgearea_path = '/'.join(self.knowledgeareas)
    return self._knowledgearea_path

  def descr(self):
    outstr = f"{self.coursedate} | {self.coursename} | {self.instructor}"
    outstr += f"{self.coursedirpath}"
    outstr += f"{self.rootdir_abspath}"
    outstr += f"{self.knowledgearea_path}"
    return outstr

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
