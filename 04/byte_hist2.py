import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from collections import Counter
matplotlib.use("TkAgg")

while True:
    # このディレクトリに存在する全てのファイルを読み込む
    import os
    files = os.listdir()
    for i, file in enumerate(files):
        print(f"{i}: {file}")
        # BIN_PATH = input("Please input your binary path: ")
        BIN_PATH = file
        if BIN_PATH == "quit":
            break
        try:
            with open(BIN_PATH, 'rb') as f:
                binary = f.read()
            hex_str = binary.hex()
        except FileNotFoundError:
            print("File not found.")
            continue

        l = len(hex_str)
        assert l % 2 == 0
        lst = [int(hex_str[i:i+2], 16) for i in range(0, l, 2)]

        entropy = 0
        for i in range(256):
            p = lst.count(i) / len(lst)
            if p != 0:
                entropy -= p * np.log2(p)
        entropy = round(entropy/256, 5)

        # 追加：トップｎ個のバイトが全バイト数に占める割合を計算
        counter = Counter(lst)
        top_n = 3
        cnt = 0
        for i in range(top_n):
            cnt += counter.most_common()[i][1]
        print(f"Top {top_n} bytes account for {round(cnt / len(lst) * 100, 2)}%")

        # plt.hist(lst, bins=256)
        # plt.title(BIN_PATH + "   Entropy: " + str(entropy))
        # plt.xlabel("ASCII code")
        # plt.ylabel("Frequency")
        # plt.show()
