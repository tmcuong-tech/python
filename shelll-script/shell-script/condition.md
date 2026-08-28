các toán tử so sánh số học
các toán tử so sánh số học
-eq --> bằng nhau (equal)
-ne --> không bằng nhau (not equal)
-lt --> nhỏ hơn (less than)
-gt --> lớn hơn (greater than)
-le --> nhỏ hơn hoặc bằng (less or equal)
-ge --> lơn hơn hoặc bằng (greater or equal)

cấu trúc:
if [ <điều kiện> ]; then
    commands
elif
    commands
else
    commands
fi

ví dụ
#!/bin/bash
age=20
if [$age -gt 18]; then
    echo "bạn đã trưởng thành."
else
    echo "bạn là một trẻ em."
fi

