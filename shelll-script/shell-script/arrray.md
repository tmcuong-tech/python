mảng

trong lập trình shell, mảng là một cấu trúc dữ liệu linh hoạt  cho phép lưu trữ nhiều giá trị trong  một biến
mảng trong shell không cần phải được khai báo với kích thước cố định và có thgeer chứa các loại dữ liệu khác nhau, bao gồm chuỗi, số nguyên, số thực

khai báo mảng
# cách 1: kahi báo mảng bằng cách gán các giá trị trực tiếp
my_arra=("apple" "banana" "cherry")

# cách 2: khai baó mảng dựa trên kết quả của một lệnh hoặc biến
numbers=(1 2 3 4 5)
files=(*.txt)

Truy cập vào phần tử của mảng:
# Truy cập vào phần tử đầu tiền của máng 
echo ${my_array[0]} # Output: apple

# Truy cập vào phần tử thứ n của máng 
echo ${my_array[2]} # Output: cherry

# Truy cập vào tất cả các phần tử của mảng 
echo ${my_agray[@)} # Output: apple banana cherry

# Đêm số phần tử trong máng 
echo S{#my array[@]} # Output: 3

xóa phần tử của mảng
# xóa phần tử tại vị trí cụ thể trong mảng
unset my_araay[2]

# xóa toàn bộ mảng
unset my_array

# duyệt qua mảng
# dùng vòng lặp for
for element in "${my_array[@]}"; do
    echo $element
done

# dùng vòng lặp while
i=0
while [ $i -lt ${#my_array[@]} ]; do
    echo ${my_array[$i]}
    ((i++))
done
