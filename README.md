# csv-delim-converter
Convert CSV delimiters, eg. `;` -> `,`

Example:
```bash
python -m src.convert input.csv -d1 "," -d2 "\t"
```

It takes `input.csv`, converts it from `,` (csv) to `\t` (tsv) and stores into `input_output.csv`

Custom output file can be set: `--output output.csv`


