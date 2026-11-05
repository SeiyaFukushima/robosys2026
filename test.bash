#!/bin/bash
ng (){
	echo${1}行目のテスト失敗
}

ng 123

res=0
a=seiya
[ "$a" = seiya ] || ng "$LINENO"
[ "$a" = seiya ] || ng "$LINENO"
 
exit $res
