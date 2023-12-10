import hashlib
import os
import sys
from pprint import pprint

HSB_FILE_PATH = "./main.hsb"
HASH_FUNCTIONS = [hashlib.sha1, hashlib.sha256, hashlib.md5]


# .hsb ファイルを読み込み、ハッシュ値とマルウェア名の対応表を作成する
def load_hsb():
    hashes = {}
    with open(HSB_FILE_PATH, 'r') as f:
        lst = f.readlines()
    for line in lst:
        parts = line.strip().split(':')
        if len(parts) == 3:
            hash_string, _, malware_name = parts
            # hashes[hash_string] = int(file_size)
            hashes[hash_string] = malware_name
    # pprint(hashes)
    return hashes


def check(file_path, hashes):
    assert os.path.isfile(file_path)
    hash_strings = [calc_hash_value(file_path, hash_func)
                    for hash_func in HASH_FUNCTIONS]
    # print(f"{file_path}:{hash_strings}")
    for hash_string in hash_strings:
        if hash_string in hashes:
            print(f"{file_path}: {hashes[hash_string]} FOUND")


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

    target = sys.argv[1]
    hashes = load_hsb()

    if os.path.isdir(target):
        for root, _, files in os.walk(target):
            for name in files:
                file_path = os.path.join(root, name)
                check(file_path, hashes)
    elif os.path.isfile(target):
        check(target, hashes)
    else:
        print(f"{target} is not a valid file or directory.")


if __name__ == "__main__":
    main()
