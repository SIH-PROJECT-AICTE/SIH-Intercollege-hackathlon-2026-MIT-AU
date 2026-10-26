
# CampusOS

Secure hackathon MVP for a live campus operations digital twin. It uses a built-in simulator for a dependable demo and provides an Oracle-ready schema for production storage.

## Start CampusOS (easiest way)

Double-click `start_campusos.bat`, or open PowerShell in this folder and run:

```powershell
python run_campusos.py
```

The launcher creates `.env` securely when needed, installs packages on the first run, starts both frontend and backend, and opens the dashboard. The simulator is built into the API/dashboard: use the **Judge demo** buttons after login, so no third terminal is needed.

## Manual run

1. Copy `.env.example` to `.env` and replace `JWT_SECRET` with a long random value.
2. Run `npm install`.
3. Run `npm run dev`, then open `http://localhost:5173`.

The interactive dashboard works in simulated mode immediately. The API starts at `http://localhost:4000/api/v1/health`.

## Security notes

The API uses strict request schemas, a small JSON payload limit, Helmet headers, CORS allowlisting, HTTP-only JWT cookies, server-side role checks, generic authentication errors, and rate limiting. Connect Oracle with the least-privilege application account and use parameterized binds in every query; never interpolate user input into SQL. `database/schema.sql` creates the core normalized tables and telemetry index.

## Demo flow

Open the dashboard, use the Digital Twin, inspect the Library leak in Anomaly Center, test an HVAC scenario in What-if Simulator, then approve the water-line recommendation in Action Center. No physical device is ever controlled in this MVP.

# SIH-Intercollege-hackathlon-2026
Smart campus os
