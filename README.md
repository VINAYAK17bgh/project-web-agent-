# AI Web Agent for High-Probability Lead Identification

## Overview
This project demonstrates a working demo of an AI-powered web agent designed to
identify, enrich, and rank high-intent leads for **3D in-vitro models in drug discovery
and toxicology**.

The system simulates how a business development professional prioritizes outreach
using scientific, funding, and role-based signals.

---

## Problem Statement
Business development teams struggle to identify which researchers or companies are
most likely to adopt advanced 3D in-vitro models. This tool solves that by ranking leads
based on **Propensity to Buy**.

---

## Data Sources (Simulated)
- Professional profiles (LinkedIn-style data)
- Scientific intent (recent publications)
- Company funding stage
- Technographic adoption (3D models)
- Location intelligence (biotech hubs)

---

## Propensity Scoring Logic (0–100)
| Signal | Weight |
|------|-------|
| Role Fit (Director/VP/Head) | +30 |
| Funding Stage (Series A/B/C) | +20 |
| Uses 3D In-Vitro Models | +15 |
| Recent Scientific Publication | +40 |
| Biotech Hub Location | +10 |

---

## Features
- Dynamic lead ranking
- Search & filtering
- Location split (Person vs HQ)
- CSV export for BD teams
- Clean, explainable scoring logic

---

## Tech Stack
- Python
- Streamlit
- Pandas

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
