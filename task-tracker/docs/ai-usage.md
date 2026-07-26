# Concrete AI Usage Rules for Engineering Teams

1. **Never-Paste Rule:** Developers shall never paste `.env` files, production database credentials, API tokens, PII, or real customer data into an AI prompt window.
2. **Mandatory Verification Rule:** Before accepting any AI-generated code diff, the developer must read every modified line and run the corresponding unit tests (`pytest tests/ -v`) or manual verification commands.
3. **Traceability Rule:** All PR descriptions containing AI-assisted code must list the prompt intent, the generated diff, and the specific verification tests executed.