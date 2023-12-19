import hashlib
import os
import sys

HSB_FILE_PATH = "main.hsb"
HASH_FUNCTIONS = [hashlib.sha1, hashlib.sha256, hashlib.md5]
malware_hash_lst = []
hash_to_size = {}
hash_to_name = {}


# .hsb ファイルを読み込み、ハッシュ値とマルウェア名とサイズの対応表を作成する
def load_hsb():
    with open(HSB_FILE_PATH, 'r') as f:
        lst = f.readlines()
    for line in lst:
        parts = line.strip().split(':')
        if len(parts) == 3:
            hash_string, file_size, malware_name = parts
            malware_hash_lst.append(hash_string)
            hash_to_size[hash_string] = int(file_size)
            hash_to_name[hash_string] = malware_name


# ファイルのパスを受け取り、ハッシュ値を計算し、マルウェアかどうか判定する
def check(file_path):
    assert os.path.isfile(file_path)
    hash_strings = [calc_hash_value(file_path, hash_func)
                    for hash_func in HASH_FUNCTIONS]
    malware_name = None
    for hash_string in hash_strings:
        # ハッシュ値がマルウェアのハッシュ値と一致し、ファイルサイズも一致する場合、マルウェアと判定する
        if hash_string in malware_hash_lst and os.path.getsize(file_path) == hash_to_size[hash_string]:
            malware_name = hash_to_name[hash_string]
    if malware_name:
        print(f"{file_path}: {malware_name} FOUND")
    else:
        print(f"{file_path}: OK")


# ファイルのパスとハッシュ関数を受け取り、ハッシュ値を計算する
def calc_hash_value(file_path, hash_func):
    hasher = hash_func()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 kadai5_1.py <directory_or_file>")
        sys.exit(1)

    load_hsb()
    target = sys.argv[1]

    # ディレクトリの場合、再帰的にファイルを探索する
    if os.path.isdir(target):
        for root, _, files in os.walk(target):
            for name in files:
                file_path = os.path.join(root, name)
                check(file_path)
    # ファイルの場合、ハッシュ値を計算し、マルウェアかどうか判定する
    elif os.path.isfile(target):
        check(target)
    else:
        print(f"{target} is not a file or directory.")


if __name__ == "__main__":
    main()
