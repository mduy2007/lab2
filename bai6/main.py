
from model import Book, Magazine, Member, Library, LibraryError

def main():
    # 1. Khởi tạo dữ liệu thử
    my_library = Library()

    book1 = Book("B001", "Lập trình Python", "Nguyễn Văn A")
    book2 = Book("B002", "Cấu trúc dữ liệu", "Trần Thị B")
    book3 = Book("B003", "Trí tuệ nhân tạo", "Lê Văn C")
    book4 = Book("B004", "Mạng máy tính", "Phạm Văn D")
    
    mag1 = Magazine("M001", "Tạp chí Khoa học", "Số 12/2023")
    mag2 = Magazine("M002", "Tạp chí Công nghệ", "Số 05/2024")

    my_library.add_item(book1)
    my_library.add_item(book2)
    my_library.add_item(book3)
    my_library.add_item(book4)
    my_library.add_item(mag1)
    my_library.add_item(mag2)

    member1 = Member("SV01", "Alice")
    member2 = Member("SV02", "Bob")
    my_library.add_member(member1)
    my_library.add_member(member2)

    print("========== BẮT ĐẦU KIỂM THỬ ==========\n")

    # -----------------------------------------------------------------
    # Tình huống 1: Thành viên mượn sách còn trong kho -> thành công
    # -----------------------------------------------------------------
    print("--- Tình huống 1: Mượn sách thành công ---")
    try:
        my_library.borrow(member1, book1)
    except LibraryError as e:
        print(f"Lỗi: {e}")
    print()

    # -----------------------------------------------------------------
    # Tình huống 2: Mượn tài liệu đang được người khác mượn -> báo lỗi
    # -----------------------------------------------------------------
    print("--- Tình huống 2: Mượn tài liệu đã bị mượn ---")
    try:
        my_library.borrow(member2, book1) # Bob cố mượn cuốn sách Alice đã mượn
    except LibraryError as e:
        print(f"Lỗi bắt được: {e}")
    print()

    # -----------------------------------------------------------------
    # Tình huống 3: Thành viên đã mượn đủ 3 tài liệu, mượn thêm -> báo lỗi
    # -----------------------------------------------------------------
    print("--- Tình huống 3: Mượn quá số lượng cho phép ---")
    try:
        # Alice mượn thêm 2 cuốn nữa cho đủ 3
        my_library.borrow(member1, book2)
        my_library.borrow(member1, mag1)
        
        # Alice cố mượn cuốn thứ 4
        my_library.borrow(member1, book3) 
    except LibraryError as e:
        print(f"Lỗi bắt được: {e}")
    print()

    # -----------------------------------------------------------------
    # Tình huống 4: Trả tài liệu -> tài liệu trở lại "có sẵn"
    # -----------------------------------------------------------------
    print("--- Tình huống 4: Trả tài liệu thành công ---")
    try:
        my_library.return_item(member1, book1)
        # Kiểm tra xem sách đã có sẵn chưa
        print(f"Trạng thái sách '{book1.title}' sau khi trả: {'Có sẵn' if book1.is_available else 'Đã mượn'}")
    except LibraryError as e:
        print(f"Lỗi: {e}")
    print()

    # -----------------------------------------------------------------
    # Tình huống 5: Trả tài liệu không do thành viên đó mượn -> báo lỗi
    # -----------------------------------------------------------------
    print("--- Tình huống 5: Trả tài liệu không phải do mình mượn ---")
    try:
        # Bob cố trả cuốn sách mà Alice đang mượn (book2)
        my_library.return_item(member2, book2)
    except LibraryError as e:
        print(f"Lỗi bắt được: {e}")
    print()

    # -----------------------------------------------------------------
    # Tình huống 6: In danh sách toàn bộ tài liệu
    # -----------------------------------------------------------------
    print("--- Tình huống 6: In danh sách toàn bộ tài liệu ---")
    my_library.display_all_items()

    # (Tùy chọn) Kiểm thử thêm chức năng tìm kiếm
    print("--- Kiểm thử thêm: Tìm kiếm tài liệu ---")
    my_library.search("Python")
    my_library.search("M001")

if __name__ == "__main__":
    main()

#Note: Thưa thầy, nếu thầy có xem tới đây thì cho em xin lỗi vì đã sử dụng AI để viết tình huống cho file 
#main.py, vì đã gần tới hạn deadline nên em không kịp thiết kế thêm tình huống, em cảm ơn thầy đã thông cảm
#cho em ạ