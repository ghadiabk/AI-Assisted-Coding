
## Reflection


## AI Tooling & Workflow
Throughout this project, I used gemini for the planning part (Module 1) since i had the pro subscription giving me alot of room with tokens.
I proceeded with using vs code with github copilot for Module 2 using the student plan but the tokens ran out midway through the module since the student plan is only 200 tokens a month so i continued with google ai studio which has much more generous limits using gemini 3.5 flash and recently  3.6 flash which was enough to complete module 2, 3 and the mid course project successfully.

## Where AI Acceleration Helped
The AI assistant accelerated development when expanding the FastAPI controller endpoints and writing Pydantic v2 model field validators. Specifying precise constraints (such as `Optional[List[str]]`, `@field_validator`, and explicit sanitization rules) allowed the AI to generate structured validation logic quickly. This reduced setup time and let me focus on testing edge cases.

## Where AI Caused Friction
A notable issue occurred during frontend integration. When configuring drag-and-drop event listeners inside a repeatedly called rendering function (`renderBoard`), the AI used standard `.addEventListener()` syntax without considering listener accumulation. Each re-render attached duplicate event listeners to the DOM elements. 

When a user dragged a card, the first listener moved the task and received an HTTP 200 success response. However, the duplicate listener immediately fired a second request for the same status transition. The backend evaluated this second request as an invalid same-to-same status transition and returned an HTTP 422 error, producing confusing error alerts in the browser despite the initial drag succeeding.

## The Role of Developer Inspection
My review process resolved this issue. By analyzing the Uvicorn terminal logs and noticing alternating `200 OK` and `422 Unprocessable Entity` entries for single drag events, I diagnosed the duplicate event listener accumulation. I replaced the generic `.addEventListener()` calls with direct property assignments (`element.ondrop = ...`), ensuring old event handlers were overwritten on every draw cycle.

This experience reinforced the core course mindset: AI coding tools generate plausible code based on patterns, but they do not execute or verify runtime behavior. Disciplined inspection, running the server locally, observing DevTools evidence, and using Break Tests remain the developer's responsibility.