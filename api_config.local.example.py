#
# Copy this file to api_config.local.py and fill in your keys.
# Supported locations:
# - project root (development)
# - next to M-LCA.exe (installed app)
# - resources/api_config.local.py
# - resources/engine-bin/api_config.local.py
# - %USERPROFILE%/.mlca/api_config.local.py
#

# 路由 Provider 类型: "openai"（OpenAI 兼容）或 "anthropic"（Anthropic 原生）
PRIMARY_PROVIDER = "openai"
FALLBACK_PROVIDER = "openai"

# 主路由（当 PRIMARY_PROVIDER = "openai" 时填 OpenAI 兼容 key/base）
# （当 PRIMARY_PROVIDER = "anthropic" 时填 Anthropic key/base）
OPENAI_API_KEY = ""
OPENAI_API_BASE = "https://newapi.ecdigit.cn/v1"
OPENAI_MODEL = "gpt-4o-mini"

# 备用路由（同理，根据 FALLBACK_PROVIDER 决定解释方式）
FALLBACK_API_KEY = ""
FALLBACK_API_BASE = "https://api.deepseek.com/v1"
FALLBACK_MODEL = "deepseek-chat"

# 独立 Anthropic 路由（仅当主路由不是 anthropic 时作为中间降级）
ANTHROPIC_API_KEY = ""
ANTHROPIC_API_BASE = "https://api.anthropic.com"
ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

# 搜索服务
TAVILY_API_KEY = ""
BRAVE_SEARCH_API_KEY = ""
