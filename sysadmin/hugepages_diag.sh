#!/usr/bin/env bash
set -euo pipefail

echo "=== HugePages Diagnostic ==="
echo

echo "[1] /proc/meminfo"
grep -i huge /proc/meminfo || echo "No hugepage-related fields found"
echo

echo "[2] Static hugepage reservation"
if [[ -r /proc/sys/vm/nr_hugepages ]]; then
    echo -n "nr_hugepages: "
    cat /proc/sys/vm/nr_hugepages
else
    echo "Cannot read /proc/sys/vm/nr_hugepages"
fi
echo

echo "[3] Transparent Huge Pages (THP)"
THP_BASE="/sys/kernel/mm/transparent_hugepage"
if [[ -r "$THP_BASE/enabled" ]]; then
    echo -n "enabled: "
    cat "$THP_BASE/enabled"
else
    echo "THP status file not found"
fi

if [[ -r "$THP_BASE/defrag" ]]; then
    echo -n "defrag:  "
    cat "$THP_BASE/defrag"
fi
echo

echo "[4] CPU support flags"
CPU_FLAGS=$(grep -m1 '^flags' /proc/cpuinfo || true)

if echo "$CPU_FLAGS" | grep -qw pse; then
    echo "2 MB hugepages supported (pse)"
else
    echo "2 MB hugepages flag NOT found"
fi

if echo "$CPU_FLAGS" | grep -qw pdpe1gb; then
    echo "1 GB hugepages supported (pdpe1gb)"
else
    echo "1 GB hugepages flag NOT found"
fi
echo

echo "[5] Per-size hugepage pools"
HP_DIR="/sys/kernel/mm/hugepages"
if [[ -d "$HP_DIR" ]]; then
    for d in "$HP_DIR"/hugepages-*; do
        [[ -d "$d" ]] || continue
        size=$(basename "$d")
        free=$(cat "$d/free_hugepages" 2>/dev/null || echo "?")
        total=$(cat "$d/nr_hugepages" 2>/dev/null || echo "?")
        reserved=$(cat "$d/resv_hugepages" 2>/dev/null || echo "?")
        echo "$size -> total=$total free=$free reserved=$reserved"
    done
else
    echo "Hugepage sysfs directory not found"
fi
echo

echo "[6] Quick verdict"
TOTAL=$(grep '^HugePages_Total:' /proc/meminfo 2>/dev/null | awk '{print $2}')
THP=$(cat /sys/kernel/mm/transparent_hugepage/enabled 2>/dev/null || true)

if [[ "${TOTAL:-0}" -gt 0 ]]; then
    echo "Explicit hugepages AVAILABLE"
else
    echo "Explicit hugepages NOT reserved"
fi

if echo "$THP" | grep -q '\['; then
    ACTIVE=$(echo "$THP" | grep -o '\[[^]]*\]' | tr -d '[]')
    echo "THP active mode: $ACTIVE"
else
    echo "THP status unknown"
fi
