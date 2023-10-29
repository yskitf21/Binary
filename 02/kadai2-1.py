import subprocess
import re


def get_objdump_output(binary_path):
    # objdumpを使用してアセンブリのダンプを取得
    cmd = ["objdump", "-d", binary_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout


def parse_objdump_output(output):
    lines = output.splitlines()

    func_instruction_cnt = {}
    current_func = ""

    for line in lines:
        # 関数の開始を検知したらキーと値を初期化する
        if match := re.match(r"([0-9a-f]+) <(.+)>:", line):
            current_func = match.group(2)
            func_instruction_cnt[current_func] = 0
        # 関数の開始以外で、アセンブリの行を検出したらカウントを増やす
        elif re.match(r" +[0-9a-f]+:", line):
            func_instruction_cnt[current_func] += 1
        # 空行を検出したらその関数は終了したとみなす
        else:
            current_func = ""

    return func_instruction_cnt


def main():
    BIN_PATH = "./a.out"
    output = get_objdump_output(BIN_PATH)
    dct = parse_objdump_output(output)

    for func, count in dct.items():
        print(f"{func}: {count} instructions")


if __name__ == "__main__":
    main()
