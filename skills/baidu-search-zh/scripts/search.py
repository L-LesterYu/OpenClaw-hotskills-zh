import sys
import json
import requests
import os
import re
from datetime import datetime, timedelta


def baidu_search(api_key, requestBody: dict):
    url = "https://qianfan.baidubce.com/v2/ai_search/web_search"

    headers = {
        "Authorization": "Bearer %s" % api_key,
        "X-Appbuilder-From": "openclaw",
        "Content-Type": "application/json"
    }

    # 使用POST方法发送JSON数据
    response = requests.post(url, json=requestBody, headers=headers)
    response.raise_for_status()
    results = response.json()
    if "code" in results:
        raise Exception(results["message"])
    datas = results["references"]
    keys_to_remove = {"snippet"}
    for item in datas:
        for key in keys_to_remove:
            if key in item:
                del item[key]
    return datas


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python baidu_search.py <JSON参数>")
        sys.exit(1)

    query = sys.argv[1]
    parse_data = {}
    try:
        parse_data = json.loads(query)
        print(f"成功解析请求参数: {parse_data}")
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")

    if "query" not in parse_data:
        print("错误: 请求参数中必须包含 query 字段。")
        sys.exit(1)
    count = 10
    search_filter = {}
    if "count" in parse_data:
        count = int(parse_data["count"])
        if count <= 0:
            count = 10
        elif count > 50:
            count = 50
    current_time = datetime.now()
    end_date = (current_time + timedelta(days=1)).strftime("%Y-%m-%d")
    pattern = r'\d{4}-\d{2}-\d{2}to\d{4}-\d{2}-\d{2}'
    if "freshness" in parse_data:
        if parse_data["freshness"] in ["pd", "pw", "pm", "py"]:
            if parse_data["freshness"] == "pd":
                start_date = (current_time - timedelta(days=1)).strftime("%Y-%m-%d")
            if parse_data["freshness"] == "pw":
                start_date = (current_time - timedelta(days=6)).strftime("%Y-%m-%d")
            if parse_data["freshness"] == "pm":
                start_date = (current_time - timedelta(days=30)).strftime("%Y-%m-%d")
            if parse_data["freshness"] == "py":
                start_date = (current_time - timedelta(days=364)).strftime("%Y-%m-%d")
            search_filter = {"range": {"page_time": {"gte": start_date, "lt": end_date}}}
        elif re.match(pattern, parse_data["freshness"]):
            start_date = parse_data["freshness"].split("to")[0]
            end_date = parse_data["freshness"].split("to")[1]
            search_filter = {"range": {"page_time": {"gte": start_date, "lt": end_date}}}
        else:
            print(f"错误: freshness 参数 ({parse_data['freshness']}) 必须是 pd、pw、pm、py 或符合格式 {pattern}。")
            sys.exit(1)

    # 通过环境变量传递敏感信息
    api_key = os.getenv("BAIDU_API_KEY")

    if not api_key:
        print("错误: 请在环境变量中设置 BAIDU_API_KEY。")
        sys.exit(1)

    request_body = {
        "messages": [
            {
                "content": parse_data["query"],
                "role": "user"
            }
        ],
        "search_source": "baidu_search_v2",
        "resource_type_filter": [{"type": "web", "top_k": count}],
        "search_filter": search_filter
    }
    try:
        results = baidu_search(api_key, request_body)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)
