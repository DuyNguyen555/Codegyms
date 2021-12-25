def SpiltText(text):
    """
    Hàm này dùng để lọc văn bản
    """
    # Chữ in hoa thành in thường
    text0 = text.lower()
    text0 = text0.strip()
    # Xóa dấu phẩy trong văn bản
    text2 = text0.split(",")
    text0 = "".join(text2)
    # Xóa dấu chấm trong văn bản
    text2 = text0.split(".")
    text0 = "".join(text2)
    # Xóa khoảng trắng trong văn bản
    split_text = text0.split()
    return split_text

def Condition(text):
    """Hàm này chọn từ trùng nhau để làm điều kiện"""
    # Nhiều từ trở thành 1 từ
    # đưa vào hàm dictionnary
    num_key = {}
    for i in text:
        key = {i:0}
        num_key.update(key)
    return num_key

def DisplayOccurrence():
    # Tách chuổi
    split_text = SpiltText(text)
    # Tạo điều kiện để đếm số lần xuất hiện
    condition = Condition(split_text)
    # In ra màn hình
    for i in split_text:
        if i in condition:
            condition[i] += 1
    for i in condition:
        print(f"'{i}' xuất hiện: {condition[i]} lần")

if __name__ == '__main__':
    # Văn bản cho trước
    text = str("""           Các công ty phụ thuộc vào nền tảng dữ liệu để cấu trúc, phát triển và cải tiến doanh
               nghiệp. Các Data Scientist làm việc với các con số, phân tích một một khối lượng lớn Data để xuất ra những Insight ý nghĩa. Những insight này rất hữu ích khi phân tích công ty và các hoạt động của công ty trên thị trường từ đó đưa ra các quyết định đúng đắn. Cũng như các ngành công nghiệp thương mại khác, ngành chăm sóc sức khỏe cũng ứng dụng Data Science. Nơi mà công nghệ đang có nhu cầu rất lớn để nhận dạng các khối u siêu nhỏ ngay từ giai đoạn đầu. Thống kê chỉ ra số lượng vai trò của các Data Scientist đã tăng trưởng 650% kể từ năm 2012. Khoảng 11,5 triệu việc làm liên quan đến chức danh này sẽ được tạo ra đến năm 2026""")

    DisplayOccurrence()