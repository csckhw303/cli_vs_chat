# Possible Token Save Comparison Example CLI vs CHAT environment (Visual Studio Code + GitHub Copilot)

A sandbox demonstration framework designed to measure, analyze, and optimize LLM token consumption profiles. This repository establishes a programmatic testing playground to compare the token economics of **IDE Chat Sidebars (Bulk Context Ingestion)** against **Command Line / Terminal Inline Interfaces (Precision Targeted Ingestion)**.

## Project Architecture

```text
├── logs/
│   └── server.log              # Generated 15,000-line token-heavy simulation target
├── src/
│   ├── components/
│   │   └── MemberCardView.cs   # Downstream consumer component dependency
│   └── services/
│       └── OldMemberService.cs # Core domain service component containing validation bounds
├── setup_benchmark.py          # Python sandbox automation script
└── README.md                   # System testing documentation
```

---

## Pre-Test Diagnostics & Environment Setup

To allow observability extensions (e.g., **AI Engineering Fluency**) or internal telemetry buffers to intercept exact token payload values inside **VS Code**, elevate your environment logging:

1. Open VS Code Settings (`Ctrl+,` or `Cmd+,`).
2. Search for `github.copilot.logLevel`.
3. Set the global dropdown configuration level to **`Debug`** or **`Trace`**.
4. Open the Command Palette (`Ctrl+Shift+P`), select `Developer: Set Log Level...`, isolate `GitHub Copilot Chat`, and switch to **`Trace`**.

---

## The 3 Diagnostic Test Cases

### Test Case 1: Precision Targeted Log Triage
* **Objective:** Isolate a specific runtime crash out of a massive text block without overflowing the context buffer.
* **Chat Sidebar Approach (Token-Heavy):** 
  Prompt the panel using active indexing flags: 
  ```
  `@workspace /explain look at #file:server.log and find out what caused the critical NullPointerException exception.`
  ```
  * *Behavior:* Ingests all 15,000 rows into the active frame window (**~120,000+ input tokens**).
* **Terminal Shell Approach (Precision Compact Ingestion):** 
  Execute local CPU preprocessing before hitting the network using Windows PowerShell stream utilities:
  ```
  grep -C 3 "NullPointerException" logs/server.log | gh copilot explain
  or
  grep -C 3 "NullPointerException" logs/server.log
  Highlight the explicit `[CRITICAL]` output line, press `Ctrl+I` to call the inline interface, and run `Explain this error`.

--- 

### Test Case 2: Source Code Reviews on Incremental Deltas
* **Objective:** Review a quick security adjustment or boundary-validation rewrite for logical bugs.
* **Preparation:** Modify line 124 inside `src/services/OldMemberService.cs` from `if (memberId <= 0)` to `if (memberId <= -999)`.
* **Chat Sidebar Approach (Token-Heavy):**
  Prompt the panel:
  ```
  `Review my changes inside #file:OldMemberService.cs for potential security or indexing vulnerabilities.`
  ```
  * *Behavior:* Packages the entire structural class boilerplate into the tracking log payload.
* **Terminal Shell Approach (Precision Compact Ingestion):**
  Generate a tight diff stream natively inside your terminal window:
  ```
  git diff | copilot -i "Review these changes for security flaws" 
  or
  git diff
  Highlight the exact red/green lines, press `Ctrl+I`, and prompt: `Review this diff for security flaws`.
  ```
  * *Behavior:* Filters out fixed file structures, passing only modified row lines directly to the LLM backend.



---

## Token Comparison Metrics Reference Ledger


| Case | Chat Environment Prompt | Usage | CLI Environment Command / Steps | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1:Log Triage**<br>• Create big log file using the python file provided.<br>• Run the test case experiment. | `@workspace /explain look at #file:server.log and find out what caused the critical NullPointerException exception.` | **6.7 credits** | `grep -C 3 "NullPointerException" logs/server.log \| gh copilot explain`<br><br>**OR**<br><br>• Run: `grep -C 3 "NullPointerException" logs/server.log`<br>• Highlight error lines in terminal.<br>• Prompt via Inline (`Ctrl+I`): *"Explain this specific error output"* | **0.6 credits** |
| **Case 2:Code Review**<br>• Open sandbox file `src/services/OldMemberService.cs`<br>• Modify line 124 from `if (memberId <= 0)...` to `if (memberId <= -999)...`<br>• Run the test case experiment. | `Review my changes inside #file:OldMemberService.cs for potential security, logic, or edge-case validation vulnerabilities.` | **5.7 credits** | • git diff \|  copilot -i "Review these changes for security flaws" or `git diff`<br>• Highlight terminal lines or use active context frame.<br>• Prompt via Inline (`Ctrl+I`): *"Review this diff for security flaws"* | **0.9 credits** |

