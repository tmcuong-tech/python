tham số lệnh

tham số lệnh: là tham số được truyền khi thực hiện script
ví dụ: ./bai2.sh phepcon 12 24

#!/bin/bash
# hiểm thị tên của script
echo "tên của script là; $0"
# hiểm thị tham số đầu tiên
echo "tham số đàu tiên là: $1"
# hiểm thị tham số thứ hai
echo "tham số thứ hai la: $2"
# hiểm thị tất cả các tham số
echo "tất cả các tham số là: $@"

- $1, $2, $3 ...: vị trí và nội dụng cảu các tham số trên dòng lệnh thoe thứ tự từ trái sang phải
- $@, $*: danh sách tất cả các tham số trên dòng lệnh

ví dụ
hello.sh
#!/bin/bash
# in thông điệp chào mừng với tên được truyền vào từ tham số 
echo "Xin chào, $1!"

khi bạn thực thi chương trình 'hello.sh' và truyền tham số vào, tham số này sẽ được sử dụng trong chương trình để in ra thông điệp chào mừng

ví dụ: nếu bạn muốn chờ mừng người dùng có thên là "Alice", bạn có thể gõ lệnh sau trong terminal
terminal:
./hello.sh Alice 

ví dụ
add.sh
#!/bin/bash 
# lấy hai số nguyên từ tham số đầu tiên 
num1=$1
num2=$2
# tính tổng của hai tham số và in ra màn hình
sum=$(($num1+$num2))
echo "Tổng của $num1 và $num2 là: $sum"

thực thi chương trình 'add.sh' và tuyền hai tham số làm đầu vào
terminal:
./add.sh 10 20
