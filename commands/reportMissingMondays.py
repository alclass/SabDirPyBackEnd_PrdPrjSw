#!/usr/bin/env python3
"""

"""
import copy


def report_missing_mondays_in_sabdircourses(self):
  courses_copied = copy.copy(self.courses)
  courses_copied.sort(key=lambda course: course.coursedate, reverse=True)
  # now the last course in a list (courses_copied) is the oldest in date
  nelems = len(courses_copied)
  oldest_course = courses_copied[nelems-1]
  oldest_coursedate = oldest_course.coursedate
  for pdate in lpd.gen_all_mondays_inbetweenfrom(oldest_coursedate, ascending_order=False):
    sabdircourse = self.find_course_on_date(pdate)
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
    print(i, sdate)


def process():
  pass


if __name__ == '__main__':
  """
  adhoc_test()
  """
  process()
