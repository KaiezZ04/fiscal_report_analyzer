from report_parser import extract_report_text
from news_crawler import get_financial_news
from financial_analyzer import analyze_financial_report

# 设置 财报PDF路径,股票代码,公司名称
# pdf_path = 替换为你自己的 PDF 文件名
# ticker = 输入的的股票代码
# company_name = 添加公司名称

pdf_path = "替换为你自己的 PDF 文件名"
ticker = "输入的的股票代码"
company_name = "Unity Software Inc"

report_text = extract_report_text(pdf_path)
if not report_text:
    print("❌ Unable to extract financial report content")
    exit()

news_summary = get_financial_news(ticker, company_name)

analysis_result = analyze_financial_report(report_text, news_summary)

filename = f"{company_name}_Financial_Report_Analysis.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(analysis_result)

print("Fully analyzed, generating the report")
