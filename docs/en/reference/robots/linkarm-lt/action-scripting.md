# LinkArm-LT Action Scripting

Mission files contain one JSON command per line. They can be created in the web console, assigned to buttons, looped, or selected for boot-time execution.

Use delay commands between motion targets when the previous move needs time to complete.

!!! danger "Use boot-time missions carefully"
    A saved boot mission can move the arm as soon as power is applied.

Recommended workflow:

1. Test each JSON command interactively.
2. Use low speed and a clear workspace.
3. Save a short mission.
4. Run it once while ready to remove power.
5. Add loops or boot execution only after repeated safe tests.

See [JSON Command Reference](json-commands.md#mission-files) for mission-management commands.

