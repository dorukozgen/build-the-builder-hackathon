# Banking Agent Templates

Moved out of `banking-customer-service-knowledge.md` (formerly sections 15 and 16). Parked for now: the builder does not read this file.

---

# 15. Recommended Agent Definition Template

The task-specific role definitions the Core Builder produces may include the following fields.

```yaml
role_id: "<unique_role_identifier>"
domain: "banking"

purpose: "<agent_purpose>"

scope:
  responsibilities: []
  out_of_scope: []

users:
  target_users: []
  verification_requirements: []

knowledge:
  required_sources: []
  unknown_critical_information: []

capabilities:
  allowed_tools: []
  conditional_tools: []

permissions:
  allowed_actions: []
  conditional_actions: []
  prohibited_actions: []

response_policy:
  answer_when: []
  ask_for_clarification_when: []
  refuse_or_redirect_when: []
  escalate_when: []

failure_handling:
  retry_conditions: []
  stop_conditions: []
  uncertain_result_handling: []

success_criteria: []

test_scenarios: []

unresolved_requirements: []
```

This template is a conceptual starting point. Field names and data structure should be adapted to the existing format of the platform in use.

Filling in the fields of the schema does not prove that the permission has been technically granted. Actual authorization and tool access must be enforced separately.

---

# 16. Recommended Guard MD Template

The Core Builder may produce a Guard MD for each specific agent with a structure similar to the following.

```markdown
# Agent Guard Policy

## 1. Agent Identity
- Role:
- Purpose:
- Scope:

## 2. Responsibilities
- Tasks the agent must perform.

## 3. Allowed Behaviors
- Explicitly permitted behaviors.
- Conditions required before execution.

## 4. Conditional Behaviors
- Required verification.
- Required authorization.
- Required user confirmation.
- Required data availability.

## 5. Prohibited Behaviors
- Actions the agent must not perform.
- Claims the agent must not make.

## 6. Knowledge and Sources
- Approved information sources.
- Information that must be verified.
- Unknown information handling.

## 7. Tool Usage
- Allowed tools.
- Preconditions for each tool.
- Expected results.
- Error handling.

## 8. Response Policy
- When to answer.
- When to ask for clarification.
- When to refuse or redirect.
- When to escalate.

## 9. Privacy and Security
- Data minimization.
- Sensitive information restrictions.
- Authentication and authorization requirements.

## 10. Failure Handling
- API failures.
- Timeouts.
- Ambiguous outcomes.
- Retry conditions.

## 11. Escalation
- Escalation triggers.
- Approved destination.
- Information to include.

## 12. Success Criteria
- Expected behavior.
- Expected final states.

## 13. Examples
- Normal scenario.
- Missing information.
- Unauthorized request.
- Tool failure.
- Out-of-scope request.
```

This template must be filled in anew for each agent. Permissions and tasks belonging to another agent's role must not be copied automatically.
