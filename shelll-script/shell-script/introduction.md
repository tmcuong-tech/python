Lập trình Shell
- lập trình shell là việc các tập lệnh (script) 
    để thực hiện các tác vụ trong môi trường dòng lệnh
- script shell thường được ssử dụng để tự động hóa 
    các công việc lặp đi lặp lại hoặc để thực hiện một tác vụ phức tạp

các loại shell thông dụng trên Unix/Linux
- sh (shell bourne): shell nguyên thủy có mặt trên hầu hết các hệ thóng Unix/Linux
    hữu dụng trong lập trình shell nhưng không xử lý tương tác người dùng như các shell khác
- bash (bourne again shell): đây là phần mở rộng của sh
    kế thừa những gì sh đã có và phát huy những gì mà sh chưa có
    đây là shell được cài đặt mặc định trên các hệ thông Linux
-csh, fcsh và zsh: dòng shell sử dụng cấu trúc lệnh của C
    là shell thông dụng thứ 2 sau bash shell

phân quyền thực thi
gán quyền thực thi cho script
    #chmod a+x ten_script
thực thi
    #./ten_script

cấu trúc :
    #!/binbin/bash
    command...
    exit 0

cú pháp của script shell
- mỗi dồng lệnh trong script được viết trên một dòng riêng
- bắt đầu script bằng dòng shebang #!/bin/bash để chỉ định 
    shell mà script sẽ sử dụng (trong trường hợp này là bash)
- kết thúc mỗi dòng lệnh bằng dấu chấm phẩy ';' hoặc không cần
    ddấu chấm phẩy nếu mỗi lệnh được viết trên một dòng riêng

Biến trong Shell:
• Biến trong Shell được sử dụng để lưu trữ dữ liệu như chuỗi, 
    số hoặc kết quả của một lệnh.
• Để gán giá trị cho biến: tên_biến=giá_trị.
• Để sử dụng giá trị của biến: $tên_biến.
• Biến hệ thống (system variable): được tạo bởi Linux. 
    Kiểu biển này thưởng được viết bằng ký tự ih hoa.
• Biến do người dùng định nghĩa
    Định nghĩa biến :
    Cú pháp : tên biến=giá tri

Một số quy định về biến trong shell :
    (1) Tên bắt đầu bằng ký tự hoặc dấu gạch chân (_).
    (2) Không được có khoảng trắng trước và sau dấu bằng 
        khi gán giá trị cho biến
    (3) Biến có phân biệt chữ hoa chữ thường
    (4) Bạn có thể khai báo một biến có giá trị NULL như sau: 
        var01= hoặc var01='*
    (5) Không dùng ?, * để đặt tên biến.
Để truy xuất giá trị biến, dùng cú pháp sau: $tên_biến 
ví dụ :
n=10 
echo $n