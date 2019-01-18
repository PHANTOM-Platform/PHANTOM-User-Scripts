#!/usr/bin/env python3

import argparse
import repository


	
parser = argparse.ArgumentParser(description='Manages the authentication with the repository. By default tries to authenticate a user and get the corresponding token')
parser.add_argument('-r', '--register', dest='register', action='store_true' , help='Attempts to register the user' )
parser.add_argument('user', nargs=1, help='email of the user')
parser.add_argument('password', nargs=1, help='password corresponding to the email')
parser.add_argument('-token', dest="tk_path", help='Name of the file with the token. Default is token.txt', default='token.txt')

args = parser.parse_args()

print('filename: ', args.tk_path)
print('user: ', args.user)
print('password: ', args.password)

if args.register == True:
	repository.register(args.user,args.password)

tk = repository.authenticate(args.user,args.password)
f = open(args.tk_path,"w")
f.write(str(tk))
f.close()
	


