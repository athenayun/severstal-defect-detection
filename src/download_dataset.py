"""Download the Severstal Steel Defect Detection dataset from Kaggle.

Prerequisites:
    - Install kagglehub.
    - Configure Kaggle API credentials.
    - Accept the Severstal competition rules.

Usage:
    python src/download_dataset.py --output-dir "/path/to/dataset"

Example:
    python src/download_dataset.py \
        --output-dir "/Volumes/ExternalSSD/datasets/severstal"
"""

import argparse
from pathlib import Path

import kagglehub


COMPETITION = "severstal-steel-defect-detection"


def download_dataset(output_dir: Path) -> Path:
    """Download the competition dataset to the specified directory."""

    output_dir.mkdir(parents=True, exist_ok=True)

    dataset_path = kagglehub.competition_download(
        COMPETITION,
        output_dir=str(output_dir),
    )

    return Path(dataset_path)


def main() -> None:
    """Parse command-line arguments and download the dataset."""

    parser = argparse.ArgumentParser(
        description="Download the Severstal dataset."
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory where the dataset will be stored.",
    )

    args = parser.parse_args()

    dataset_path = download_dataset(args.output_dir)

    print(f"Dataset downloaded to: {dataset_path}")


if __name__ == "__main__":
    main()