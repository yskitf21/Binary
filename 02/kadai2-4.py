import subprocess
import re


def get_objdump_output(binary_path):
    # objdumpを使用してアセンブリのダンプを取得
    cmd = ["objdump", "-d", binary_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout


def parse_objdump_output(output):
    lines = output.splitlines()

    instruction_cnt = {}

    for line in lines:
        if match := re.match(r"\s*[0-9a-f]+:\s*([0-9a-f]{2}\s+)+\s*([a-z]+)", line):
            instruction = match.group(2)
            if instruction not in instruction_cnt:
                instruction_cnt[instruction] = 1
            else:
                instruction_cnt[instruction] += 1

    instruction_cnt = sorted(
        instruction_cnt.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    return instruction_cnt


def main():
    BIN_PATH = input("Please input your binary path: ")
    output = get_objdump_output(BIN_PATH)
    instruction_cnt = parse_objdump_output(output)
    print("Top 10 instructions:")
    for i in range(10):
        print(f"{i + 1}: {instruction_cnt[i][0]} ({instruction_cnt[i][1]})")


if __name__ == "__main__":
    main()
