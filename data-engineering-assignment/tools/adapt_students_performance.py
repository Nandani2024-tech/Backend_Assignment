import csv
from pathlib import Path

# -------- CONFIG --------
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "StudentsPerformance.csv"
OUTPUT_FILE = BASE_DIR / "students_kaggle_adapted.csv"

# -------- HELPERS --------
def score_to_year(score: int) -> int:
    if score < 40:
        return 1
    elif score < 55:
        return 2
    elif score < 70:
        return 3
    elif score < 85:
        return 4
    else:
        return 5


def score_to_dept(score: int) -> str:
    if score < 50:
        return "ME"
    elif score < 65:
        return "EE"
    elif score < 80:
        return "CS"
    else:
        return "CE"


# -------- MAIN --------
def adapt_dataset():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    total_rows = 0
    written_rows = 0
    skipped_rows = 0

    with open(INPUT_FILE, newline="", encoding="utf-8") as inp, \
         open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as out:

        reader = csv.DictReader(inp)
        writer = csv.writer(out)

        # Target ETL schema
        writer.writerow(["Name", "Email", "Phone", "Year", "Dept"])

        for i, row in enumerate(reader):
            total_rows += 1

            try:
                math_score = row.get("math score")
                reading_score = row.get("reading score")

                # Skip rows with missing scores
                if not math_score or not reading_score:
                    skipped_rows += 1
                    continue

                math = int(math_score)
                reading = int(reading_score)

                writer.writerow([
                    f"Student {i}",
                    f"student{i}@example.com",
                    "",
                    score_to_year(math),
                    score_to_dept(reading)
                ])

                written_rows += 1

            except ValueError:
                # Handles non-numeric scores
                skipped_rows += 1
                continue

    print("✅ Kaggle dataset adapted successfully")
    print(f"📥 Total rows read     : {total_rows}")
    print(f"✅ Rows written        : {written_rows}")
    print(f"⚠️ Rows skipped (bad) : {skipped_rows}")
    print(f"📄 Output file         : {OUTPUT_FILE}")


if __name__ == "__main__":
    adapt_dataset()