# Generated from ./src/cminx/parser/CMake.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,15,227,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,1,0,1,0,1,1,1,1,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,61,8,2,1,2,5,2,64,8,2,10,2,12,2,67,9,2,1,2,
        1,2,1,3,1,3,3,3,73,8,3,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,5,6,94,8,6,10,6,12,6,97,
        9,6,1,7,1,7,4,7,101,8,7,11,7,12,7,102,1,8,1,8,1,8,3,8,108,8,8,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,119,8,10,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,5,12,128,8,12,10,12,12,12,131,9,12,1,12,
        1,12,1,13,1,13,1,13,3,13,138,8,13,1,13,3,13,141,8,13,1,14,1,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,153,8,15,10,15,12,15,
        156,9,15,1,15,3,15,159,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,5,17,173,8,17,10,17,12,17,176,9,17,1,17,1,
        17,5,17,180,8,17,10,17,12,17,183,9,17,1,17,1,17,5,17,187,8,17,10,
        17,12,17,190,9,17,1,17,1,17,5,17,194,8,17,10,17,12,17,197,9,17,3,
        17,199,8,17,1,17,1,17,3,17,203,8,17,1,17,3,17,206,8,17,1,17,1,17,
        1,18,1,18,3,18,212,8,18,1,18,4,18,215,8,18,11,18,12,18,216,1,18,
        1,18,1,19,4,19,222,8,19,11,19,12,19,223,1,19,1,19,3,65,77,154,0,
        20,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,0,21,0,23,0,25,10,
        27,0,29,11,31,0,33,12,35,13,37,14,39,15,1,0,10,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,6,0,9,10,13,13,32,32,34,35,40,41,
        92,92,4,0,48,57,59,59,65,90,97,122,2,0,34,34,92,92,4,0,10,10,13,
        13,61,61,91,91,2,0,10,10,13,13,3,0,10,10,13,13,91,91,1,1,10,10,2,
        0,9,9,32,32,253,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,25,1,0,0,0,0,29,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,39,1,0,0,0,1,41,1,0,0,0,3,43,1,0,0,0,5,45,1,0,0,0,7,70,1,0,0,0,
        9,82,1,0,0,0,11,87,1,0,0,0,13,91,1,0,0,0,15,100,1,0,0,0,17,107,1,
        0,0,0,19,109,1,0,0,0,21,118,1,0,0,0,23,120,1,0,0,0,25,123,1,0,0,
        0,27,134,1,0,0,0,29,142,1,0,0,0,31,158,1,0,0,0,33,160,1,0,0,0,35,
        168,1,0,0,0,37,214,1,0,0,0,39,221,1,0,0,0,41,42,5,40,0,0,42,2,1,
        0,0,0,43,44,5,41,0,0,44,4,1,0,0,0,45,47,3,9,4,0,46,48,3,39,19,0,
        47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,64,0,0,50,51,5,
        109,0,0,51,52,5,111,0,0,52,53,5,100,0,0,53,54,5,117,0,0,54,55,5,
        108,0,0,55,56,5,101,0,0,56,60,1,0,0,0,57,58,3,39,19,0,58,59,3,15,
        7,0,59,61,1,0,0,0,60,57,1,0,0,0,60,61,1,0,0,0,61,65,1,0,0,0,62,64,
        9,0,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,66,1,0,0,0,65,63,1,0,0,0,
        66,68,1,0,0,0,67,65,1,0,0,0,68,69,3,11,5,0,69,6,1,0,0,0,70,72,3,
        9,4,0,71,73,3,39,19,0,72,71,1,0,0,0,72,73,1,0,0,0,73,77,1,0,0,0,
        74,76,9,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,78,1,0,0,0,77,75,1,
        0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,3,11,5,0,81,8,1,0,0,0,82,
        83,5,35,0,0,83,84,5,91,0,0,84,85,5,91,0,0,85,86,5,91,0,0,86,10,1,
        0,0,0,87,88,5,35,0,0,88,89,5,93,0,0,89,90,5,93,0,0,90,12,1,0,0,0,
        91,95,7,0,0,0,92,94,7,1,0,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,
        0,0,0,95,96,1,0,0,0,96,14,1,0,0,0,97,95,1,0,0,0,98,101,8,2,0,0,99,
        101,3,17,8,0,100,98,1,0,0,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,
        1,0,0,0,102,103,1,0,0,0,103,16,1,0,0,0,104,108,3,19,9,0,105,108,
        3,21,10,0,106,108,3,23,11,0,107,104,1,0,0,0,107,105,1,0,0,0,107,
        106,1,0,0,0,108,18,1,0,0,0,109,110,5,92,0,0,110,111,8,3,0,0,111,
        20,1,0,0,0,112,113,5,92,0,0,113,119,5,116,0,0,114,115,5,92,0,0,115,
        119,5,114,0,0,116,117,5,92,0,0,117,119,5,110,0,0,118,112,1,0,0,0,
        118,114,1,0,0,0,118,116,1,0,0,0,119,22,1,0,0,0,120,121,5,92,0,0,
        121,122,5,59,0,0,122,24,1,0,0,0,123,129,5,34,0,0,124,128,8,4,0,0,
        125,128,3,17,8,0,126,128,3,27,13,0,127,124,1,0,0,0,127,125,1,0,0,
        0,127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,
        0,130,132,1,0,0,0,131,129,1,0,0,0,132,133,5,34,0,0,133,26,1,0,0,
        0,134,140,5,92,0,0,135,137,5,13,0,0,136,138,5,10,0,0,137,136,1,0,
        0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,141,5,10,0,0,140,135,1,0,
        0,0,140,139,1,0,0,0,141,28,1,0,0,0,142,143,5,91,0,0,143,144,3,31,
        15,0,144,145,5,93,0,0,145,30,1,0,0,0,146,147,5,61,0,0,147,148,3,
        31,15,0,148,149,5,61,0,0,149,159,1,0,0,0,150,154,5,91,0,0,151,153,
        9,0,0,0,152,151,1,0,0,0,153,156,1,0,0,0,154,155,1,0,0,0,154,152,
        1,0,0,0,155,157,1,0,0,0,156,154,1,0,0,0,157,159,5,93,0,0,158,146,
        1,0,0,0,158,150,1,0,0,0,159,32,1,0,0,0,160,161,5,35,0,0,161,162,
        5,91,0,0,162,163,1,0,0,0,163,164,3,31,15,0,164,165,5,93,0,0,165,
        166,1,0,0,0,166,167,6,16,0,0,167,34,1,0,0,0,168,198,5,35,0,0,169,
        199,1,0,0,0,170,174,5,91,0,0,171,173,5,61,0,0,172,171,1,0,0,0,173,
        176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,199,1,0,0,0,176,
        174,1,0,0,0,177,181,5,91,0,0,178,180,5,61,0,0,179,178,1,0,0,0,180,
        183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,
        181,1,0,0,0,184,188,8,5,0,0,185,187,8,6,0,0,186,185,1,0,0,0,187,
        190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,199,1,0,0,0,190,
        188,1,0,0,0,191,195,8,7,0,0,192,194,8,6,0,0,193,192,1,0,0,0,194,
        197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,199,1,0,0,0,197,
        195,1,0,0,0,198,169,1,0,0,0,198,170,1,0,0,0,198,177,1,0,0,0,198,
        191,1,0,0,0,199,205,1,0,0,0,200,202,5,13,0,0,201,203,5,10,0,0,202,
        201,1,0,0,0,202,203,1,0,0,0,203,206,1,0,0,0,204,206,7,8,0,0,205,
        200,1,0,0,0,205,204,1,0,0,0,206,207,1,0,0,0,207,208,6,17,0,0,208,
        36,1,0,0,0,209,211,5,13,0,0,210,212,5,10,0,0,211,210,1,0,0,0,211,
        212,1,0,0,0,212,215,1,0,0,0,213,215,5,10,0,0,214,209,1,0,0,0,214,
        213,1,0,0,0,215,216,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        218,1,0,0,0,218,219,6,18,0,0,219,38,1,0,0,0,220,222,7,9,0,0,221,
        220,1,0,0,0,222,223,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,
        225,1,0,0,0,225,226,6,19,0,0,226,40,1,0,0,0,28,0,47,60,65,72,77,
        95,100,102,107,118,127,129,137,140,154,158,174,181,188,195,198,202,
        205,211,214,216,223,1,6,0,0
    ]

class CMakeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Module_docstring = 3
    Docstring = 4
    Doccomment_start = 5
    Blockcomment_end = 6
    Identifier = 7
    Unquoted_argument = 8
    Escape_sequence = 9
    Quoted_argument = 10
    Bracket_argument = 11
    Bracket_comment = 12
    Line_comment = 13
    Newline = 14
    Space = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'#[[['", "'#]]'" ]

    symbolicNames = [ "<INVALID>",
            "Module_docstring", "Docstring", "Doccomment_start", "Blockcomment_end", 
            "Identifier", "Unquoted_argument", "Escape_sequence", "Quoted_argument", 
            "Bracket_argument", "Bracket_comment", "Line_comment", "Newline", 
            "Space" ]

    ruleNames = [ "T__0", "T__1", "Module_docstring", "Docstring", "Doccomment_start", 
                  "Blockcomment_end", "Identifier", "Unquoted_argument", 
                  "Escape_sequence", "Escape_identity", "Escape_encoded", 
                  "Escape_semicolon", "Quoted_argument", "Quoted_cont", 
                  "Bracket_argument", "Bracket_arg_nested", "Bracket_comment", 
                  "Line_comment", "Newline", "Space" ]

    grammarFileName = "CMake.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


