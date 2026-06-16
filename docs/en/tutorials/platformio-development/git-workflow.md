# Use a Git Development Workflow

## Start from a Known State

```bash
git status
git switch -c feature/my-change
```

Use a short cycle:

1. Make one focused change.
2. Build the project.
3. Test the smallest relevant hardware behavior.
4. Review `git diff`.
5. Commit the working state.

```bash
git add <files>
git commit -m "Describe the behavior change"
```

Do not commit `.pio/`, editor caches, serial logs, credentials, or generated firmware unless the repository explicitly tracks release artifacts.

Resolve conflicts by understanding both versions, then rebuild and retest. For hardware projects, a textually clean merge is not proof that pin assignments, timing, or startup behavior remain safe.

