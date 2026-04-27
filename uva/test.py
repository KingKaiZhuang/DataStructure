spots = set()
history = set()

# 第一步：放 (1, 1)
spots.add((1, 1))
history.add(spots)

# 第二步：放 (2, 2)
spots.add((2, 2))
history.add(spots)

# 第三步：移除 (2, 2)
spots.remove((2, 2))

if spots in history:
    print("重複了")
else:
    print("沒重複")