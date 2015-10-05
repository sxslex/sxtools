# -*- coding: utf-8 -*-
#
# Copyright 2015 Alexandre Villela (SleX) <https://github.com/sxslex/sxtools/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# sqlite_single - Class to work access to a SQLite database simply
#   sx.slex@gmail.com
# Thanks:
#   @denisfrm
#
import contextlib
import sqlite3
import pprint
import os


class SqliteSingle():
    def __init__(self, filename, sql_create=None, debug=False):
        self.filename = filename
        self.sql_create = sql_create
        self.con = None
        self.cur = None
        self.debug = debug

    def open_db(self):
        if self.debug:
            print('open_db')
        to_create = not os.path.exists(self.filename)
        self.con = sqlite3.connect(self.filename)
        self.cur = self.con.cursor()
        if to_create and self.sql_create:
            self.cur.executescript(self.sql_create)
            self.con.commit()

    def close_db(self):
        if self.debug:
            print('close_db')
        if self.cur:
            self.cur.close()
            self.cur = None
        if self.con:
            self.con.close()
            self.con = None

    @contextlib.contextmanager
    def transaction(self):
        try:
            it_is_open = bool(self.cur)
            if not it_is_open:
                self.open_db()
            yield
        finally:
            if not it_is_open:
                self.close_db()

    def insert(self, table, values, commit=True):
        campos = values.keys()
        campos.sort()
        sql = 'INSERT INTO %s(%s) VALUES(%s)' % (
            table,
            ', '.join(campos),
            ', '.join(['?' for i in campos]),
        )
        params = [values[c] for c in campos]
        if self.debug:
            pprint.pprint([sql, params])
        with self.transaction():
            resp = self.cur.execute(
                sql,
                params
            )
            if commit:
                self.con.commit()
            return resp.rowcount

    def make_where(self, wheres):
        if not wheres:
            wheres = []
        if isinstance(wheres, dict):
            wheres = [wheres]
        lwheres = []
        vwheres = []
        for where in wheres:
            lwheres.append(
                '%s %s ?' % (where['f'], where.get('o', '='))
            )
            vwheres.append(where['v'])
        return lwheres, vwheres

    def count(self, table, wheres=None, field='*'):
        lwheres, vwheres = self.make_where(wheres)
        sql = 'SELECT COUNT(%s) FROM %s' % (field, table)
        if lwheres:
            sql += ' WHERE '
            sql += ' AND '.join(lwheres)
        if self.debug:
            pprint.pprint([sql, vwheres])
        with self.transaction():
            self.cur.execute(
                sql,
                vwheres
            )
            return self.cur.fetchone()[0]

    def select(self, table, wheres=None, fields='*', limit=None, offset=None):
        lwheres, vwheres = self.make_where(wheres)
        if isinstance(fields, (list, tuple)):
            fields = ', '.join(fields)
        sql = 'SELECT %s FROM %s' % (fields, table)
        if lwheres:
            sql += ' WHERE '
            sql += ' AND '.join(lwheres)
        if limit:
            sql += ' LIMIT %s' % str(limit)
        if self.debug:
            pprint.pprint([sql, vwheres])
        with self.transaction():
            self.cur.execute(
                sql,
                vwheres
            )
            return self.cur.fetchall()

    def query(self, sql, params):
        with self.transaction():
            self.cur.execute(
                sql,
                params
            )
            return self.cur.fetchall()


# if __name__ == '__main__':
#     if os.path.exists('students.db'):
#         os.unlink('students.db')
#     students = SqliteSingle(
#         'students.db',
#         '''
#            create table students (
#                id_students          integer primary key,
#                name                 varchar(100),
#                salary               float,
#                birthdate            date
#            );
#            create table assessments (
#                id_assessments       integer primary key,
#                id_students          integer,
#                grade                float
#            );
#         ''',
#         debug=True
#     )
#     print students.insert(
#         'students',
#         values=dict(id_students=1, name='slex', salary=3500.10)
#     )
#     print students.insert(
#         'students',
#         values=dict(id_students=2, name='denis', salary=8000.50)
#     )
#     print students.select(
#         'students',
#         [dict(f='id_students', v=2)]
#     )
