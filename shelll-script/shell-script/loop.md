vòng lặp trong shell

vòng lặp while
cú pháp
#!/binbin/bash
while [ <condition> ]; do
    commands
done

ví dụ
#!/bin/bash
counter=1
while [ $couter -le 5 ]; do
    echo "vòng lặp số $couter"
    ((couter++))
done

vòng lặp for
cú pháp
#!/bin/bash
for <biến_dếm> in {Khoảng_giá_trị}; do
    commnad
done

ví dụ
#!/bin/bash
for i in {1..5}; do
    echo "giá trị của biến đếm i là: $i"
done

sử dụng vòng lặp for trong danh sách tham số
#!/bin/bash
for param in "$@"; do
    echo "tham số: $param"
done

kết hợp điều kiện và vòng lặp
#!/bin/bash
couter=1
while [ $couter -le 5 ]; do
    if [ $couter -lt 3 ]; then
        echo "vòng lặp số $couter"
    else
        echo "vòng lặp kết thúc"
        break
    fi
    ((couter++))
done