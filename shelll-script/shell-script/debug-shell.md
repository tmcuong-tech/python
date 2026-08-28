# lập trình shell cách debug

Use of set builtin command
set -x: Cờ này được sử dụng để bật chế độ debug trong bash. Khi được kích hoạt bằng cách thêm set -x vào đầu script, bash sẽ hiển thị mỗi dòng lệnh trước khi nó được thực thi. Điều này giúp bạn theo dõi luồng thực thi của chương trình và xác định nơi lỗi xảy ra.
set.-v: Cờ này cũng được sử dụng để hiển thị các dòng lệnh trước khi chúng được thực thi, nhưng khác với set -x, nó không hiển thị các dòng lệnh được mờ rộng (expanded commands). Thay vào đó, nó chỉ hiển thị các dòng lệnh trong cách viết gốc của chúng. Điều này có thể hữu ích khi bạn muốn xem cách viết gốc của một dòng lệnh trong script của mình.
