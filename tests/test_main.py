import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import load_and_process_data

def test_no_duplicates():
    df = load_and_process_data(
        "data/dataset.csv",
        "data/test_processed_dataset.csv"
    )

    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
