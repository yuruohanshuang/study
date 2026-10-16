from src.api import APIClient
from src.core import APIError

client = APIClient("https://jsonplaceholder.typicode.com", max_retries=1)
client.set_token("<YOUR_ACCESS_TOKEN>")

try:
    users = client.get("/users", params={"_limit": 2})
    print("用户数量:", len(users))

    created = client.post(
        "/posts",
        json_data={
            "title": "API 进阶开发",
            "body": "升级 APIClient",
            "userId": 1,
        },
    )
    print("创建文章 ID:", created.get("id"))

    updated = client.put(
        "/posts/1",
        json_data={
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1,
        },
    )
    print("更新标题:", updated.get("title"))

    deleted = client.delete("/posts/1")
    print("删除结果:", deleted)

    client.get("/not-found")
except APIError as e:
    print("捕获 API 异常:", e)
