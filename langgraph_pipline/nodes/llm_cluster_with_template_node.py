import json
from pathlib import Path
from utils.llm import call_llm

def load_category_template():
  config_path = Path(__file__).resolve().parent.parent.parent / "config" / "category_template.json"
  with open(config_path, "r", encoding="utf-8") as f:
    return json.load(f)

def llm_cluster_with_template_node(state: dict) -> dict:
  tags = state.get("tags", [])
  category_template = load_category_template()

  prompt = f"""
아래는 템플릿 카테고리 목록과 사용자 태그입니다.
각 태그를 가장 적절한 카테고리에 분류해주세요.

카테고리 템플릿:
{json.dumps(category_template, indent=2, ensure_ascii=False)}

사용자 태그:
{tags}

요청:
각 카테고리별로 해당되는 태그만 포함해 JSON으로 출력해 주세요.
카테고리에 맞지 않는 태그는 "기타"에 넣어 주세요.
  """

  result = call_llm(prompt)

  try:
    parsed_result = json.loads(result)
  except json.JSONDecodeError:
    parsed_result = {"기타": tags}

  return {"tag_clusters": parsed_result}
