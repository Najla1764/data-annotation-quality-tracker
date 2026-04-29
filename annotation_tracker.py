import pandas as pd
from datetime import date

# ── STEP 1: Load your data ──────────────────────────
df = pd.read_excel("customer_messages.xlsx")
print("=" * 45)
print("     ANNOTATION QUALITY TRACKER")
print("=" * 45)

# ── STEP 2: Count total messages ────────────────────
total = len(df)
print(f"\n Total messages    : {total}")

# ── STEP 3: Count labels ─────────────────────────────
complaint = df["your_label"].value_counts().get("COMPLAINT", 0)
inquiry   = df["your_label"].value_counts().get("INQUIRY", 0)
urgent    = df["your_label"].value_counts().get("URGENT", 0)
feedback  = df["your_label"].value_counts().get("FEEDBACK", 0)

print(f"\n Label Breakdown:")
print(f"   COMPLAINT  : {complaint}")
print(f"   INQUIRY    : {inquiry}")
print(f"   URGENT     : {urgent}")
print(f"   FEEDBACK   : {feedback}")

# ── STEP 4: Count confidence levels ─────────────────
high   = df["confidence"].value_counts().get("HIGH", 0)
medium = df["confidence"].value_counts().get("MEDIUM", 0)
low    = df["confidence"].value_counts().get("LOW", 0)

print(f"\n Confidence Levels:")
print(f"   HIGH       : {high}")
print(f"   MEDIUM     : {medium}")
print(f"   LOW        : {low}")

# ── STEP 5: Calculate accuracy ───────────────────────
accuracy = round((high / total) * 100, 2)
print(f"\n Accuracy Rate     : {accuracy}%")

# ── STEP 6: Count issues ─────────────────────────────
issues = df[df["issue_flag"] == "YES"]
print(f" Issues Flagged    : {len(issues)}")

# ── STEP 7: Check SLA ────────────────────────────────
daily_target = 50
print(f"\n SLA Target        : {daily_target} messages/day")

if total >= daily_target:
    print(f" SLA Status        : MET ✅")
else:
    print(f" SLA Status        : NOT MET ❌")
    print(f" Shortfall         : {daily_target - total} messages")

# ── STEP 8: Save daily report ────────────────────────
report = pd.DataFrame({
    "Metric": [
        "Date",
        "Total Messages",
        "COMPLAINT",
        "INQUIRY",
        "URGENT",
        "FEEDBACK",
        "HIGH Confidence",
        "MEDIUM Confidence",
        "LOW Confidence",
        "Accuracy Rate",
        "Issues Flagged",
        "SLA Target",
        "SLA Status"
    ],
    "Value": [
        str(date.today()),
        total,
        complaint,
        inquiry,
        urgent,
        feedback,
        high,
        medium,
        low,
        f"{accuracy}%",
        len(issues),
        daily_target,
        "MET" if total >= daily_target else "NOT MET"
    ]
})

report.to_excel("quality_report.xlsx", index=False)
print(f"\n📊 Quality report saved to quality_report.xlsx ✅")
print("=" * 45)