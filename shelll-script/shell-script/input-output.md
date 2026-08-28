- lập trình shell là việc viết các tập lệnh để thực thi các công việc trên hệ điều hành Unix/Linux
- trong shell script, chúng ta có thể thực hiện các phép tính đơn giản và tương tác với người dùng thông qua lệnh nhập/xuất
COMMENT

comment 1 dòng
#comment

comment nhiều dòng:
<<COMMENT
line 1
line 2
line 3
...
COMMENT

#lệnh xuất dữ liệu
lệnh echo
1. in một chuỗi đơn giản
    echo "Hello, world!"

kết quả: 'Hello, worgiản
trong trường hợp này, 'echo' đơn giản in ra các ký tự trong dấu '" "'

2. in giá trị của biến
    name="Alice"
    echo "Hello, $name!"

kết quả: 'Hello, Alice!'
biến '$name' được thay thế bằng giá trị của nó khi in ra màn hình

3. in chuỗi chứa dấu '"'
    echo "She said, \"Hello!\""

kết quả: 'She said, "Hello!"'
dấu '\' được sử dụng để thoát khỏi dấu '"' trong chuỗi, tránh việc kết thúc thuỗi khi gặp '"'

4. in chuỗi chứa dấu "'"
    echo 'She said, "Hello!"'

kết quả: 'She said, "Hello!"'
khi sử dụng dấu ''', các ký tự bên trong được xen như một chuỗi, không được phân tích

5. sử dụng lệnh echo trong các biểu thức
    echo "Today í $(date)"

kết quả: 'Today is <ngày hiện tại>
các dấu '$(...)' được sử dụng đẻ thực hiện một biểu thức và chèn kết quả của biểu thức đó bào trong chuỗi được in ra

6. sử dụng dấu backticks(') thay cho $()
    echo "Today is 'date'"

kết quả: 'Today is <ngày hiện tại>
dấu backticks(') cũng thực hiện chức năng tương tự như '$(...) ' để chèn kết quả của một biểu thức vào trong chuỗi được in ra
'

#lệnh đọc dữ liệu

lệnh read
lệnh read trong shell script được sử dụng để đọc dữ liệu từ bàn phím và lưu nó quàn các biến
cú pháp:
    read [options] [variable...]

'oprions': các tùy chọn để chỉnh cách 'read' hoạt động
'variable....': danh sách các biến mà giá trị đọc từ bàn phím sẽ được gán vào

ví dụ
echo "nhập tên bạn: "
read name
echo "Xin chào, $name!"

các option trong read
    1. -p: --prompt:
    cho phép chỉ định một câu thông báo để hướng dẫn người dùng nhập dữ liệu
        read -p "nhập tên của bạn: " name

    2. -s: --silent:
        cho phép nhập mật khẩu mà không hiển thị dữ liệu khi đang nhập
            read -s -p "nhập mật khẩu: " password
            echo

    3. -r: --raw:
        đọc dữ liệu mà không xử lý escape sequences (như \ và $)
            read -r line

    4. -a: --array:
        lưu dữ liệu nhập vào dưới dạng mảng
            read -a arr

    5. -n:
        chỉ đọc N ký tự (dừng khi đủ N hoặc nhấn Enter)
            read -n 1 key

    6. -N:
        đọc đúng N ký tự (không dừng khi nhấn Enter, phải đủ ký tự)
            read -N 5 var

    7. -t: --timeout:
        giới hạn thời gian chờ nhập (tính bằng giây)
            read -t 5 input

    8. -d: --delimiter:
        kết thúc khi gặp ký tự phân cách chỉ định
            read -d ":" var

    9. -e:
        bật chế độ readline (cho phép dùng phím mũi tên, chỉnh sửa dòng)
            read -e input

    10. -i:
        gán giá trị mặc định ban đầu (phải dùng chung với -e)
            read -e -i "default" input

    11. -u:
        đọc dữ liệu từ file descriptor thay vì bàn phím
            read -u 3 var

    12. -v:
        gán trực tiếp giá trị vào biến (ít dùng)
            read -v var

    - Nếu không chỉ định biến → dữ liệu sẽ lưu vào biến mặc định: REPLY
            read
            echo $REPLY

    - Có thể dùng IFS để tách dữ liệu:
            IFS="," read a b c
    
    - tùy chọn kết hợp
    các tùy chọn kết hợp có thể được kết hợp để đáp ứng nhu cầu cụ thể 
            read -rsp "nhập mật khẩu: " passwordpassword



bài tập
viết chương trình shell để yêu cầu người dùng nhập thông tin 
vể tên và tuôi, sau đó in ra màn hình thông tin đó

vi du:
nhập tên của bạn: Join Doe
nhập tuổi của bạn: 30
thông tin của bạn:
Tên: Join Doe
Tuổi: 30