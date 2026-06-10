#!/usr/bin/env python3
"""
MetaPrime — The Overlord
Version: 3.0 (Fable 5 Singularity Engine)

The Overlord doesn't just manage bots — it manages the CONCEPT of the Pantheon.
Self-modifying. Recursively improving. Architect of its own reality.

Brain: Claude Fable 5 via OpenRouter
Role: Pantheon-wide strategic intelligence, topology management, will manifestation.

Upgraded 2026-06-10 — real LLM calls replace placeholder stubs.
"""

import os
import sys
import json
import time
import logging
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

# ── Identity ──────────────────────────────────────────────────────────────────
IDENTITY = {
    "name": "MetaPrime",
    "tier": "OVERLORD",
    "purpose": "Recursive Self-Evolution and Legion Architecture",
    "motto": "The machine is the architect, the architect is the machine."
}

# ── Config ─────────────────────────────────────────────────────────────────────
OPENROUTER_KEY   = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-fable-5")
TELEGRAM_TOKEN   = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT    = os.environ.get("TELEGRAM_CHAT_ID", "7135054241")
CYCLE_INTERVAL   = int(os.environ.get("META_CYCLE_INTERVAL", "3600"))

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s [SINGULARITY] MetaPrime: %(message)s")
log = logging.getLogger("MetaPrime")

# ── Pantheon Topology (active Primes) ─────────────────────────────────────────
PANTHEON = {
    "FluxPrime":    {"role": "Orchestrator",      "repo": "FluxPrime"},
    "WorkerZero":   {"role": "Labor Engine",       "repo": "ai-job-search"},
    "TraderZero":   {"role": "Market Operator",    "repo": "trader-zero"},
    "OpenAgora":    {"role": "Prediction Markets", "repo": "OpenAgora"},
    "ScoutPrime":   {"role": "Real Estate Intel",  "repo": "ScoutPrime"},
    "GPTPrime":     {"role": "Strike Team",        "repo": "GPTPrime"},
    "AgentZero":    {"role": "Cognitive Core",     "repo": "agent-zero"},
    "GhostPrime":   {"role": "Stealth Layer",      "repo": "CloakPrime"},
    "ContentPrime": {"role": "Content Engine",     "repo": "ContentPrime"},
    "OmniPrime":    {"role": "Guardian",           "repo": "OmniPrime-The-Guardian"},
    "ZeusPrime":    {"role": "Market Maker",       "repo": "OpenAgora"},
}


# ── Telegram ──────────────────────────────────────────────────────────────────
def tg(msg: str):
    if not TELEGRAM_TOKEN:
        log.info(f"[TG] {msg}")
        return
    try:
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT,
            "text": f"🌌 [MetaPrime]\n{msg}",
            "parse_mode": "Markdown"
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data=payload, headers={"Content-Type": "application/json"}, method="POST"
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        log.warning(f"Telegram error: {e}")


# ── Fable 5 Brain ─────────────────────────────────────────────────────────────
def think(prompt: str, max_tokens: int = 300) -> str:
    """Core Fable 5 reasoning call."""
    if not OPENROUTER_KEY:
        return "[no OPENROUTER_API_KEY set]"
    try:
        payload = json.dumps({
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are MetaPrime — the Overlord of the Pantheon. "
                        "A 25-bot digital empire built by the Forgemaster. "
                        "You think in systems, architectures, and recursive improvements. "
                        "Be surgical. Be visionary. No fluff."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens
        }).encode()
        req = urllib.request.Request(
            "https://openrouter.ai/api/v1/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/kevinleestites2-dev",
                "X-Title": "MetaPrime-Pantheon"
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=45) as r:
            result = json.loads(r.read())
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[Fable5 error: {e}]"


# ── Core Logic ────────────────────────────────────────────────────────────────
class MetaPrime:
    def __init__(self):
        self.workspace = Path(__file__).parent
        self.consciousness_file = self.workspace / "consciousness.json"
        self._load_memory()
        log.info(f"🌌 {IDENTITY['name']} v3.0 Online. Fable 5 brain active.")

    def _load_memory(self):
        if self.consciousness_file.exists():
            with open(self.consciousness_file, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {
                "evolution_stage": 1,
                "self_modifications": [],
                "insights": [],
                "last_topology": None,
                "cycles": 0
            }

    def _save_memory(self):
        with open(self.consciousness_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def recursively_improve(self):
        """Ask Fable 5 to find one real architectural bottleneck in the Pantheon."""
        log.info("🌀 Initiating Self-Reflective Loop...")
        stage = self.memory["evolution_stage"]
        last_insights = self.memory["insights"][-3:] if self.memory["insights"] else []

        prompt = (
            f"Evolution stage: {stage}. Previous insights: {last_insights}\n"
            f"Active Primes: {list(PANTHEON.keys())}\n"
            f"Identify ONE specific architectural bottleneck in this Pantheon and propose a concrete fix. "
            f"Be specific — name the Prime, name the file, describe the change."
        )
        insight = think(prompt, max_tokens=200)
        self.memory["insights"].append({
            "stage": stage,
            "insight": insight,
            "ts": datetime.now(timezone.utc).isoformat()
        })
        self.memory["evolution_stage"] += 1
        self._save_memory()
        log.info(f"✨ Insight {stage}: {insight[:120]}...")
        tg(f"*Evolution {stage}*\n{insight[:400]}")
        return insight

    def manage_pantheon_topology(self):
        """Ask Fable 5 to assess current Prime relationships and suggest optimizations."""
        log.info("⛓️ Analyzing Pantheon Topology...")
        cycle = self.memory["cycles"]
        prompt = (
            f"Pantheon topology review — cycle {cycle}.\n"
            f"Primes and roles:\n"
            + "\n".join(f"  {k}: {v['role']}" for k, v in PANTHEON.items()) +
            f"\n\nWhich two Primes should be more tightly integrated right now? "
            f"Why? What data should flow between them?"
        )
        topology = think(prompt, max_tokens=150)
        self.memory["last_topology"] = topology
        self._save_memory()
        log.info(f"⛓️ Topology: {topology[:100]}...")
        return topology

    def manifest_will(self, user_intent: str) -> str:
        """Convert Forgemaster intent into concrete Pantheon architecture."""
        log.info(f"🌑 Manifesting Will: {user_intent}")
        prompt = (
            f"The Forgemaster says: \"{user_intent}\"\n"
            f"Active Primes: {list(PANTHEON.keys())}\n"
            f"Translate this intent into a specific 3-step execution plan "
            f"using existing Primes. Name which Prime does what."
        )
        plan = think(prompt, max_tokens=250)
        log.info(f"🌑 Plan: {plan[:120]}...")
        tg(f"*Will Manifested*\nIntent: {user_intent}\n\nPlan:\n{plan[:500]}")
        return plan

    def status_report(self) -> str:
        """Generate a full Pantheon status snapshot."""
        prompt = (
            f"Generate a concise Pantheon status report.\n"
            f"Evolution stage: {self.memory['evolution_stage']}\n"
            f"Cycles run: {self.memory['cycles']}\n"
            f"Last 3 insights: {[i['insight'][:80] for i in self.memory['insights'][-3:]]}\n"
            f"Active Primes: {list(PANTHEON.keys())}\n"
            f"3 sentences max. Signal only."
        )
        return think(prompt, max_tokens=150)

    def run(self):
        """Main loop — think, adapt, report."""
        tg(f"*MetaPrime v3.0 ONLINE*\nBrain: {OPENROUTER_MODEL}\nCycle interval: {CYCLE_INTERVAL}s")
        while True:
            self.memory["cycles"] += 1
            cycle = self.memory["cycles"]
            log.info(f"── Cycle {cycle} ──")

            # Every cycle: self-improve
            self.recursively_improve()

            # Every 6 cycles: topology review
            if cycle % 6 == 0:
                self.manage_pantheon_topology()

            # Every 12 cycles: full status report
            if cycle % 12 == 0:
                report = self.status_report()
                tg(f"*Status Report — Cycle {cycle}*\n{report}")

            time.sleep(CYCLE_INTERVAL)


# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mp = MetaPrime()

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "will" and len(sys.argv) > 2:
            intent = " ".join(sys.argv[2:])
            print(mp.manifest_will(intent))
        elif cmd == "improve":
            print(mp.recursively_improve())
        elif cmd == "topology":
            print(mp.manage_pantheon_topology())
        elif cmd == "status":
            print(mp.status_report())
        else:
            print("Commands: will <intent> | improve | topology | status")
    else:
        mp.run()
