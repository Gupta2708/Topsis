# Topsis

A Python package for calculating TOPSIS score and ranking alternatives using the Technique for Order Preference by Similarity to Ideal Solution.

## What is TOPSIS?

TOPSIS is a multi-criteria decision-making method used to rank alternatives based on their closeness to the ideal best solution and distance from the ideal worst solution.

The alternative with the highest TOPSIS score gets Rank 1.

## Installation

```bash
pip install Topsis-Vaibhav-102316130
```

## Usage

Run the package from the command line using:

```bash
python -m topsis_vaibhav_102316130.topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

## Example

```bash
python -m topsis_vaibhav_102316130.topsis data.csv "1,1,1,1" "-,+,+,+" output-result.csv
```

## Input CSV Format

The input file must be a CSV file.

The input CSV must contain three or more columns.

The first column should contain the name or identifier of the alternative.

From the second column to the last column, all values must be numeric.

Example input file:

```csv
Model,Price,Storage,Camera,Looks
M1,250,16,12,5
M2,200,16,8,3
M3,300,32,16,4
M4,275,32,8,4
M5,225,16,16,2
```

## Weights

Weights must be numeric and comma-separated.

Example:

```text
1,1,1,1
```

The number of weights must be equal to the number of criteria columns.

Criteria columns are all columns from the second column to the last column.

## Impacts

Impacts must be comma-separated.

Each impact must be either `+` or `-`.

Use `+` when a higher value is better.

Use `-` when a lower value is better.

Example:

```text
-,+,+,+
```

The number of impacts must be equal to the number of criteria columns.

## Output

The output file will be generated as a CSV file.

The output CSV contains all original columns plus two extra columns:

- Topsis Score
- Rank

Example output:

```csv
Model,Price,Storage,Camera,Looks,Topsis Score,Rank
M1,250,16,12,5,0.5342768571821003,3
M2,200,16,8,3,0.3083677687324685,5
M3,300,32,16,4,0.6916322312675315,1
M4,275,32,8,4,0.534736584486838,2
M5,225,16,16,2,0.40104612151678615,4
```

## Error Handling

This package checks for:

- Correct number of command-line arguments
- File not found error
- Input file must contain three or more columns
- Values from the second column onward must be numeric
- Number of weights must match the number of criteria columns
- Number of impacts must match the number of criteria columns
- Impacts must be either `+` or `-`
- Weights and impacts must be separated by commas

## PyPI Package

You can view and install the package from PyPI here:

[https://pypi.org/project/Topsis-Vaibhav-102316130/](https://pypi.org/project/Topsis-Vaibhav-102316130/)

## Author

Vaibhav Gupta  
Roll Number: 102316130