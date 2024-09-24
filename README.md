# CRANBERRY-GPT

![PyPI - Downloads](https://img.shields.io/pypi/dm/cranberry-gpt)
[![PyPI - Version](https://img.shields.io/pypi/v/cranberry-gpt)](https://pypi.org/project/cranberry-gpt/)
[![codecov](https://codecov.io/gh/AdityaNG/cranberry-gpt/branch/main/graph/badge.svg?token=kan-gpt_token_here)](https://codecov.io/gh/AdityaNG/cranberry-gpt)
[![CI](https://github.com/AdityaNG/cranberry/actions/workflows/main.yml/badge.svg)](https://github.com/AdityaNG/cranberry/actions/workflows/main.yml)
[![GitHub License](https://img.shields.io/github/license/AdityaNG/cranberry-gpt)](https://github.com/AdityaNG/cranberry/blob/main/LICENSE)


Teaching LMMs to interact with computers

## Install it from PyPI

```bash
pip install cranberry_gpt
```

## Citation

If you find our work useful cite us!

```
@misc{NG2024CRANBERRYGPT,
  author       = {Aditya Nalgunda Ganesh},
  title        = {CRANBERRY-GPT: Teaching LMMs to interact with computers},
  year         = {2024},
  month        = {September},
  note         = {Release 1.0.0, 24th September 2024},
  url          = {https://github.com/AdityaNG/cranberry/}
}
```

## Usage

TODO

```py
# TODO
```

## Setup for Development

```bash
# Download Repo
git clone https://github.com/AdityaNG/cranberry
cd cranberry
git pull

make virtualenv

```

## TODO Points

- [ ] Draw Architecture diagram
- [ ] Build the Dockercontainer w/ OpenInterpreter
- [ ] Implement [LLM Proxy](https://github.com/BerriAI/litellm) to intercept all the chat data
- [ ] Implement [MCTS](https://github.com/AdityaNG/MyuGPT/blob/main/myugpt/mcts.py)
- [ ] Logging for all the agent's data
- [ ] Setup RL experiments (need to list out more experiments)
    - [ ] Create a file on the desktop, open it in the GUI and save the screenshot
    - [ ] Open the Gmail and Summarise the top 5 unread emails
- [ ] Generate dataset of runs with the RL experiments
- [ ] Fine-tune LMMs on the newly created
- [x] Documentation: `mkdocs gh-deploy`
- [x] Test Cases

## Development

Read the [CONTRIBUTING.md](https://github.com/AdityaNG/cranberry/blob/main/CONTRIBUTING.md) file.

## References

- TODO
