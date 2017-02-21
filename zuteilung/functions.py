# zuteilungen/functions.py
# -*- coding: UTF-8 -*-

import cx_Oracle

class Zuteilungen:
    def get_filialumsatz(self, p_jahr, p_manr, p_lanr):
        l_umsatz = self.__cursor.callfunc("PKG_ZUTEILUNG.GET_FILIALUMSATZ",
                                         cx_Oracle.VARCHAR2, [p_jahr, p_manr, p_lanr])
        return l_umsatz

    def get_filialumsatz_wabe(self, p_jahr, p_manr, p_lanr, p_wabe):
        l_umsatz = self.__cursor.callfunc("PKG_ZUTEILUNG.GET_FILIALUMSATZ",
                                         cx_Oracle.VARCHAR2, [p_jahr, p_manr, p_lanr, p_wabe])
        return l_umsatz