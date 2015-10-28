#!/usr/bin/python -tt

"""
Gender words 
"""


MALE_WORDS=set(['guy','spokesman','chairman',"men's",'men','him',"he's",'his',
	'boy','boyfriend','boyfriends','boys','brother','brothers','dad',
	'dads','dude','father','fathers','fiance','gentleman','gentlemen',
	'god','grandfather','grandpa','grandson','groom','he','himself',
	'husband','husbands','king','male','man','mr','nephew','nephews',
	'priest','prince','son','sons','uncle','uncles','waiter','widower',
	'widowers'])
FEMALE_WORDS=set(['heroine','spokeswoman','chairwoman',"women's",'actress','women',
	"she's",'her','aunt','aunts','bride','daughter','daughters','female',
	'fiancee','girl','girlfriend','girlfriends','girls','goddess',
	'granddaughter','grandma','grandmother','grandmothers','herself','ladies','lady',
	'lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
	'priestess','princess','queens','she','sister','sisters','waitress',
	'widow','widows','wife','wives','woman'])

if __name__ == '__main__':
	print MALE_WORDS, FEMALE_WORDS