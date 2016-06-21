# Python examples for the NBG Open Bank API

This repository contains examples for accessing the API of the National Bank of Greece, through Python.

More information on the NBG Open Bank API can be found at https://nbgdemo.portal.azure-api.net/docs/services/570d09697a995a13c499072f/

## Installation

To use the `nbg` package you must install its requirements using the following command

```
pip install -r requirements.txt
```

## Configuration

To configure the NBG Open Bank API Python client create a file with `.env` as its name in the root directory of your project. Add your subscription primary and secondary keys in the following format in this file:

```
NBG_PRIMARY_KEY=your_primary_key_here
NBG_SECONDARY_KEY=your_secondary_key_here
```

Your subscription keys can be located at https://nbgdemo.portal.azure-api.net/developer.

## Usage

In order to use `nbg` open a Python terminal and import it like this:

```python
import nbg
```

Below you can find several examples on how to use the NBG API with the `nbg` library.

### List available ATMs

```python
import nbg

response = nbg.get('/api/banks')

print response.json()
```
