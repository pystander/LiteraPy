# LiteraPy

``LiteraPy`` is a pure-Python program dedicated for autofilling Chinese vocabularies and phrases. It is particularly designed to assist students and writers in their writings with matched, suitable word choice.

Please note that this is only my own practice on Python as a CS student. The program is still under development and should never be taken as a high-end solution.
For further enquiries, please feel free to contact me on GitHub via [Issues](https://github.com/pystander/LiteraPy/issues).

<br/>

## Features

- Built on external libraries (Currently based on [開放詞典](https://kaifangcidian.com/xiazai/))

- Text segmentation with [jieba](https://github.com/fxsjy/jieba) and [paddlepaddle-tiny](https://pypi.org/project/paddlepaddle-tiny/)

- Vocabulary and Pinyin search

- Optimization for clarity and efficiency

- Bad words list ([LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words)) and customized filtering

<br/>

## Installation

``LiteraPy`` is developed and works under [Python](https://www.python.org/) 3.7

<br/>

## To-do List

- [x] Multi-character Pinyin search -> See [v1.0.3](https://github.com/pystander/LiteraPy/releases/tag/v1.0.3)

- [x] Identifier for Chinese part of speech (主謂賓 定狀補) -> [jieba](https://github.com/fxsjy/jieba)

- [ ] AI / algorithms with word suggestions (e.g. HMM & Viterbi)

- [x] Temp for less time in re-search 

- [ ] CPython implementation to improve efficiency

<br/>

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<br/>

## References

[1] [開放詞典](https://kaifangcidian.com/xiazai/)

[2] [LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words: List of Dirty, Naughty, Obscene, and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words)

[3] [fxsjy/jieba: 结巴中文分词](https://github.com/fxsjy/jieba)
