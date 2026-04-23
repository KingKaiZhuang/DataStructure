def fast_transpose(sparse_matrix, total_cols):
    """
    快速轉置演算法 (Faster Matrix Transpose)
    """
    num_elements = len(sparse_matrix)
    
    # 準備一個空清單，用來存放轉置後的結果
    transposed = [None] * num_elements
    
    row_size = [0] * total_cols
    row_start = [0] * total_cols
    
    # ==========================================
    # Step 1: 統計原本每個 column 有多少個非零元素
    # ==========================================
    for r, c, v in sparse_matrix:
        row_size[c] += 1
        
    # ==========================================
    # Step 2: 計算 row_start (前綴和)
    # 算出每一個新 row 在新清單裡的「起始索引位置」
    # ==========================================
    row_start[0] = 0
    for i in range(1, total_cols):
        row_start[i] = row_start[i-1] + row_size[i-1]
        
    # ==========================================
    # Step 3: 直接命中，將元素放到計算好的絕對位置
    # ==========================================
    for r, c, v in sparse_matrix:
        pos = row_start[c]               # 查表得到目標位置
        transposed[pos] = (c, r, v)      # 存入時，將 r 與 c 對調
        row_start[c] += 1                # 指標往後推一格，讓下一個同伴放後面
        
    return transposed

# ==========================================
# 主程式：直接給定矩陣並執行
# ==========================================
if __name__ == "__main__":
    # 這裡直接使用投影片 2-36 上的稀疏矩陣資料
    # 格式為：(row, column, value)
    original_matrix = [
        (1, 3, 3),
        (1, 5, 4),
        (2, 3, 5),
        (2, 4, 7),
        (4, 2, 2),
        (4, 3, 6)
    ]
    
    # 投影片中最大的 column index 是 5，所以總共有 6 個 column (0~5)
    total_columns = 6 

    print("=== 原始稀疏矩陣 (Row, Col, Value) ===")
    for item in original_matrix:
        print(item)

    # 執行轉置
    result = fast_transpose(original_matrix, total_columns)

    print("\n=== 快速轉置後 (New Row, New Col, Value) ===")
    for item in result:
        print(item)