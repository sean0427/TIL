def create_prefix_table(pattern):
  table = [0]*len(pattern)

  prev = 0
  i = 1

  while i < len(pattern):
    if pattern[i] == pattern[prev]:
      table[i] = prev + 1
      i += 1
      prev += 1
    elif prev == 0:
      table[i] = 0
      i += 1
    else:
      prev = table[prev - 1]

  return table

def findPattern(s, pattern, prefix_table):
  i = 0
  j = 0

  while i < len(s):
    if (s[i] == pattern[j]):
      i += 1
      j += 1
    else:
      if j == 0:
        i += 1
      else:
        j = prefix_table[j-1]

    
    if j == len(prefix_table):
      return i - len(prefix_table)
  
  return -1



def kmp(text, pattern):
  table = create_prefix_table(TEST_DATA)
  idx = findPattern(TEST_DATA_STR, TEST_DATA, table)

  print(table)
  print(idx)
  if idx != -1:
    print(TEST_DATA == TEST_DATA_STR[idx:idx+len(TEST_DATA)])
    assert TEST_DATA == TEST_DATA_STR[idx:idx+len(TEST_DATA)]
  

if __name__ == '__main__':
  TEST_DATA_STR = 'feaifhioeahfi;oejwai;ofja;owfjefawur90uew90arjpewrfaabbacsaw90urf90wrjowajfe'
  TEST_DATA_PATTERN = 'aabbacsa'

  kmp(TEST_DATA_STR, TEST_DATA_PATTERN)
