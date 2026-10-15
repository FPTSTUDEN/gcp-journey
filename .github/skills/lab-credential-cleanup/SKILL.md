---
name: lab-credential-cleanup
description: "Review and clean up Google Cloud credentials created specifically for a completed lab, including temporary gcloud accounts or configurations. Use at the end of a lab; preserve personal accounts and unrelated ADC."
---

# Clean up lab-specific credentials

1. Determine what authentication state existed before the lab, if known, and which account or configuration was created or selected specifically for the lab. Do not put account details, tokens, or credential values in lab history.
2. Inspect the current gcloud configuration and authenticated accounts using targeted commands such as `gcloud config configurations list`, `gcloud config list`, and `gcloud auth list`. Do not print or copy credential-file contents.
3. Identify the exact lab-specific account/configuration and any temporary credential state. Do not infer that an account is lab-only merely because it is currently active or has a lab-looking email address.
4. When the account is clearly identified as created specifically for the lab, revoke only that account with `gcloud auth revoke <ACCOUNT>`. The lab-assistant instruction authorizes this targeted cleanup. Never use `gcloud auth revoke --all`.
5. Remove or switch away from a gcloud configuration only when it was created specifically for this lab. Preserve the configuration that was active before the lab when known. Do not delete the default configuration or change shared configuration to hide an uncertain state.
6. Treat ADC separately from gcloud CLI account credentials. Do not run `gcloud auth application-default revoke` unless ADC was created specifically for this lab and the user authorized its removal.
7. Verify the resulting authentication and active configuration state with `gcloud auth list` and `gcloud config list`. Report what was cleaned, what was preserved, and anything that could not be safely determined.
8. If the account or cleanup scope is unclear, make no credential changes. Explain the ambiguity and ask one focused question.
