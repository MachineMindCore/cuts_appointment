username=$1
password=$2
firstName="admin"
lastName="permission"
number=$RANDOM
email="${number}@mail.com"
flag="admin"
python push_user.py $username $password $firstName $lastName $number $email $flag