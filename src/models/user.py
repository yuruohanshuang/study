from datetime import datetime


class User:
    """用户基类."""

    platform_name = "AI学习平台"
    total_count = 0

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_logged_in = False
        self.is_active = True
        User.total_count += 1

    def login(self) -> bool:
        if not self.is_active:
            print(f"用户 {self.username} 已被禁用，无法登录")
            return False
        self.is_logged_in = True
        print(f"用户 {self.username} 登录成功")
        return True

    def logout(self):
        self.is_logged_in = False
        print(f"用户 {self.username} 已退出")

    def update_email(self, new_email: str) -> bool:
        if "@" not in new_email:
            print("邮箱格式不正确")
            return False
        self.email = new_email
        return True

    def get_profile(self) -> dict:
        return {
            "role": "user",
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "is_logged_in": self.is_logged_in,
            "is_active": self.is_active,
        }


class AdminUser(User):
    """管理员用户."""

    def __init__(self, username: str, email: str, permissions: list[str] | None = None):
        super().__init__(username, email)
        self.permissions = permissions or ["read", "write", "disable_user"]

    def disable_user(self, user: User) -> bool:
        if "disable_user" not in self.permissions:
            print("权限不足")
            return False
        user.is_active = False
        user.is_logged_in = False
        print(f"管理员 {self.username} 禁用了用户 {user.username}")
        return True

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile["role"] = "admin"
        profile["permissions"] = self.permissions
        return profile


class StudentUser(User):
    """学员用户."""

    def __init__(self, username: str, email: str, student_id: str, class_name: str):
        super().__init__(username, email)
        self.student_id = student_id
        self.class_name = class_name
        self.homeworks: list[str] = []

    def submit_homework(self, title: str):
        self.homeworks.append(title)
        print(f"学员 {self.username} 已提交作业: {title}")

    def get_profile(self) -> dict:
        profile = super().get_profile()
        profile.update(
            {
                "role": "student",
                "student_id": self.student_id,
                "class_name": self.class_name,
                "homeworks": self.homeworks,
            }
        )
        return profile
