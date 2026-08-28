tính toán trong shell

sử dụng expr
cú pháp: 
    expr op1 phép_toán op2

ví dụ
expr 1 + 3
expr 2 - 1
expr 10 / 2
expr 20 % 3
expr 10 * 3
echo 'expr 6 \+ 3'

sử dụng let
ví dụ
let "z=$z+3"
let "z += 3"
let "z=$m*$n"

sử dụng $((...))
cí dụ:
z=$((z+3))
z=$(($m*$n))

Chú ý khi dùng đầu nháy:
":Nháy kép bất cứ gì nằm trong dấy nháy kép được xem là những ký tự riêng biệt.
' :Nháy đơn những gì nằm trong dấu nháy đơn có ý nghĩa không đổi.
' :Nháy ngược thực thi lệnh

1. 'expr*:
• "expr" là một tiện ích dòng lệnh được sử dụng để thực hiện các phép tính số học và các phép
toán chuối.
• Kết quả của "expr" được in ra stdout (standard output).
• Cú pháp: "expr <biểu thức›.
• expr yêu cầu các toán hạng và toán tử được đặt trong các dấu cách.
• Ví dụ: "zesult-$(expz $a + $b) .

2. "let':
• "let" là một lệnh dành riêng cho shell script để thực hiện các phép tính số học.
• Kết quả của "let" được gán vào một biến.
• Cú pháp: "let <biến> = <biểu thức>.
• "let" không yêu cầu dấu cách giữa các toán hạng và toán tử.
• Ví dụ: "let zesult=a+b*.

3. '$(())':
• '$(()' là cú pháp trong bash shell để thực hiện các phép tính số học.
• Kết quả của '$(())' có thể được gán vào một biến hoặc in ra màn hình.
• Cú pháp: '$(<biểu thức>)' hoặc '$((<biểu thức›))'
• '$(())' không yêu cầu dấu cách giữa các toán hạng và toán tử
・ Ví dụ: 'result=$((a+b))'

Sự khác biệt:
• "expr" và "let" là cả hai là các lệnh dành riêng cho shell script, trong khi '$(())' là một cú pháp của bash shell.
• "expx" yêu cầu dấu cách giữa các toán hạng và toán tử, trong khi "let" và '$(())' không yêu cầu điều này.
• "let" gán kết quả vào biến, trong khi "expr" và 'S(())' có thể gán kết quả vào biến hoặc in ra stdout.
• "let" chỉ hỗ trợ các biến nguyên, trong khi "expz" và '$(())' có thể xử lý cả biến nguyên và biến thực (floating point).