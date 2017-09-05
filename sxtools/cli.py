# -*- coding: utf-8 -*-

# Copyright 2015-2017 Alexandre Villela <https://github.com/sxslex/sxtools/>
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


import click
import sxtools


@click.group()
@click.version_option(version=sxtools.__version__, prog_name='sxtools')
def cli():
    pass


@cli.command(help='Converts the word to the plural')
@click.argument('word')
def pluralize(word):
    print(sxtools.pluralize(word))


@cli.command(help='Remove accents from text')
@click.argument('text')
def removeaccents(text):
    print(sxtools.remove_accents(text))


@cli.command(
    help=(
        'Returns the correct writing of a compound name, '
        'respecting the first letters of the names in upper case.'
    )
)
@click.argument('text')
def capitalize(text):
    print(sxtools.capitalize(text))

if __name__ == '__main__':
    cli()
