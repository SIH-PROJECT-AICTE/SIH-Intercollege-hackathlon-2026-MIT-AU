"""One-command launcher for the CampusOS hackathon demo (Windows/macOS/Linux)."""

from __future__ import annotations

import os
import secrets
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENV_FILE = ROOT / ".env"
ENV_EXAMPLE = ROOT / ".env.example"
NPM = "npm.cmd" if os.name == "nt" else "npm"


def fail(message: str) -> None:
    print(f"\n[CampusOS] {message}\n")
    input("Press Enter to close...")
    raise SystemExit(1)


def create_env_if_missing() -> None:
    if ENV_FILE.exists():
        return
    if not ENV_EXAMPLE.exists():
        fail(".env.example is missing. Restore it, then run this launcher again.")
    secret = secrets.token_urlsafe(40)
    content = ENV_EXAMPLE.read_text(encoding="utf-8").replace(
        "replace-with-a-long-random-secret", secret
    )
    ENV_FILE.write_text(content, encoding="utf-8")
    print("[CampusOS] Created .env with a secure local JWT secret.")


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def install_dependencies() -> None:
    vite_binary = ROOT / "node_modules" / ".bin" / ("vite.cmd" if os.name == "nt" else "vite")
    if vite_binary.exists():
        return
    print("[CampusOS] Installing required packages. This only happens on first run.")
    local_cache = ROOT / ".npm-cache"
    result = subprocess.run(
        [NPM, "install", "--cache", str(local_cache), "--no-audit", "--no-fund"],
        cwd=ROOT,
    )
    if result.returncode != 0:
        fail(
            "Package installation failed. Check your internet connection, then run this script again. "
            "If it still fails, delete node_modules and package-lock.json from this project folder, then retry."
        )


def open_dashboard() -> None:
    time.sleep(4)
    webbrowser.open("http://localhost:5173")


def main() -> None:
    print("=" * 58)
    print(" CampusOS — Smart Campus Operations Demo")
    print("=" * 58)
    if not command_exists("node") or not command_exists(NPM):
        fail("Node.js is not installed. Install the current LTS version from https://nodejs.org, then run this file again.")
    create_env_if_missing()
    install_dependencies()
    print("[CampusOS] Starting frontend and backend...")
    print("[CampusOS] Dashboard: http://localhost:5173")
    print("[CampusOS] Demo login: manager@campusos.demo / DemoPass!2026")
    print("[CampusOS] Press Ctrl+C in this terminal to stop CampusOS.\n")
    threading.Thread(target=open_dashboard, daemon=True).start()
    try:
        subprocess.run([NPM, "run", "dev"], cwd=ROOT, check=False)
    except KeyboardInterrupt:
        print("\n[CampusOS] Stopped.")


if __name__ == "__main__":
    main()
