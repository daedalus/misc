.PHONY: bootstrap doctor lint format test ci

# Run all first-time setup steps
bootstrap:
	@scripts/bootstrap

# Print environment diagnostic info
doctor:
	@scripts/doctor

# Run linters on shell scripts (and pre-commit if configured)
lint:
	@scripts/lint

# Auto-format shell scripts (and pre-commit if configured)
format:
	@scripts/format

# Run tests (placeholder — add test commands here as the repo grows)
test:
	@echo "No automated tests configured yet."
	@echo "Add test commands to this target as needed."

# Run lint — suitable as a CI check
ci: lint
