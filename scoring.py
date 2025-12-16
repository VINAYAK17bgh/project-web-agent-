def calculate_score(row):
    score = 0

    if any(x in row["Title"] for x in ["Director", "Head", "VP"]):
        score += 30

    if row["Funding_Stage"] in ["Series A", "Series B", "Series C"]:
        score += 20

    if row["Uses_3D_Models"] == "Yes":
        score += 15

    if row["Recent_Publication"] == "Yes":
        score += 40

    hubs = ["Cambridge", "Boston", "Basel", "Bay Area"]
    if any(hub in row["Person_Location"] for hub in hubs):
        score += 10

    return min(score, 100)
