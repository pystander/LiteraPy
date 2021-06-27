# LiteraPy

``LiteraPy`` is a pure-Python program dedicated for autofilling Chinese vocabularies and phrases. It is particularly designed to assist students and writers in their writings with matched, suitable word choice.

Please note that this is only my own practice on Python as an IT student, and this should never be taken as a high-end solution.
For further enquiries, please feel free to contact me on GitHub via [Issues](https://github.com/pystander/LiteraPy/issues).

<br/>

## Features

- Built on [MDBG CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict)

- Vocabulary and Pinyin search

- Easy-to-read

<br/>

## Installation

``LiteraPy`` is developed and works under [Python](https://www.python.org/) 3.7

No external package or library is required to run the program.

<br/>

## Changelog

**1.0.3**

- Added ``nodup(dup_list)`` for removing duplicates from list

- Fixed errors on matching ``search()`` zh-CHT results

- Supported multi-character search for ``pinyin()``

**1.0.2**

- Optimized ``search()`` and ``pinyin()``

- Supported both Traditional and Simplified Chinese for ``search()`` and ``pinyin()``

- Removed class ``Language`` for optimization

**1.0.1**

- Added ``Language.lang()`` for language settings

- Added ``fun()`` for functions

**1.0.0**

- Built on [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict) Utf-8 library

- Added ``search()`` for vocabulary search

- Added ``pinyin()`` for single character Pinyin search

<br/>

## To-do List

~~- Multi-character Pinyin search~~ Achieved in v1.0.3 (See [Minimalist Release](https://github.com/pystander/LiteraPy/releases/tag/1.0.3))

- AI with word suggestions and identifier for Chinese part of speech (主謂賓 定狀補)

- More languages to be supported

<br/>

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<br/>

## References

[1] [MDBG Chinese Dictionary](https://www.mdbg.net/chinese/dictionary?page=cedict)

[2] [CC-CEDICT Home [CC-CEDICT WIKI]](https://cc-cedict.org/wiki/)
