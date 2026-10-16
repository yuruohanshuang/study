# a = [1,2,3,4]
#
# b = a.append(5)
# c = sorted(a)
#
# print(b)
# print(c)
# def get_stats(nums):
#     return min(nums),max(nums), sum(nums)
#
# lo,hi,total = get_stats([3,1,4])
# print(f"lo: {lo}, hi: {hi}, total: {total}")
# from unittest import result
# from curses import wrapper
# import functools
# import time


# nums = [3,1,2,3,1]
# print(set(nums),sorted(set(nums)))

# items = ["1", "2", "x", "3", "y"]

# n = 5
# total = 0
# while n > 0:
#     total += n
#     n -= 1
# print(total)
# nums = [1,2,3,4,5,6]
# print(nums[::2],nums[::-1])

# squares = {x:x**2 for x in range(1,4)}
# print(squares[3],len(squares))
# s = "hello"
# S = s.replace("l","L")
# print(s,S)
# t = "Date.CSV".strip().lower()
# print(t.endswith(".csv"),t.startswith("date"))
# d = {"a":1,"b":2}
# for k in d:
#     d[k] = d[k]*10
# print(d)

# d = {"a": 1,"b": 2}
# del d["b"]
# print(len(d),d.get("b",0))
# with open("test.txt","w",encoding="utf-8") as f:
#     f.write("A")
# with open("test.txt","a",encoding="utf-8") as f:
#     f.write("B")
# with open("test.txt","r",encoding="utf-8") as f:
# #     print(f.read())
# # print(int("7")+float("3.5"),str(3)*2)
# print(sorted(["10","9","2"]))
# lst = [1,2,3]
# print(lst[1:99],lst[99:100])
# a=[[1,2],[3,4]]
# b=a[:]
# b[0][0]=100
# print(a,b)
# nums = [3,1,2]
# result = sorted(nums,reverse=True)
# print(result)
# print([1,2,3]*2)
# lst = [1,2]
# lst.extend(5)
# print(lst)
# d = {"a":1,"a":2}
# print(d["a"])

# def circle_info(r: float) -> tuple[float, float]:
#     """计算圆的周长和面积
#
#     Args:
#         r (float): 圆的半径
#
#     Returns:
#         tuple[float, float]: 圆的周长和面积
#
#     Example:
#     >>> circle_info(1)
#     (6.28318, 3.14159)
#     """
#     a = 3.14159
#     l = 2 * a * r
#     s = a * r ** 2
#     return l, s
#
# result = circle_info(5)
# print(result)
# print(type(result))
# def send_email(to,subject="无主题",*,body):
#     print(f"发送给{to},主题:{subject},正文:{body}")
#
# try:
#     send_email(12334,body="hello")
# except TypeError:
#     print("send_email中body参数必须使用关键字传递")
#
#
# try:
#     send_email(12334,subject="测试",body="hello")
# except TypeError:
#     print("send_email中body参数必须使用关键字传递")
#
#
# try:
#     send_email(12334,"测试","hello")
# except TypeError:
#     print("send_email中body参数必须使用关键字传递")
#
# def add_item(item,items=None):
#     """默认值[]会在函数定义时创建一次，后续调用会共享同一个列表，导致意外的结果。"""
#     if items is None:
#         items = []
#     items.append(item)
#     return items
# print(add_item(1))
# print(add_item(2))
# def calc_stats(*args)-> dict:
#     """返回 count/sum/avg/max/min 五项统计."""
#     print(args)
#     print(type(args).__name__)
#     if not args:
#         return {"count": 0, "sum": 0, "avg": None, "max": None, "min": None}
#     return {
#         "count": len(args),
#         "sum": sum(args),
#         "avg": sum(args) / len(args),
#         "max": max(args),
#         "min": min(args),
#     }
#
# print(calc_stats(10,20,30))
# print(calc_stats(*[10,20,30]))
# print(calc_stats())

# def make_counter(start=0):
#     count = start
#     def step(delta=1):
#         nonlocal count
#         count += delta
#         return count
#     return step
# c1 = make_counter()
# print(c1())
# print(c1())
# c2 = make_counter(100)
# print(c2(5))
# print(c2(5))
#
# counter = 0
# def bad():
#     counter = counter +1
#     return counter
# try:
#     bad()
# except UnboundLocalError as e:
#     print("bad()函数中counter变量未定义:", e)
#
# def good():
#     global counter
#     counter += 1
#     return counter
#
# print(good())
# print(good())
# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier
# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5))
# print(triple(5))
#
# def apply(func,value):
#     return func(value)
# print(apply(double,21))
#
# students = [("张三", 85,"北京"), ("李四", 92,"上海"),
# ("王五", 78,"北京"), ("赵六", 88,"广州")]
#
# print(sorted(students, key=lambda x: x[1], reverse=True))
# #sorted的key参数指定一个函数，用于从每个元素中提取一个比较键
# print(list(filter(lambda x:x[2]=="北京", students)))
# print(list(map(lambda x:x[0], students)))

# def add_item(item, items=[]):
#     """默认值[]会在函数定义时创建一次，后续调用会共享同一个列表，导致意外的结果。"""
#     items.append(item)
#     return items
# print(add_item(1))
# print(add_item(2))
# lst = [1, 2, 3]
#
# lst = lst.append(4)
#
# print(lst)

# def log_it(func):
#     def wrapper(*args, **kwargs):
#         print(f"调用函数 {func.__name__}，参数: {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"函数 {func.__name__} 返回值: {result}")
#         return result
#     return wrapper
#
# @log_it
# def add(a, b):
#     return a + b
#
# print(add(2, 3))
# print(add(10,20))

# def timer(precision=2):
#     time.perf_counter()
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time.perf_counter()
#             result = func(*args, **kwargs)
#             end = time.perf_counter()
#             print(f"函数 {func.__name__} 执行时间: {end - start:.{precision}f} 秒")
#             return result
#         return wrapper
#     return decorator
#
# @timer(precision=2)
# def slow_sum():
#     total = sum(range(1_000_000))
#     time.sleep(0.2)
#     return total
# print(slow_sum.__name__)
# print(slow_sum())

# def counter_gen(n):
#     """生成一个计数器，返回一个生成器对象，每次调用next()都会返回下一个计数值，直到达到n为止。"""
#     for i in range(n):
#         yield i
# g = counter_gen(3)
# print(next(g))
# print(next(g))
# print(next(g))
# try:
#     print(next(g))
# except StopIteration as e:
#     print("生成器已结束:", e)
# squares = (x*x for x in [1, 2, 3])
#
# print("第一次list():", list(squares))
# print("第二次list():", list(squares))

# def fake_read_lines(lines):
#     """模拟读取文件的每一行，返回一个生成器对象，每次调用next()都会返回下一行，直到没有更多行。"""
#     for line in lines:
#         yield line
# def filter_errors(lines):
#     """过滤掉包含"ERROR"的行，返回一个生成器对象，每次调用next()都会返回下一行，直到没有更多行。"""
#     for line in lines:
#         if "ERROR" not in line:
#             yield line
# def add_prefix(lines, tag):
#     """为每一行添加前缀，返回一个生成器对象，每次调用next()都会返回下一行，直到没有更多行。"""
#     for line in lines:
#         yield f"{tag}{line}"
#
# LOG_LINES = [
#     "INFO: This is an info message.",
#     "ERROR: This is an error message.",
#     "INFO: Another info message.",
#     "ERROR: Another error message.",]
#
# pipe = add_prefix(filter_errors(fake_read_lines(LOG_LINES)), 'ERR')
# print("过滤掉包含'ERROR'的行，并为每一行添加前缀:")
# for line in pipe:
#     print(line)
# def retry(max_retries=3, delay=0.1,exceptions=(Exception,)):
#     """重试装饰器，允许在函数调用失败时自动重试指定次数。"""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for attempt in range(max_retries):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     print(f"尝试 {attempt + 1} 失败: {e}")
#                     time.sleep(delay)
#                     if attempt == max_retries - 1:
#                         raise
#         return wrapper
#     return decorator
#
# count = 0
#
# @retry(max_retries=3, delay=0.1, exceptions=(ValueError,))
# def flaky():
#     global count
#     count += 1
#     if count < 3:
#         raise ValueError("网络波动")
#     return "成功"
# print(flaky())
#
# @retry(max_retries=3, delay=0.1)
# def always_fail():
#     raise ConnectionError("服务不可用")
# try:
#     always_fail()
# except ConnectionError as e:
#     print("最终捕获异常：", e)
#
# @functools.lru_cache(maxsize=None)
# def fibonacci(n):
#     if n <= 1:
#         return n
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print("fibonacci(20) =", fibonacci(20))
# print("缓存信息：", fibonacci.cache_info())

# class User:
#     platform_name = "AI学习平台"
#     total_count = 0
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email
#         self.is_logged_in = False
#         self.is_active = True
#         User.total_count += 1
#
#     def login(self):
#         if not self.is_active:
#             print(f"用户 {self.username} 已被禁用，无法登录")
#             return False
#         self.is_logged_in = True
#         print(f"用户 {self.username} 登录成功")
#         return True
#
#     def logout(self):
#         self.is_logged_in = False
#
#     def get_profile(self):
#         return {
#             "role": "user",
#             "username": self.username,
#             "email": self.email,
#             "is_logged_in": self.is_logged_in,
#             "is_active": self.is_active,
#         }
#
# user1 = User("zhangsan", "zhangsan@example.com")
# user2 = User("lisi", "lisi@example.com")
# user1.login()
# user2.login()
# print(user1.get_profile())
# print(user2.get_profile())
# print(f"当前创建用户数: {User.total_count}")

# class User:
#     def __init__(self,username,email,phone=""):
#         self.username = username
#         self.email = email
#         self.phone = phone
#         self.is_logged_in = False
#         self.is_active = True
#
#     def update_email(self,new_email)-> bool:
#         if "@" not in new_email:
#             print("邮箱格式不正确")
#             return False
#         self.email = new_email
#         return True
#     def update_phone(self,new_phone)-> bool:
#         if len(new_phone) != 11 or not new_phone.isdigit():
#             print("手机号格式不正确")
#             return False
#         self.phone = new_phone
#         return True
#     def get_profile(self)-> dict:
#         return {
#             "username": self.username,
#             "email": self.email,
#             "phone": self.phone,
#             "is_logged_in": self.is_logged_in,
#             "is_active": self.is_active,
#         }
#
# user1 = User("zhangsan", "zhangsan@example.com", "13800138000")
# print(user1.update_email("valid@example.com"))
# print(user1.update_phone("13900139000"))
# print(user1.update_phone("123"))
# print(user1.get_profile())
#
# class User:
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email
#         self.is_logged_in = False
#         self.is_active = True
#
#     def get_profile(self) -> dict:
#         return {
#             "role": "user",
#             "username": self.username,
#             "email": self.email,
#             "is_logged_in": self.is_logged_in,
#             "is_active": self.is_active,
#         }
#
# class AdminUser(User):
#     def __init__(self, username: str, email: str, permissions: list[str] | None = None):
#         super().__init__(username,email)
#         self.permissions = permissions or ["read","write","disable_user"]
#
#     def disable_user(self,user: User) -> bool:
#         user.is_active = False
#         user.is_logged_in = False
#         print(f"管理员 {self.username} 禁用了用户 {user.username}")
#         return True
#
#     def get_profile(self) -> dict:
#         profile = super().get_profile()
#         profile["role"] = "admin"
#         profile["permissions"] = self.permissions
#         return profile
#
# class StudentUser(User):
#     def __init__(self, username: str, email: str, student_id: str):
#         super().__init__(username,email)
#         self.student_id = student_id
#         self.homeworks: list[str] = []
#
#     def submit_homework(self, title: str) -> bool:
#         self.homeworks.append(title)
#         print(f"学员 {self.username} 提交了作业: {title}")
#         return True
#
#     def get_profile(self) -> dict:
#         profile = super().get_profile()
#         profile.update({
#             "role": "student",
#             "student_id": self.student_id,
#             "homeworks": self.homeworks
#         })
#         return profile
#
# class Course:
#     def __init__(self, title: str, teacher: str):
#         self.title = title
#         self.teacher = teacher
#     def get_profile(self) -> dict:
#         return {
#             "role": "course",
#             "title": self.title,
#             "teacher": self.teacher
#         }
#
# def print_profile(obj):
#     profile = obj.get_profile()
#     print(f"--- {profile['role'].capitalize()} Profile ---")
#     for key, value in profile.items():
#         if key != "role":
#             print(f"{key}: {value}")
#     print()
#
# user1 = User("user1", "user1@example.com")
# admin1 = AdminUser("admin1", "admin1@example.com")
# student1 = StudentUser("student1", "student1@example.com", "S001")
# course1 = Course("Python Programming", "Prof. Smith")
# print_profile(user1)
# print_profile(admin1)
# print_profile(student1)
# print_profile(course1)
# student1.submit_homework("作业1")
# print(student1.get_profile())
# print(admin1.get_profile())

# class User:
#     platform_name = "AI学习平台"
#     default_role = "user"
#     total_count = 0
#
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email
#         self.is_logged_in = False
#         User.total_count += 1
#
#     def get_profile(self):
#         return {
#             "role": self.default_role,
#             "username": self.username,
#             "email": self.email,
#             "is_logged_in": self.is_logged_in,
#         }
# user1 = User("user1", "user1@example.com")
# user2 = User("user2", "user2@example.com")
# print(user1.get_profile()["role"])
# print(user2.get_profile()["role"])
# User.default_role = "member"
# user3 = User("user3", "user3@example.com")
# print(user1.get_profile()["role"])
# print(user3.get_profile()["role"])
#
# user1.custom_tag = "VIP"
# print(user1.custom_tag)
# print("user2是否有custom_tag:", hasattr(user2, "custom_tag"))
# print("用户总数:", User.total_count)

# class AppConfig:
#     tags = []
# a = AppConfig()
# b = AppConfig()
# a.tags.append("new")
# print(b.tags)  # Output: ['new']
