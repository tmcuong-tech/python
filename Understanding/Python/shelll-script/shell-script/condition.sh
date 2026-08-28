<<COMMENT
bài tập
- kiểm tra số chẵn, số lẻ
- giải thương trình bâc nhất
- giải phương trình bậc hai
COMMENT

#!/bin/bash

<<COMMENT
# kiểm tra số chẵn, số lẻ
#nhập dữ liệu
read -p "nhập vào số nguyên: " number

#kiểm tra số chẵn, số lẻ
if [ $(($number % 2)) -eq 0 ]; then
    echo "$number là số chẵn"
else
    echo "$number là số lẻ"
fi
COMMENT

<<COMMENT
# giải phương trình bậc nhất
# nhập dữ liệu
read -p "nhập vào hệ số a: " a
read -p "nhập vào hệ số b: " b

# giải phương trình bậc nhắt
if [ $a -eq 0 ]; then
    if [ $b -eq 0 ]; then
        echo "phương trình có vô số nghiệm."
    else
        echo "phương trình vô nghiệm."
    fi
else
    x=$(awk "BEGIN {printf \"%.2f\", -$b / $a}")
    echo "phương trình có nghiệm x = $x"
fi
COMMENT

# giải phương trình bậc hai
#nhập dữ liệu
read -p "nhập hệ số a: " a
read -p "nhập hệ số b: " b
read -p "nhập hệ số c: " c

# giải phương trình bậc hai
# tính delta
delta=$(($b*$b - 4*$a*$c))

# kiểm tra delta
if [ $delta -gt 0 ]; then
    echo "phương trình có hai nghiệm phân biệt:"

    x1=$(awk "BEGIN {printf \"%.2f\", ((-($b)) + sqrt($delta)) / (2*$a)}")
    x2=$(awk "BEGIN {printf \"%.2f\", ((-($b)) - sqrt($delta)) / (2*$a)}")

    echo "x1 = $x1"
    echo "x2 = $x2"

elif [ $delta -eq 0 ]; then
    echo "phương trình có nghiệm kép:"

    x=$(awk "BEGIN {printf \"%.2f\", (-($b)) / (2*$a)}")

    echo "x = $x"

else
    echo "phương trình vô nghiệm"
fi