import uuid
from datetime import datetime, timedelta

import jwt
from fastapi import FastAPI, Form

# 初始化 FastAPI 服务
app = FastAPI(title="OAuth2.0 认证服务器", version="1.0")

# 密钥
SECRET_KEY = "my-super-secret-key-2025"
ALGORITHM = "HS256"

# 模拟数据库：允许的客户端
VALID_CLIENTS = {"test_client_id": "test_client_secret"}


# ==============================================
# 核心接口：获取 Token（client_credentials 模式）
# ==============================================
@app.post("/oauth/token")
def get_token(
    grant_type: str = Form(...),
    client_id: str = Form(...),
    client_secret: str = Form(...),
    refresh_token: str = Form(None),
):
    # 1. 刷新 Token 逻辑
    if grant_type == "refresh_token" and refresh_token:
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
            new_access_token = create_access_token(client_id=payload["sub"])
            return {
                "access_token": new_access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer",
                "expires_in": 600,
            }
        except Exception:
            return {"error": "refresh_token invalid"}

    # 2. 全新获取 Token 逻辑
    if grant_type != "client_credentials":
        return {"error": "unsupported grant_type"}

    # 校验客户端是否合法
    if client_id not in VALID_CLIENTS or VALID_CLIENTS[client_id] != client_secret:
        return {"error": "invalid client"}

    # 生成 Token
    access_token = create_access_token(client_id)
    refresh_token = create_refresh_token(client_id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
        "expires_in": 600,  # 10分钟过期
    }


# ==============================================
# 工具：生成 Access Token
# ==============================================
def create_access_token(client_id: str):
    expire = datetime.utcnow() + timedelta(minutes=10)
    payload = {"sub": client_id, "exp": expire, "jti": str(uuid.uuid4())}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ==============================================
# 工具：生成 Refresh Token
# ==============================================
def create_refresh_token(client_id: str):
    expire = datetime.utcnow() + timedelta(days=7)
    payload = {"sub": client_id, "exp": expire, "jti": str(uuid.uuid4())}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ==============================================
# 测试接口：需要 Token 才能访问
# ==============================================
@app.get("/api/test")
def test_api(token: str):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"status": "success", "msg": "你通过了 OAuth2 认证！"}
    except Exception:
        return {"error": "invalid token"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
