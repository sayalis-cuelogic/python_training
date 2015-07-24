from nose.tools import *
from ex49.parser import* 

def test():
	x = parse_sentence([('noun','bear'),
						('verb','eat'),
						('stop','the'),
						('noun','honey')])

	check_class(x)

	assert_equal(x.subject,'bear')
	assert_equal(x.verb,'eat')
	assert_equal(x.object,'honey')


def test_none_verb_object():
	y = parse_sentence([('verb','run'),('direction','north')])

	check_class(y)

	assert_equal(y.subject,'player')
	assert_equal(y.verb,'run')
	assert_equal(y.object,'north')


def test_error_nosubject():
	assert_raises(ParserError,parse_sentence,([('error','error'),
											   ('verb','eat'),
											   ('stop','the'),
											   ('noun','honey')]))


def test_error_noverb():
	assert_raises(ParserError,parse_sentence,([('noun','bear'),
											   ('error','error'),
											   ('direction','north')]))


def test_error_noobject():
	assert_raises(ParserError,parse_sentence,([('noun','bear'),
											   ('verb','go'),
											   ('error','error')]))


def test_error_noparam():
	assert_raises(ParserError,parse_sentence,([]))

		
def check_class(obj):
	assert_equal(isinstance(obj, Sentence), True)