import requests
from config import DEEPSEEK_API_KEY

def analyze_financial_report(report_text, news_summary):
    prompt = f"""
你是一位专业的金融分析师，请综合以下两部分信息，系统分析该公司的财报表现与未来走势：

🧾【财报摘要】
{report_text}

📰【相关新闻摘要】
{news_summary}

请从以下角度输出分析内容，格式使用Markdown：

## 1. 财报关键指标总结
- 概括公司在本期的营收、利润、增长/下滑趋势、指引（guidance）等数据要点。

## 2. 新闻与财报的关联分析
- 新闻中是否有进一步佐证、质疑或补充财报内容？是否影响市场预期？

## 3. 投资者关注点梳理
- 基于当前财报和新闻，指出投资者最应关注的风险与机会因素。

## 4. 总结与评级建议
- 总体判断公司当前经营状态与前景（选择：正面 / 中性 / 负面）
- 给出一个合理的投资评级建议（如：买入 / 观望 / 卖出），并解释理由。

要求内容：
- 使用清晰的结构
- 行文风格参考证券分析师的研报
- 不要输出任何“作为AI我不能”的句子
"""

    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5
        }
    )

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Failed to analysis: {e}"