# Governance Worksheet & Code Trace

## Data Shared with AI

| Material Shared | Category | Risk Level | Reason |
|---|---|---|---|
| `app/main.py` & `app/models/task.py` code | Codebase Structure | **Low** | Synthetic, non-proprietary educational project code. |
| Terminal execution outputs & Pytest logs | Stack Traces | **Low** | Contains local environment file paths, no real server IP or secrets. |
| `.env.example` template | Configuration | **Low** | Template file containing placeholder variables only. |
| Real database credentials or API keys | Secrets | **High** | *Never shared.* Excluded via `.gitignore` and prompt constraints. |

---

## Data Received from AI

| AI Output Received | Action Taken | Understanding & Review Status |
|---|---|---|
| Pydantic `@field_validator` functions | Adapted | Fully understood after inspecting mode parameter (`mode="before"`). |
| Native Drag-and-Drop JavaScript handlers | Modified | Required manual rewrite (`ondrop`) to fix event listener accumulation. |
| Docker multi-stage build configuration | Accepted | Verified non-root user execution (`whoami`) in running container. |

---

## Line-by-Line Code Trace

Selected Block: `validate_tags` validator in `app/models/task.py`:

```python
1: @field_validator("tags", mode="before")
2: @classmethod
3: def validate_tags(cls, v: Optional[List[str]]) -> List[str]:
4:     if v is None:
5:         return []
6:     if not isinstance(v, list):
7:         raise ValueError("tags must be a list of strings")
8:     sanitized = [tag.strip() for tag in v if isinstance(tag, str) and tag.strip()]
9:     if len(sanitized) > 5:
10:        raise ValueError("cannot have more than 5 tags")
11:    for tag in sanitized:
12:        if len(tag) > 20:
13:            raise ValueError("tag length cannot exceed 20 characters")
14:    return sanitized