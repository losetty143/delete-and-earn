#arr = [1,2,3]
def maxpoints(arr):
   arr.sort(reverse = True)
  maxpoints = 0
  for i in arr:
    if (arr.count(i)) >=2:
      maxpoints = maxpoints + (i * arr.count(i))
      high = i
      val1 = high - 1
      val2 = high + 1
      while i in arr: arr.remove(i)
      while val1 in arr: arr.remove(val1)
      while val2 in arr: arr.remove(val2)
      continue
      l = len(arr)
      if l > 1:
        if arr[0] == arr[1]:
          maxpoints = maxpoints + (l * arr[0])
          print(maxpoints)
          i = arr[0]
          while i in arr: arr.remove(i)

        else:
          high = max(arr)
          maxpoints = maxpoints + high
          val1 = high - 1
          val2 = high + 1
          while val1 in arr: arr.remove(val1)
          while val2 in arr: arr.remove(val2)
          while high in arr: arr.remove(high)

      else:
        print(maxpoints)
  l = len(arr)
  if (maxpoints > 0) and (l < 1) :
    print(maxpoints)
  l = len(arr)
  if l > 0:
    high = max(arr)
    maxpoints = maxpoints + high 
    arr.remove(high) 
    val1 = high - 1 
    val2 = high + 1 
    for val in arr:

        while val1 in arr: arr.remove(val1)
        while val2 in arr: arr.remove(val2)
        l = len(arr)
        if l > 0:
          high = max(arr) 
          maxpoints = maxpoints + high 
          arr.remove(high) 
          val1 = high - 1
          val2 = high + 1
          while val1 in arr: arr.remove(val1)
          while val2 in arr: arr.remove(val2)

    l = len(arr)
    while l > 1:
        high = max(arr)
        while high in arr: arr.remove(high)
        maxpoints = maxpoints + high
        val1 = high - 1 
        val2 = high + 1 
        while val1 in arr: arr.remove(val1)
        while val2 in arr: arr.remove(val2)
        l = len(arr)
    else:
      if len(arr) == 1:
        maxpoints = maxpoints + arr[0]
        print(maxpoints)
      else:
          print(maxpoints)
  else:
    pass
