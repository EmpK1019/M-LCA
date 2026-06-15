#
# Copy this file to api_config.local.py and fill in your keys.
# Supported locations:
# - project root (development)
# - next to M-LCA.exe (installed app)
# - resources/api_config.local.py
# - resources/engine-bin/api_config.local.py
# - %USERPROFILE%/.mlca/api_config.local.py
#

# 两个对等、独立的路由槽（主 / 备用），互不依赖、无降级优先级。
# 每个槽的 Provider 类型可独立设为 "openai"（OpenAI 兼容）或 "anthropic"（Anthropic 原生）。
# 引擎会同时连通已配置 key 的所有路由，把它们的可选模型展示在前端，
# 用户选哪个模型，引擎那次推理就只走对应路由。
PRIMARY_PROVIDER = "openai"
FALLBACK_PROVIDER = "openai"

# 主路由
# - PRIMARY_PROVIDER = "openai" 时填 OpenAI 兼容 key/base，模型名填到 OPENAI_MODEL
# - PRIMARY_PROVIDER = "anthropic" 时填 Anthropic key/base，OPENAI_MODEL 填 Claude 模型名（如 claude-sonnet-4-20250514）
OPENAI_API_KEY = ""
OPENAI_API_BASE = "https://newapi.ecdigit.cn/v1"
OPENAI_MODEL = "gpt-4o-mini"

# 备用路由（与主路由完全对等，根据 FALLBACK_PROVIDER 决定 openai / anthropic）
FALLBACK_API_KEY = ""
FALLBACK_API_BASE = "https://api.deepseek.com/v1"
FALLBACK_MODEL = "deepseek-chat"

# 搜索服务
TAVILY_API_KEY = ""
BRAVE_SEARCH_API_KEY = ""
