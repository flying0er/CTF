#!/usr/bin/env python
# -*- coding: utf-8 -*-
decode = lambda x: bin(int(x, 16))[2:].replace('0',' ').replace('1', 'X')

print decode('C03B800000000E0000383800180FFFF18F6D8000000F9B0000186C000C1BB581866DEDB6EE06C3F8EF9E0DBBCC1831E3066DB6DB6C06CE7DB7DB38EF06183181B66DB6DB6C078355F55B0CC3CC1B3181B66DB6DB2806DB55855B6CC0EC0E7BC19C39B6DB380F6E54F57E39E7CC000000C000000030000000000000001800000000000000E1F8')
