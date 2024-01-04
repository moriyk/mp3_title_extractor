# mp3_title_extractor

This is a simple tool to extract the title attribute from a specified MP3 file.

## Installation

You can install the package directly from GitHub using the following command:

```bash
pip install git+https://github.com/moriyku/mp3_title_extractor.git
```

## Usage

You can use the command line as follows:

```bash
mp3_title_extractor path/to/your/file.mp3
```

The title attribute of the specified MP3 file will be displayed on the standard output.

For example:

```bash
Title: My Example Song
```

## Note

The target MP3 file must contain the title attribute.
If the title does not exist, "N/A" will be displayed.
