#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 成绩转换为等级
#   - >= 90: A
#   - >= 80: B
#   - >= 70: C
#   - >= 60: D
#   - < 60: E

def score_to_level(score):
  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'E'

score = int(input('请输入成绩: '))
print('对应的等级是: ', score_to_level(score))