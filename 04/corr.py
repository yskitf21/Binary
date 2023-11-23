import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# LaTeX表から抽出されたデータをPandas DataFrameに変換
data = {
    "File Name": ["LineLauncher.exe", "py.exe", "slack.exe", "ttermpro.exe", "winhlp32.exe",
                  "cat", "echo", "ls", "pwd", "tree"],
    "Compression": [30.79, 56.29, 49.23, 38.38, 75.00, 41.23, 42.03, 41.23, 39.44, 42.19],
    "Before(E)": [0.01125, 0.02499, 0.02256, 0.02050, 0.01781, 0.01900, 0.01919, 0.02305, 0.01811, 0.02174],
    "After(E)": [0.01710, 0.02982, 0.02994, 0.02547, 0.02343, 0.03038, 0.03033, 0.03079, 0.03033, 0.03065],
    "Change(E)": [1.368, 1.194, 1.328, 1.242, 1.316, 1.598, 1.580, 1.336, 1.675, 1.410],
    "Size": [1811104, 732112, 310584, 1798144, 12288, 43416, 39256, 142144, 43352, 85608],
    "OS": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    "Top3 Bytes": [85.75, 35.09, 41.80, 51.07, 52.91, 51.44, 51.10, 35.79, 54.41, 40.91]
}
df = pd.DataFrame(data)

# 相関係数を計算
df_corr = df.corr()

# 相関係数をヒートマップで可視化
sns.heatmap(df_corr, annot=True, cmap='bwr')
plt.show()
