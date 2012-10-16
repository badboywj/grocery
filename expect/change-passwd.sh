#!/bin/bash
#201105 version 0.0.2
#This shell will change user password,use expect.

DATE=`date +%Y%m%d" "%H:%M:%S`
LOG=/tmp/expectlog.$$.$RANDOM.log
TMPFILE=$RANDOM.log

GOODIPFILE=goodip.txt
BADIPFILE=badip.txt
FAILIP=fail_ip.txt

USERNAME=yourname
OLDPASSWD=xxxxxx  #注意特殊字符要加转义\,如“$”,需要写成“\$”. 可事先用autoexpect -p ssh x.x.x.x -p 22 命令记录一个你的修改密码过程，然后查看生成的script.exp，看你的特殊字符到底该如何转义。方便不是。不用死记expect的字符哪些需要转义。
NEWPASSWD=yyyyyy  #同上
SSHKEYFILE=$HOME/.ssh/known_hosts

#if host and 22 port is good,check out to goodip.txt
echo -e "Please input the all ip file name:"
read ALLIPFILE
echo -e "Begin check host and port..."
nmap -sT -p22 -v -i $ALLIPFILE|awk -F'[)(]'  '/^Host.*good.$/{print $2 >"'"$GOODIPFILE"'"}/^Host.*skipping it.$/{print $2 >"'"$BADIPFILE"'"}'
echo -e "Total number ip is `wc -l $ALLIPFILE`"
echo -e "Good ip number ip is `wc -l $GOODIPFILE`"
echo -e "Bad ip number ip is `wc -l $BADIPFILE`"

#change the username passwd with expect.exp
echo -e "Continue? Please input (y/n)"
read CONTINUE
if [ $CONTINUE = "y" ]
    then
    echo -e "BEGIN--->"
    echo -e "We will clean the $HOME/.ssh/known_hosts,please input (y/n)"
    read INPUT
    if [ $INPUT = "y" ]
    then
        echo >$SSHKEYFILE
        if [ $? -eq 0 ]
        then
              echo "Ok,$SSHKEYFILE has been cleand.We will go..."
              echo $DATE>>$LOG
              for i in `cat $GOODIPFILE`
              do
                ./expect.exp $USERNAME $i $OLDPASSWD $NEWPASSWD >>$LOG
              done
              echo -e "<---END"
              echo -e "Failed ip is(are):($FAILIP)"
              #this awk shell will select these ip of change passwd failed.
              awk -v var="" '/^'"$USERNAME"'@[0-9]/{gsub(/('"$USERNAME"'@)||([^0-9]s password:.*$)/,"");var=$0};/current/{print var > "'"$TMPFILE"'"}' $LOG
              grep -vFf $TMPFILE $GOODIPFILE > $FAILIP
              cat $FAILIP
              rm -f $TMPFILE
              #$LOG must been deleted.Because username and passwd had included by $LOG.
              #If you check the error in $LOG,can delete it after check it.
              #rm -f $LOG
        else
              echo "Sorry,$SSHKEYFILE has not been cleand,please check it."
              exit
        fi
    else
        echo "Sorry,$SSHKEYFILE must been cleand.Otherwise the ssh connect server will faild and expect will faild also."
        exit
    fi
else
    echo -e "Ok,bye."
    exit
fi
