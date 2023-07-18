# Planet NG

Uses [reader](https://reader.readthedocs.io/en/latest/) and jinja2 to replace
the original planet-planet software that seems unmaintained. Reads the same
`config.ini` file as planet-planet, but ignores parts of it.

## Quick start

```
export PYTHONUSERBASE=$PWD/py-env
pip install -r requirements.txt
python -m planet_reader
```

## Options

```
Usage: python -m planet_reader [OPTIONS]

Options:
  --config PATH           Configuration file.  [default: config.ini]
  --db PATH               Sqlite database file.  [default: db.sqlite]
  --template-path PATH    Path to custom templates.
  --update / --no-update  Update feeds in database  [default: update]
  --sync / --no-sync      Sync database feed list to config file  [default:
                          sync]
  --no-out                [default: False]
  --help                  Show this message and exit.  [default: False]
```
