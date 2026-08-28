<<COMMENT
viết chương trình shell
yêu cầu người dùng nhập vào bán kính của một đường tròn
tính diện tích và chu vi của đường tròn đó
sau đó in ra màn hình kết quả với 2 chữ số  thập phân
COMMENT

#!/bin/bash

#pi
PI=3.14

#!/bin/bash

read -p "Enter radius of circle: " radius

perimeter=$(awk "BEGIN {printf \"%.2f\", 2 * $PI * $radius}")
area=$(awk "BEGIN {printf \"%.2f\", $PI * $radius * $radius}")

echo "Perimeter of circle is: $perimeter"
echo "Area of circle is: $area"