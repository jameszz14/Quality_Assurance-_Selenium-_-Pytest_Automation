# Automated Testing Project

**Course**: Software Quality  
**Student**: Débora Sieburger Carvalho  
**Submission Date**: 06/03/2025  
**Institution**: Centro Universitário Senac-RS - Pelotas

## Project Structure

- `funcional/test_login_saucedemo.py`: functional test using Selenium (login on https://www.saucedemo.com/)  
- `unitario/`: Python functions with unit tests using Pytest

## How to run

1. Install the dependencies and run the tests:

```bash
pip install -r requirements.txt

# Run functional tests (Selenium)
cd funcional
py test_adicionar_produto.py

# Run unit tests (Pytest)
cd ../unitario
python -m pytest nome_do_arquivo.py -s
