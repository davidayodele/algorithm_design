import textwrap

def solution(s):
  s_len = len(s)
  cuts = 1
  match = False
  slice_size = s_len / cuts
  #print(s_len)
  #print(slice_size)
  #print(s_len / cuts)

  parts = []
  # (s_len / cuts) < 200
  # sub_s = textwrap.wrap(s, cuts)
  # sub_s = [s[i:i + cuts] for i in range(0, len(s), cuts)]
  # print(sub_s)
  

  while match == False and cuts >= 1 and slice_size <= 200:
    parts = [s[i:i + cuts] for i in range(0, s_len, cuts)]
    first = parts[0]

    for item in parts:
      if item == first:
        match = True
      else:
          match = False
          break

    cuts += 1
  print(len(parts))
  
  #print(sub_s)
  #print(slice_size)
  #print(cuts)


solution("abcabcabcabc")
