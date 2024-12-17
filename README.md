# mfmt

mfmt (pronounced "em-format") is a tool for converting the output format of one morphological analyzer to another. It supports the following analyzers:

- [MeCab](https://taku910.github.io/mecab/)
- [Juman](https://nlp.ist.i.kyoto-u.ac.jp/?JUMAN) ([Juman++](https://nlp.ist.i.kyoto-u.ac.jp/?JUMAN%2B%2B))
- [KyTea](https://www.phontron.com/kytea/index-ja.html)
- [Vaporetto](https://github.com/daac-tools/vaporetto) (bccwj-suw+unidic_pos+kana)

## Install

```Shell
$ pipx install mfmt
```

## Usage

```Shell
$ mfmt <command> <file>
```

`<command>` consists of the short forms of each analyzer. In mfmt, the following abbreviations are used:

- m: MeCab
- j: Juman (Juman++)
- k: KyTea
- v: Vaporetto

For example, to convert the output format from MeCab to Juman:

```Shell
$ mfmt m2j mecab.txt
```

Conversely, to convert the format from Juman to MeCab:

```Shell
$ mfmt j2m juman.txt
```

Please note that mfmt does not convert parts of speech. This is because it is difficult to map the part-of-speech categories between different analyzers.

## Example

```Shell
$ cat mecab.txt
今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
よい	形容詞,自立,*,*,形容詞・アウオ段,基本形,よい,ヨイ,ヨイ
天気	名詞,一般,*,*,*,*,天気,テンキ,テンキ
です	助動詞,*,*,*,特殊・デス,基本形,です,デス,デス
。	記号,句点,*,*,*,*,。,。,。
EOS

$ mfmt m2j mecab.txt > juman.txt

$ cat juman.txt
今日 きょう * 名詞 * 副詞可能 * * * * * *
は は * 助詞 * 係助詞 * * * * * *
よい よい * 形容詞 * 自立 * * * * * *
天気 てんき * 名詞 * 一般 * * * * * *
です です * 助動詞 * * * * * * * *
。 。 * 記号 * 句点 * * * * * *
EOS
```
