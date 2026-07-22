t = int(input().strip())

for case_num in range(1, t + 1):
    # 題目規定：兩筆測試資料的輸出之間必須有一個空行
    if case_num > 1:
        print()
        
    prices = []
    # 改用 while 確保一定能安全讀滿 36 個數字 (防範測資亂斷行)
    while len(prices) < 36:
        prices += list(map(int, input().split()))
        
    # 印出第幾筆測資的標頭
    print(f"Case {case_num}:")
    
    test = int(input().strip())

    for _ in range(test):
        originalNum = int(input().strip())
        minN = 99999
        rec = []
        
        # split -> bases analyze -> competent max (min in this case)
        for i in range(2, 37):
            total = 0
            num = originalNum
            
            # 必須特別處理 0 的狀況
            if num == 0:
                total = prices[0]
            else:
                while num > 0:
                    tail = num % i
                    num //= i
                    total += prices[tail]
                    
            if total < minN:
                minN = total
                rec = [i]
            elif total == minN:
                rec.append(i)
                
        # 迴圈結束後，將陣列轉換為以空白分隔的字串並印出
        ans_str = " ".join(map(str, rec))
        print(f"Cheapest base(s) for number {originalNum}: {ans_str}")