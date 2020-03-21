#
# JiWER - Jitsi Word Error Rate
#
# Copyright @ 2018 - present 8x8, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This file implements methods to transform text input. It implements some useful
processing steps which are advised when calculating the WER,
such as filtering out common words and standardizing abbreviations.
"""

import re
from typing import Union, List

import string

whitespace_characters = [c for c in string.whitespace]
punctuation_characters = [c for c in string.punctuation]

class Compose(object):

    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, text):
        for tr in self.transforms:
            text = tr(text)

        return text

class BaseTransform(object):

    def __call__(self, sentences: Union[str, List[str]]):
        if isinstance(sentences, str):
            return self.process_string(sentences)
        elif isinstance(sentences, list):
            return self.process_list(sentences)
        else:
            raise ValueError("input {} was expected to be a string or list of strings".format(sentences))


    def process_string(self, s: str):
        raise NotImplementedError()

    def process_list(self, inp: List[str]):
        return [self.process_string(s) for s in inp]


class SentenceToListOfWords(BaseTransform):

    def __init__(self, word_delimiter=" ", sentence_delimiter=None):
        """
        Transforms one or more sentences into a list of words. A sentence is
        assumed to be a string, where words are delimited by a token
        (such as ` `, space).

        :param word_delimiter: the character which delimits words. Default is ` ` (space).
        :param sentence_delimiter: the character which delimits sentences. Default is None (sentences are not delimited)
        """
        self.word_delimiter = word_delimiter
        self.sentence_delimiter = sentence_delimiter

    def process_string(self, s: str):
        if self.sentence_delimiter is not None:
            s = s.split(self.sentence_delimiter)

        return s.split(self.word_delimiter)



class RemoveSpecificWords(BaseTransform):

    def __init__(self, words_to_remove: List[str]):
        self.words_to_remove = words_to_remove

    def process_string(self, s: str):
        for w in self.words_to_remove:
            s = s.replace(w, "", )

        return s

class RemoveWhiteSpace(BaseTransform):

    def __init__(self, characters=string.whitespace):

class RemoveMultipleSpaces(BaseTransform):

    def process_string(self, s: str):
        return re.sub("\s\s+", " ", s)



class ExpandAbbreviations:
    pass


class ToLowerCase(object):
    pass


class RemoveNonWords(object):
    pass

class Remove