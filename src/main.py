import pandas as pd
from pathlib import Path

def load_and_process_data(
    filepath="data/dataset.csv",
    output_path="data/processed_dataset.csv"
):
    """
    Loads dataset, removes duplicate rows, and saves the processed dataset.
    """

    input_path = Path(filepath)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")

    df = pd.read_csv(input_path)

    print("Original dataset shape:", df.shape)

    df = df.drop_duplicates()

    print("Dataset shape after removing duplicates:", df.shape)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Processed dataset saved to: {output_path}")

    return df

if __name__ == "__main__":
    load_and_process_data()
