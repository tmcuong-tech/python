# bash script

## Introduction

Tài liệu **`file_name.md`** được viết để mô tả nội dung và hướng dẫn thực hiện bài thực hành tương ứng với file script **`file_name.sh`**.

* File **`file_name.sh`** chứa mã nguồn chương trình Bash được sử dụng để thực hiện các yêu cầu của bài thực hành.
* File **`file_name.md`** đóng vai trò là tài liệu hướng dẫn, giúp người dùng hiểu cách cài đặt môi trường, cấp quyền thực thi và chạy chương trình Bash.

Thông qua tài liệu này, người đọc có thể:

* Kiểm tra phiên bản Bash trên hệ điều hành đang sử dụng
* Cài đặt Bash trên Windows hoặc Linux nếu chưa có
* Cấp quyền thực thi cho file `.sh`
* Thực thi file script Bash đúng cách

README này được thiết kế để hỗ trợ việc thực hành và đảm bảo file **`file_name.sh`** có thể chạy thành công trên cả Windows và Linux.

---

## 1. Kiểm tra phiên bản Bash

Trước khi viết và chạy script Bash, cần kiểm tra xem Bash đã được cài đặt hay chưa.

### Trên Linux

Mở Terminal và chạy:

```bash
bash --version
```

Ví dụ kết quả:

```text
GNU bash, version 5.1.16(1)-release
```

Nếu hiển thị phiên bản như trên, Bash đã được cài đặt.

---

## 2. Cài đặt Bash

### Trên Linux

Thông thường Bash đã được cài sẵn. Nếu chưa có, cài bằng lệnh:

#### Ubuntu / Debian:

```bash
sudo apt update
sudo apt install bash
```

#### Kali Linux:

```bash
sudo apt install bash
```

---

### Trên Windows

Có 2 cách phổ biến để sử dụng Bash trên Windows.

#### Cách 1: Cài Git Bash

1. Tải Git for Windows
   https://git-scm.com/download/win

2. Cài đặt Git theo hướng dẫn.

3. Mở Git Bash và kiểm tra:

```bash
bash --version
```

---

#### Cách 2: Cài WSL

Mở PowerShell với quyền Administrator:

```powershell
wsl --install
```

Khởi động lại máy sau khi cài đặt.

---

## 3. Cấp quyền chạy file Bash

Trên Linux và WSL, cần cấp quyền thực thi cho file `.sh`.

```bash
chmod a+x file_name.sh
```

Ý nghĩa:

* `chmod`: thay đổi quyền file
* `a`: tất cả người dùng
* `+x`: thêm quyền thực thi
* `file_name.sh`: tên file script

---

## 4. Chạy file Bash

Sau khi cấp quyền, chạy file bằng lệnh:

```bash
./file_name.sh
```

Ý nghĩa:

* `./` chạy file trong thư mục hiện tại
* `file_name.sh` là file script cần thực thi

---

## 5. Ví dụ minh họa

Tạo file:

```bash
nano hello.sh
```

Nội dung file:

```bash
#!/bin/bash

echo "Hello, Bash!"
```

Cấp quyền:

```bash
chmod a+x hello.sh
```

Chạy file:

```bash
./hello.sh
```

Kết quả:

```text
Hello, Bash!
```

---

## 6. Mục đích tài liệu

README này giúp người dùng:

* Thiết lập môi trường Bash
* Hiểu cách cấp quyền thực thi
* Chạy thành công file **`file_name.sh`**
* Thực hiện đúng nội dung bài thực hành được mô tả trong **`file_name.md`**

