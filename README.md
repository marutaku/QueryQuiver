# QueryQuiver

QueryQuiver estimates your interests based on your past Google Chrome search history and suggests technical article ideas that you might be comfortable writing about.

## Install

```shell
pip install queryquiver
```

or If you want to install from source code, you can install it as follows.

```shell
pip install git+https://github.com/marutaku/QueryQuiver
```

## Usage

Please close Google Chrome before using this tool.

The tool references the SQLite database used internally by Google Chrome.

While using GoogleChrome, this SQLite database will be locked and an error will occur.

```shell
queryquiver generate
```

### Options

```shell
queryquiver generate --help

NAME
    queryquiver generate - Generate idea of tech articles from Google Chrome history

SYNOPSIS
    queryquiver generate <flags>

DESCRIPTION
    Generate idea of tech articles from Google Chrome history

FLAGS
    -q, --query_history_limit=QUERY_HISTORY_LIMIT
        Type: int
        Default: 20
    -n, --number_of_ideas=NUMBER_OF_IDEAS
        Type: int
        Default: 5
    -c, --chrome_history_path=CHROME_HISTORY_PATH
        Type: Optional[str | None]
        Default: None
    -o, --openai_api_key=OPENAI_API_KEY
        Type: Optional[str | None]
```

## Developer information

### setup

```shell
make setup
```

### test

```shell
make test
```

### lint

```shell
make lint
```

### format

```shell
make format
```
