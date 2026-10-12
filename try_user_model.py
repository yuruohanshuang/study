from src.models import AdminUser, StudentUser, User

# 说明：`__name__` 是 Python 的内置变量。
# 直接运行本文件（python try_user_model.py）时，它的值是 "__main__"，条件成立；
# 当本文件被其他文件 import 时，它的值不是 "__main__"，下面的演示代码不会自动执行。
if __name__ == "__main__":
    user = User("zhangsan", "zhangsan@example.com")
    admin = AdminUser("admin", "admin@example.com")
    student = StudentUser("lisi", "lisi@example.com", "S2026001", "AI应用1班")

    user.login()
    student.login()
    student.submit_homework("Day7-OOP用户模型")
    admin.disable_user(user)

    print("\n--- 普通用户 ---")
    print(user.get_profile())

    print("\n--- 管理员 ---")
    print(admin.get_profile())

    print("\n--- 学员用户 ---")
    print(student.get_profile())

    print(f"\n当前创建用户数: {User.total_count}")
