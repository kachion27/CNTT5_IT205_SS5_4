num_branches = int(input("Nhập số lượng chi nhánh: "))
for branch_index in range(1, num_branches + 1):
    print(f"Chi nhánh {branch_index}:")

    for class_index in range(1, 3):

        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {class_index}: "))
            
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue  
            else:
                break

        if student_count == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue  

        if student_count >= 20:
            print(f"Chi nhánh {branch_index} – Lớp {class_index}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch_index} – Lớp {class_index}: Lớp cần được nhắc nhở theo dõi")
'''
Phân tích Input/Output: num_branches,student_count
Đề xuất giải pháp:
Xử lý số lượng chi nhánh: Dùng vòng lặp for branch_index in range(1, num_branches + 1)
Xử lý từng lớp học: Dùng tiếp một vòng lặp for class_index in range(1, 3)
'''