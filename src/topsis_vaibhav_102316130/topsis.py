import sys
import os
import pandas as pd
import numpy as np


USAGE = (
    'Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>\n'
    'Example: python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv'
)


def parse_weights(weights_string):
    if "," not in weights_string:
        raise ValueError("Weights must be separated by commas.")

    try:
        weights = [float(w.strip()) for w in weights_string.split(",")]
    except ValueError:
        raise ValueError("Weights must contain numeric values only.")

    if len(weights) == 0:
        raise ValueError("Weights cannot be empty.")

    if any(w <= 0 for w in weights):
        raise ValueError("Weights must be positive numbers.")

    return np.array(weights, dtype=float)


def parse_impacts(impacts_string):
    if "," not in impacts_string:
        raise ValueError("Impacts must be separated by commas.")

    impacts = [i.strip() for i in impacts_string.split(",")]

    if len(impacts) == 0:
        raise ValueError("Impacts cannot be empty.")

    for impact in impacts:
        if impact not in ["+", "-"]:
            raise ValueError("Impacts must be either + or - only.")

    return impacts


def calculate_topsis(input_file, weights_string, impacts_string, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        raise ValueError(f"Unable to read input CSV file: {e}")

    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns.")

    weights = parse_weights(weights_string)
    impacts = parse_impacts(impacts_string)

    criteria_columns = df.columns[1:]

    if len(weights) != len(criteria_columns):
        raise ValueError("Number of weights must be equal to number of criteria columns.")

    if len(impacts) != len(criteria_columns):
        raise ValueError("Number of impacts must be equal to number of criteria columns.")

    data = df.iloc[:, 1:].copy()

    for col in data.columns:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    if data.isnull().values.any():
        raise ValueError("From 2nd to last columns, all values must be numeric.")

    data = data.astype(float)

    denominator = np.sqrt((data ** 2).sum(axis=0))

    if (denominator == 0).any():
        raise ValueError("Criteria columns cannot contain all zero values.")

    normalized_data = data / denominator
    weighted_data = normalized_data * weights

    ideal_best = []
    ideal_worst = []

    for i, impact in enumerate(impacts):
        column_values = weighted_data.iloc[:, i]

        if impact == "+":
            ideal_best.append(column_values.max())
            ideal_worst.append(column_values.min())
        else:
            ideal_best.append(column_values.min())
            ideal_worst.append(column_values.max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    scores = distance_worst / (distance_best + distance_worst)

    result_df = df.copy()
    result_df["Topsis Score"] = scores
    result_df["Rank"] = result_df["Topsis Score"].rank(
        ascending=False,
        method="min"
    ).astype(int)

    result_df.to_csv(output_file, index=False)

    return result_df


def main():
    if len(sys.argv) != 5:
        print(USAGE)
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        calculate_topsis(input_file, weights, impacts, output_file)
        print(f"TOPSIS result saved successfully to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()