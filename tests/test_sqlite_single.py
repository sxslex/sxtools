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
#    by sx.slex@gmail.com

from sxtools import SqliteSingle
import unittest
import tempfile
import os
path_db = os.path.join(tempfile.gettempdir(), 'students.db')


class TestSqliteSingle(unittest.TestCase):

    def test_01_create_db(self):
        try:
            os.unlink(path_db)
        except:
            pass
        students = SqliteSingle(
            path_db,
            '''
               create table students (
                   id_students          integer primary key,
                   name                 varchar(100),
                   salary               float,
                   birthdate            date
               );
               create table assessments (
                   id_assessments       integer primary key,
                   id_students          integer,
                   grade                float
               );
            ''',
            debug=True
        )
        self.assertEqual(
            students.insert(
                'students',
                values=dict(id_students=1, name='slex', salary=3500.10)
            ),
            1
        )
        self.assertEqual(
            students.insert(
                'students',
                values=dict(id_students=2, name='denis', salary=8000.50)
            ),
            1
        )
        self.assertListEqual(
            students.select(
                table='students',
                fields=['id_students', 'name', 'salary', 'birthdate'],
                wheres=[dict(f='id_students', v=2)],
                limit=1
            ),
            [(2, u'denis', 8000.5, None)]
        )
        self.assertEqual(
            students.count(
                table='students'
            ),
            2
        )
        self.assertEqual(
            students.count(
                table='students',
                wheres=dict(f='id_students', v=2)
            ),
            1
        )
        self.assertEqual(
            students.query(
                sql='SELECT COUNT(*) FROM students'
            ),
            [(2,)]
        )
        if os.path.exists(path_db):
            os.unlink(path_db)
