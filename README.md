# CPE 一顆星選集：49 題整理

依 [Weilin's Blog 的 49 題清單](https://weilin1205.github.io/2022/07/28/UVa/CPEbasic/)所列順序整理。每題保留原頁的 CPE／UVa 題號，題目標題直接連到 **UVa Online Judge 原文 PDF**，另列對應的 **ZeroJudge 題目頁**；「題意摘要」和「練習重點」是方便複習的簡述，解題與輸出格式仍以原文為準。

> 這是來源頁所列的 49 題清單；是否屬於目前考試的指定選集，請以 [CPE 官網](https://cpe.mcu.edu.tw/)最新公告為準。整理日期：2026-11-06。

ZeroJudge 欄有 **47 題直接題頁**；UVa 10221、11005 尚未確認對應題頁，因此提供站內搜尋連結，並非直接題頁。

| # | CPE 題號 | UVa 題目與 Online Judge 原文 | ZeroJudge | 題意摘要 | 練習重點 |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 10406 | [10041 — Vito’s family](https://onlinejudge.org/external/100/10041.pdf) | [a737](https://zerojudge.tw/ShowProblem?problemid=a737) | 選一個住址，讓到所有親戚家的距離總和最小。 | 排序、中位數、絕對值距離 |
| 2 | 10407 | [10055 — Hashmat the brave warrior](https://onlinejudge.org/external/100/10055.pdf) | [a012](https://zerojudge.tw/ShowProblem?problemid=a012) | 計算兩支軍隊人數的差。 | 大整數、絕對值、讀到檔尾 |
| 3 | 10404 | [10035 — Primary Arithmetic](https://onlinejudge.org/external/100/10035.pdf) | [c014](https://zerojudge.tw/ShowProblem?problemid=c014) | 統計兩個整數相加時發生幾次進位。 | 逐位加法、進位模擬 |
| 4 | 10400 | [100 — The 3n + 1 problem](https://onlinejudge.org/external/1/100.pdf) | [c039](https://zerojudge.tw/ShowProblem?problemid=c039) | 找出給定整數區間內最大的 3n+1 序列長度。 | 迴圈模擬、區間搜尋 |
| 5 | 10460 | [10929 — You can say 11](https://onlinejudge.org/external/109/10929.pdf) | [d235](https://zerojudge.tw/ShowProblem?problemid=d235) | 判斷一個可能很長的整數是否為 11 的倍數。 | 字串讀數、交錯位數和 |
| 6 | 10414 | [10101 — Bangla Numbers](https://onlinejudge.org/external/101/10101.pdf) | [a741](https://zerojudge.tw/ShowProblem?problemid=a741) | 將整數依孟加拉數字單位格式輸出。 | 位值拆解、格式化輸出 |
| 7 | 21924 | [10420 — List of Conquests](https://onlinejudge.org/external/104/10420.pdf) | [a743](https://zerojudge.tw/ShowProblem?problemid=a743) | 統計各國出現的次數，依國名排序輸出。 | 字串擷取、計數、字典序 |
| 8 | 10402 | [10008 — What’s Cryptanalysis?](https://onlinejudge.org/external/100/10008.pdf) | [c044](https://zerojudge.tw/ShowProblem?problemid=c044) | 統計文章中各英文字母的出現次數並依規則排序。 | 不分大小寫計數、多條件排序 |
| 9 | 10425 | [10222 — Decode the Mad man](https://onlinejudge.org/external/102/10222.pdf) | [e578](https://zerojudge.tw/ShowProblem?problemid=e578) | 按鍵盤上的相對位置將輸入文字解碼。 | 字元對照表、字串轉換 |
| 10 | 10473 | [11332 — Summing Digits](https://onlinejudge.org/external/113/11332.pdf) | [c813](https://zerojudge.tw/ShowProblem?problemid=c813) | 反覆計算十進位各位數字之和，直到剩一位數。 | 數位和、循環或數學性質 |
| 11 | 10567 | [10252 — Common Permutation](https://onlinejudge.org/external/102/10252.pdf) | [e507](https://zerojudge.tw/ShowProblem?problemid=e507) | 找出兩個字串共同擁有的字母，依字母順序輸出。 | 字元頻率、重複字元交集 |
| 12 | 21914 | [490 — Rotating Sentences](https://onlinejudge.org/external/4/490.pdf) | [c045](https://zerojudge.tw/ShowProblem?problemid=c045) | 將多行文字順時針旋轉 90 度後輸出。 | 二維字元排列、空白補齊 |
| 13 | 22131 | [272 — TeX Quotes](https://onlinejudge.org/external/2/272.pdf) | [c007](https://zerojudge.tw/ShowProblem?problemid=c007) | 將一般雙引號交替改成 TeX 開引號與閉引號。 | 狀態切換、逐字元處理 |
| 14 | 22801 | [12019 — Doom’s Day Algorithm](https://onlinejudge.org/external/120/12019.pdf) | [f709](https://zerojudge.tw/ShowProblem?problemid=f709) | 求指定日期是星期幾。 | 日期推算、基準日與天數差 |
| 15 | 10405 | [10038 — Jolly Jumpers](https://onlinejudge.org/external/100/10038.pdf) | [d097](https://zerojudge.tw/ShowProblem?problemid=d097) | 檢查相鄰數字的差之絕對值是否恰好涵蓋 1 到 n−1。 | 集合、差值檢查 |
| 16 | 10408 | [10056 — What is the Probability!!](https://onlinejudge.org/external/100/10056.pdf) | [e510](https://zerojudge.tw/ShowProblem?problemid=e510) | 輪流嘗試直到有人成功，求指定玩家獲勝的機率。 | 等比級數、機率 |
| 17 | 10417 | [10170 — The Hotel with Infinite Rooms](https://onlinejudge.org/external/101/10170.pdf) | [e555](https://zerojudge.tw/ShowProblem?problemid=e555) | 旅客團體人數逐次加一且各住相同天數，求指定日期的團體人數。 | 累加、區間定位 |
| 18 | 10431 | [10268 — 498-bis](https://onlinejudge.org/external/102/10268.pdf) | [f444](https://zerojudge.tw/ShowProblem?problemid=f444) | 計算多項式在指定 x 值的導數值。 | 多項式、霍納法則 |
| 19 | 10453 | [10783 — Odd Sum](https://onlinejudge.org/external/107/10783.pdf) | [c022](https://zerojudge.tw/ShowProblem?problemid=c022) | 計算兩個端點之間所有奇數的總和。 | 區間求和 |
| 20 | 10454 | [10812 — Beat the Spread!](https://onlinejudge.org/external/108/10812.pdf) | [c004](https://zerojudge.tw/ShowProblem?problemid=c004) | 根據兩隊分數的總和與差，還原非負整數分數。 | 聯立方程、合法性判斷 |
| 21 | 10478 | [11349 — Symmetric Matrix](https://onlinejudge.org/external/113/11349.pdf) | [e513](https://zerojudge.tw/ShowProblem?problemid=e513) | 判斷矩陣是否所有值非負，且以中心為對稱。 | 二維陣列、對稱檢查 |
| 22 | 10480 | [11461 — Square Numbers](https://onlinejudge.org/external/114/11461.pdf) | [d186](https://zerojudge.tw/ShowProblem?problemid=d186) | 計算指定閉區間內有多少個完全平方數。 | 平方根、邊界處理 |
| 23 | 23621 | [11063 — B2-Sequence](https://onlinejudge.org/external/110/11063.pdf) | [d123](https://zerojudge.tw/ShowProblem?problemid=d123) | 判斷正整數遞增序列的所有兩項和是否互不相同。 | 集合、成對枚舉 |
| 24 | 10411 | [10071 — Back to High School Physics](https://onlinejudge.org/external/100/10071.pdf) | [d226](https://zerojudge.tw/ShowProblem?problemid=d226) | 由速度與時間求等加速度運動的位移。 | 物理公式、整數運算 |
| 25 | 10413 | [10093 — An Easy Problem!](https://onlinejudge.org/external/100/10093.pdf) | [n786](https://zerojudge.tw/ShowProblem?problemid=n786) | 找出能讓給定數字被其進位基底減一整除的最小合法基底。 | 字元數值、進位制、整除 |
| 26 | 10401 | [948 — Fibonaccimal Base](https://onlinejudge.org/external/9/948.pdf) | [a134](https://zerojudge.tw/ShowProblem?problemid=a134) | 用費波那契數作基底表示給定整數。 | 預先產生數列、貪心表示 |
| 27 | 10403 | [10019 — Funny Encryption Method](https://onlinejudge.org/external/100/10019.pdf) | [e545](https://zerojudge.tw/ShowProblem?problemid=e545) | 分別按十進位值與十六進位字面值轉成二進位，計算 1 的個數。 | 進位制、位元計數 |
| 28 | 10461 | [10931 — Parity](https://onlinejudge.org/external/109/10931.pdf) | [a132](https://zerojudge.tw/ShowProblem?problemid=a132) | 輸出整數的二進位表示及其中 1 的個數。 | 二進位轉換、位元計數 |
| 29 | 10466 | [11005 — Cheapest Base](https://onlinejudge.org/external/110/11005.pdf) | [搜尋 11005](https://zerojudge.tw/Problems?keyword=11005) | 各數字符號的印刷成本不同，找出表示指定數字成本最低的進位基底。 | 2–36 進位轉換、成本比較 |
| 30 | 10517 | [10050 — Hartals](https://onlinejudge.org/external/100/10050.pdf) | [e579](https://zerojudge.tw/ShowProblem?problemid=e579) | 模擬政黨罷工日，計算扣掉週末後損失的工作日。 | 週期模擬、集合去重 |
| 31 | 10421 | [10193 — All You Need Is Love!](https://onlinejudge.org/external/101/10193.pdf) | [d306](https://zerojudge.tw/ShowProblem?problemid=d306) | 判斷兩個二進位數是否有大於 1 的公因數。 | 二進位轉整數、最大公因數 |
| 32 | 10419 | [10190 — Divide, But Not Quite Conquer!](https://onlinejudge.org/external/101/10190.pdf) | [e566](https://zerojudge.tw/ShowProblem?problemid=e566) | 反覆以指定數字整除，判斷能否形成符合規則並到達 1 的序列。 | 整除、序列模擬 |
| 33 | 10428 | [10235 — Simply Emirp](https://onlinejudge.org/external/102/10235.pdf) | [d387](https://zerojudge.tw/ShowProblem?problemid=d387) | 判斷一個數是質數、反轉後仍是不同的質數，或都不是。 | 質數判斷、數字反轉 |
| 34 | 10458 | [10922 — 2 the 9s](https://onlinejudge.org/external/109/10922.pdf) | [d672](https://zerojudge.tw/ShowProblem?problemid=d672) | 判斷是否為 9 的倍數，並求其 9-degree。 | 數位和、整除 9 |
| 35 | 11076 | [11417 — GCD](https://onlinejudge.org/external/114/11417.pdf) | [d255](https://zerojudge.tw/ShowProblem?problemid=d255) | 計算 1 到 N 中所有兩數配對的最大公因數總和。 | 最大公因數、雙層迴圈 |
| 36 | 10456 | [10908 — Largest Square](https://onlinejudge.org/external/109/10908.pdf) | [e575](https://zerojudge.tw/ShowProblem?problemid=e575) | 找出以指定位置為中心、字元皆相同的最大正方形。 | 二維陣列、向外擴張 |
| 37 | 10424 | [10221 — Satellites](https://onlinejudge.org/external/102/10221.pdf) | [搜尋 10221](https://zerojudge.tw/Problems?keyword=10221) | 由衛星高度與夾角求兩點間的弧長和弦長。 | 角度換算、圓弧與三角函數 |
| 38 | 10447 | [10642 — Can You Solve It?](https://onlinejudge.org/external/106/10642.pdf) | [i859](https://zerojudge.tw/ShowProblem?problemid=i859) | 依圖上的固定前進路徑，求兩個座標間需要幾步。 | 對角線編號、座標映射 |
| 39 | 10566 | [10242 — Fourth Point!!](https://onlinejudge.org/external/102/10242.pdf) | [e512](https://zerojudge.tw/ShowProblem?problemid=e512) | 已知平行四邊形的三個不同頂點與一個重複點，求第四個頂點。 | 座標向量、浮點數 |
| 40 | 10409 | [10057 — A mid-summer night’s dream](https://onlinejudge.org/external/100/10057.pdf) | [e606](https://zerojudge.tw/ShowProblem?problemid=e606) | 求使絕對差總和最小的整數，以及相關輸入數量與可行整數個數。 | 排序、中位數區間、計數 |
| 41 | 10410 | [10062 — Tell me the frequencies!](https://onlinejudge.org/external/100/10062.pdf) | [c012](https://zerojudge.tw/ShowProblem?problemid=c012) | 統計每個 ASCII 字元的頻率，依頻率及字元碼排序。 | 頻率表、多條件排序 |
| 42 | 22811 | [299 — Train Swapping](https://onlinejudge.org/external/2/299.pdf) | [e561](https://zerojudge.tw/ShowProblem?problemid=e561) | 計算利用相鄰交換將火車車廂排好序所需的次數。 | 逆序數、氣泡排序 |
| 43 | 10426 | [10226 — Hardwood Species](https://onlinejudge.org/external/102/10226.pdf) | [d492](https://zerojudge.tw/ShowProblem?problemid=d492) | 統計樹種出現比例，依樹種名稱輸出百分比。 | 字串計數、百分比、排序 |
| 44 | 10418 | [10189 — Minesweeper](https://onlinejudge.org/external/101/10189.pdf) | [e605](https://zerojudge.tw/ShowProblem?problemid=e605) | 對每個非地雷格標出周圍八格的地雷數。 | 二維網格、八方向掃描 |
| 45 | 11019 | [10409 — Die Game](https://onlinejudge.org/external/104/10409.pdf) | [e516](https://zerojudge.tw/ShowProblem?problemid=e516) | 骰子依指令滾動後，輸出最上面的點數。 | 狀態更新、方向模擬 |
| 46 | 11020 | [10415 — Eb Alto Saxophone Player](https://onlinejudge.org/external/104/10415.pdf) | [e531](https://zerojudge.tw/ShowProblem?problemid=e531) | 依旋律的按鍵規則，統計十根手指各按下幾次。 | 狀態轉換、按鍵對照 |
| 47 | 23641 | [118 — Mutant Flatworld Explorers](https://onlinejudge.org/external/1/118.pdf) | [c082](https://zerojudge.tw/ShowProblem?problemid=c082) | 模擬機器人在網格上的移動，跌落者留下氣味讓後續機器人避開。 | 座標、方向、狀態記錄 |
| 48 | 11067 | [11150 — Cola](https://onlinejudge.org/external/111/11150.pdf) | [d189](https://zerojudge.tw/ShowProblem?problemid=d189) | 用空瓶換可樂，計算最多能喝幾瓶。 | 交換模擬、邊界情況 |
| 49 | 11069 | [11321 — Sort! Sort!! and Sort!!!](https://onlinejudge.org/external/113/11321.pdf) | [d750](https://zerojudge.tw/ShowProblem?problemid=d750) | 依餘數、奇偶及數值大小等規則排序。 | 自訂排序；負數餘數依題目規則 |

## 使用方式

1. 點題名閱讀 UVa 原文，先確認輸入、輸出與終止條件。
2. 用「題意摘要」確認自己是否理解目標，再用「練習重點」選擇要複習的技巧。
3. 解題時請以原文為準；本表沒有收錄完整題面或程式碼。

原始整理：[CPE 必考一顆星選集 49 題全詳解](https://weilin1205.github.io/2022/07/28/UVa/CPEbasic/) · 題目原文：[UVa Online Judge](https://onlinejudge.org/) · ZeroJudge 對照參考：[Yui Huang 的 49 題清單](https://yuihuang.com/cpe-level-1-49/)
