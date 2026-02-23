# misc

A collection of miscellaneous scripts, tools, and experiments.

Topics covered include cryptography, Bitcoin/blockchain tooling, security research, networking utilities, system administration, mathematics, and general utilities.

## Quickstart

```bash
# First-time setup (checks tools, makes scripts executable, creates .env)
make bootstrap

# Check your environment
make doctor

# Run linters
make lint
```

## Directory Layout

```
misc/
├── bin/            User-facing commands (added to PATH)
├── scripts/        Internal helper scripts (bootstrap, doctor, lint, format)
├── crypto/         Cryptographic algorithms, primitives, and tests
│                   (AES, RSA, ECDSA, DH, TOTP, PRNG, hashes, encoding)
├── bitcoin/        Bitcoin and blockchain tools
│                   (address utilities, node scanners, miners, FactorDB)
├── security/       Security research and offensive tooling
│                   (CVE PoCs, network reconnaissance, forensics, credential tools)
├── networking/     Networking utilities
│                   (DNS, FTP, Docker Swarm, iptables, Tor, JSON-RPC)
├── sysadmin/       System administration scripts
│                   (backups, storage, VM management, Android, package setup)
├── math/           Mathematics and computer science experiments
│                   (LFSR, IEEE-754, ALU, number theory, combinatorics)
├── utils/          General-purpose utilities and tests
│                   (compression, data encoding, file tools, ML helpers)
└── examples/       Example images used in demonstrations
```

### Conventions

| Directory  | Purpose |
|------------|---------|
| `bin/`     | User-facing commands intended to be on `PATH` |
| `scripts/` | Internal repo helpers (bootstrap, doctor, lint, format) |

## Tooling

All common tasks are driven by the `Makefile`. The scripts live in `scripts/`.

| Target            | Description |
|-------------------|-------------|
| `make bootstrap`  | Verify required tools, make scripts executable, create `.env` |
| `make doctor`     | Print versions and warn about missing tools |
| `make lint`       | Run shellcheck / shfmt (or pre-commit if configured) |
| `make format`     | Auto-format shell scripts with shfmt (or pre-commit) |
| `make test`       | Run tests (placeholder — add commands as repo grows) |
| `make ci`         | Alias for `make lint` — used in CI |

## Running Scripts

Most scripts are standalone and can be run directly:

```bash
# Python scripts
python crypto/simple_sha256.py
python math/ackermann.py

# Shell scripts
bash sysadmin/fastcommit.sh
bash security/certfinder.sh example.com
```

Some scripts require third-party dependencies. Install them with:

```bash
pip install -r requirements.txt
```

See each script's header comment for specific usage instructions and any additional dependencies.

## Requirements

- Python 3.6+
- Various third-party packages (see `requirements.txt`)
- Some shell scripts require Linux-specific tools (e.g., `cryptsetup`, `virsh`, `nmap`)

---

## DISCLAIMER

> **Security & Offensive Tooling — Authorized and Educational Use Only**
>
> Several scripts in this repository (particularly under `security/`, `crypto/`, and `bitcoin/`) implement or demonstrate offensive security techniques, cryptographic attacks, vulnerability proofs-of-concept, credential extraction methods, and network reconnaissance tools.
>
> **These scripts are provided strictly for:**
> - Authorized penetration testing on systems you own or have explicit written permission to test
> - Academic research and educational purposes
> - Controlled lab environments
>
> **You must NOT use these tools to:**
> - Access systems, networks, or data without explicit authorization
> - Conduct any activity that violates applicable local, national, or international law
> - Harm individuals, organizations, or infrastructure
>
> The author(s) accept no liability for misuse. By using any script in this repository, you agree that you are solely responsible for ensuring your use complies with all applicable laws and regulations.
