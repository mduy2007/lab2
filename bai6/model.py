from abc import ABC, abstractmethod
from typing import List

class LibraryError(Exception):
    """Ngoại lệ tùy chỉnh dùng để bắt các lỗi nghiệp vụ trong thư viện"""
    pass

class LibraryItem(ABC):
    """
    Lớp trừu tượng đại diện cho một tài liệu trong thư viện.
    """
    def __init__(self, item_id, title):
        """
        Khởi tạo tài liệu.
        item_id: Mã tài liệu
        title: Tiêu đề tài liệu
        """
        self.item_id = item_id
        self.title = title
        self.__is_available = True  # Thuộc tính private

    @property
    def is_available(self):
        """Getter cho trạng thái sẵn có của tài liệu"""
        return self.__is_available

    def set_availability(self, status):
        """Setter để thay đổi trạng thái sẵn có của tài liệu"""
        self.__is_available = status

    @abstractmethod
    def loan_days(self):
        """Phương thức trừu tượng trả về số ngày mượn tối đa"""
        pass

    @abstractmethod
    def display_info(self):
        """Phương thức trừu tượng hiển thị thông tin tài liệu"""
        pass


class Book(LibraryItem):
    """Lớp đại diện cho Sách, kế thừa từ LibaryItem"""
    def __init__(self, item_id, title, author):
        """
        Khởi tạo sách
        author: Tên tác giả
        """
        super().__init__(item_id, title)
        self.author = author

    def loan_days(self):
        """sách được mượn tối đa 14 day"""
        return 14

    def display_info(self):
        """Hiển thị thông tin chi tiết của sách"""
        status = "Có sẵn" if self.is_available else "Đã mượn"
        print(f"[Sách] ID: {self.item_id} | Tiêu đề: {self.title} | Tác giả: {self.author} "
              f"| Trạng thái: {status} | Số ngày mượn tối đa: {self.loan_days()} ngày")


class Magazine(LibraryItem):
    """Lớp đại diện cho Tạp chí, kế thừa từ LibraryItem"""
    def __init__(self, item_id, title, issue):
        """
        Khởi tạo tạp chí
        issue: Số phát hành
        """
        super().__init__(item_id, title)
        self.issue = issue

    def loan_days(self):
        """Tạp chí được mượn tối đa 7 days."""
        return 7

    def display_info(self):
        """Hiển thị thông tin chi tiết của tạp chí."""
        status = "Có sẵn" if self.is_available else "Đã mượn"
        print(f"[Tạp chí] ID:{self.item_id} | Tiêu đề: {self.title} | Số phát hành: {self.issue} "
              f"| Trạng thái: {status} | Số ngày mượn tối đa: {self.loan_days()} ngày")


class Member:
    """Lớp đại diện cho Thành viên thư viện"""
    def __init__(self, member_id: str, name: str):
        """
        Khởi tạo thành viên
        member_id: Mã thành viên
        name: Tên thành viên
        """
        self.member_id = member_id
        self.name = name
        self.borrowed_items: List[LibraryItem] = []  # Danh sách các tài liệu đang mượn

    def can_borrow(self):
        """Kiểm tra xem thành viên có thể mượn thêm tài liệu không"""
        return len(self.borrowed_items) < 3

    def has_borrowed(self, item: LibraryItem):
        """Kiểm tra xem thành viên có đang mượn tài liệu này không"""
        return item in self.borrowed_items


class Library:
    """Lớp quản lý kho tài liệu và các thành viên"""
    def __init__(self):
        """Khởi tạo thư viện với kho tài liệu và danh sách thành viên rỗng"""
        self.items: List[LibraryItem] = []
        self.members: List[Member] = []

    def add_item(self, item: LibraryItem):
        """Thêm tài liệu"""
        self.items.append(item)

    def add_member(self, member: Member):
        """Thêm thành viên"""
        self.members.append(member)

    def borrow(self, member: Member, item: LibraryItem):
        """
        Xử lý nghiệp vụ mượn tài liệu
        Ném ra LibraryError nếu vi phạm quy định
        """
        if item not in self.items:
            raise LibraryError("Tài liệu này không thuộc thư viện")
        
        if not item.is_available:
            raise LibraryError(f"Tài liệu {item.title} đang được người khác mượn")
            
        if not member.can_borrow():
            raise LibraryError(f"Thành viên {member.name} đã mượn đủ 3 tài liệu, không thể mượn thêm")
            
        # Thực hiện mượn
        item.set_availability(False)
        member.borrowed_items.append(item)
        print(f"Thành công: Thành viên {member.name} đã mượn tài liệu {item.title}")

    def return_item(self, member: Member, item: LibraryItem):
        """
        Xử lý nghiệp vụ trả tài liệu
        Ném ra LibraryError nếu vi phạm quy định
        """
        if not member.has_borrowed(item):
            raise LibraryError(f"Lỗi: Thành viên {member.name} không mượn tài liệu {item.title} này")
            
        # Thực hiện trả
        item.set_availability(True)
        member.borrowed_items.remove(item)
        print(f"Thành công: Thành viên {member.name} đã trả tài liệu {item.title}")

    def search(self, keyword: str):
        """Tìm kiếm tài liệu theo Mã hoặc Tiêu đề"""
        results = [item for item in self.items if keyword.lower() in item.item_id.lower() or keyword.lower() in item.title.lower()]
        if not results:
            print(f"không tìm thấy tài liệu nào với từ khóa {keyword}")
        else:
            print(f"Kết quả tìm kiếm cho '{keyword}':")
            for item in results:
                item.display_info()

    def display_all_items(self):
        """In danh sách toàn bộ tài liệu trong thư viện"""
        print("\nDANH SÁCH TOÀN BỘ TÀI LIỆU")
        if not self.items:
            print("Thư viện chưa có tài liệu nào")
        for item in self.items:
            item.display_info()
        print("\n")