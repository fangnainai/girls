# -*- coding:utf -8-*-
#CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护。
# 在大多数情况下，你需要激活该配置使得你的应用程序更安全些。
#SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。
# 当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'