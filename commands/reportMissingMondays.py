#!/usr/bin/env python3
"""
commands/reportMissingMondays.py

Help docstring

"""
import copy
import os
import sys
import argparse
from models import sabdirclass
from commands import sabdirOSWalkerMod as walkermod
home_dir = os.path.expanduser("~")
bin_dir = os.path.join(home_dir, 'bin')
sys.path.insert(0, bin_dir)
import localuserpylib.pydates.localpydates as lpd  # module where gen_last_n_monday_dates_from_today() resides


parser = argparse.ArgumentParser(description="Walk a dirtree to find SabDir course dates.")
parser.add_argument("--rootdir", type=str, default=None,
                    help="Directory from which to walk up directory to find SabDir course dates")
parser.add_argument("--nlist", type=int, default=50,
                    help="number of courses to list in descending alphabetical order")
# parser.add_argument("--help", action=list_help_n_exit,
#                     help="print help and exist")
args = parser.parse_args()


def report_missing_mondays_in_sabdircourses(rootdir_abspath):
  grabber = walkermod.SabDirCourseOSWalkGrabber(rootdir_abspath=rootdir_abspath)
  first_course_in_date = grabber.first_course_in_date
  for pdate in lpd.gen_all_mondays_inbetweenfrom(first_course_in_date, ascending_order=False):
    sabdircourse = grabber.find_course_on_date(pdate)
    if sabdircourse:
      scrmsg = f"The is a course on {pdate} | {sabdircourse}"
      print(scrmsg)
    else:
      scrmsg = f"The is NOT a course on {pdate}"
      print(scrmsg)


def adhoc_test():
  """
  Example for an adhoc test:
    --rootdir="/home/dados/VideoAudio/Soc vi/Law vi/BRA Dir vi/Sab Dir vi/completed Sab Dir ytvi"
  """
  for i, sdate in enumerate(lpd.gen_last_n_monday_dates_from_today()):
    seq = i + 1
    print(seq, sdate)


def process():
  rootdir_abspath = args.rootdir
  report_missing_mondays_in_sabdircourses(rootdir_abspath)
  pass


if __name__ == '__main__':
  """
  """
  process()
  adhoc_test()
