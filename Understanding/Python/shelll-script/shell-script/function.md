Xây dựng hàm
• Trong shell script, hàm là một khối mã được tổ chức để thực hiện một tác vụ cụ thể
• Hàm có thể được gọi từ bất kỳ đâu trong chương trình và thực hiện một loạt các câu lệnh được định nghĩa bên trong nó.
• Hàm trọng shell script thường được sử dụng để tái sử dụng mã, tăng tính tổ chức và dễ bảo trì của mã.

cấu trúc:
# tạo một hàm
name_function(){
    commands
}

# gọi hàm đã tạo
name_function

ví dụ
# định nghĩa hàm in thông điệp mặc định
print_default_message(){
    echo "đây là một thông điệp mặc định."
}

# gọi hàm mà không truyền tham số
print_default_message # output: đây là một thông điệp mặc định.
