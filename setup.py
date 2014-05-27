#encoding:utf-8
from cx_Freeze import setup,Executable

setup(
	name = "OJ_Register",
	version = "1",
	description = "Register form swjtu oj.",
	executables = [Executable("oj.py")]
	)
