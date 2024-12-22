# write a python program to fill in a letter template given brlow with name and date.
""" letter = '''
  Dear <|Name|>
  you are selected!
  <|Date|>
  '''
"""
letter = '''Dear <|Name|>
  you are selected!
  <|Date|>
  '''
print(letter.replace("<|Name|>","Rahul").replace("<|Date|>","1 jan 2025"))