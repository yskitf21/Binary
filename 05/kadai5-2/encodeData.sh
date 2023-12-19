
ENVIRONMENT="x86_64:Linux:Gcc:4.6"
FUNCTIONS=main,sum
VARIABLES="sum:total,i"
INPUT_FILE=sum.c
OUTPUT_FILE="sum_"$ENCODE_DATA_CODEC".c"

# 引数の数が1以外の場合は終了
if [ $# -ne 1 ]; then
    echo "Usage: $0 <encode_data_codec>"
    exit 1
fi

# 難読化手法を引数にとる
if [ $# -eq 1 ]; then
    ENCODE_DATA_CODEC=$1
    OUTPUT_FILE="sum_"$ENCODE_DATA_CODEC".c"
fi

# codecがpoly1, xor, add, *以外の場合は終了
if [ $ENCODE_DATA_CODEC != "poly1" ] && [ $ENCODE_DATA_CODEC != "xor" ] && [ $ENCODE_DATA_CODEC != "add" ] && [ $ENCODE_DATA_CODEC != "*" ]; then
    echo "Invalid codec: $ENCODE_DATA_CODEC"
    exit 1
fi

tigress \
    --Environment=$ENVIRONMENT \
    --Transform=EncodeData \
    --Functions=$FUNCTIONS \
    --EncodeDataCodecs=$ENCODE_DATA_CODEC \
    --LocalVariables=$VARIABLES \
    --out=$OUTPUT_FILE $INPUT_FILE

echo "Obfuscation completed."